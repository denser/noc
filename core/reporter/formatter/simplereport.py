# ----------------------------------------------------------------------
# SimpleReport DataFormatter
# ----------------------------------------------------------------------
# Copyright (C) 2007-2023 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from typing import List, Any, Optional, Tuple

# Third-party modules
from jinja2 import Template as Jinja2Template
from xlsxwriter.workbook import Workbook

# NOC modules
from .base import DataFormatter
from ..types import OutputType, BandFormat
from ..report import BandData
from noc.services.web.base.simplereport import (
    Report,
    TextSection,
    TableSection,
    SectionRow,
    TableColumn,
)


class SimpleReportFormatter(DataFormatter):
    def render_document(self):
        """

        :return:
        """
        if self.report_template.output_type != OutputType.HTML:
            self.render_table()
            return
        report = Report()
        rband_format = self.get_band_format(self.root_band)
        report.append_section(
            TextSection(title=rband_format.title_template if rband_format else "")
        )
        columns, fields = self.get_columns()
        report.append_section(
            TableSection(
                columns=list(columns),
                data=self.get_report_data(fields),
                enumerate=False,
            )
        )
        if self.output_type == OutputType.CSV:
            r = report.to_csv(delimiter=self.csv_delimiter)
        elif self.output_type == OutputType.SSV:
            r = report.to_csv(delimiter=";")
        elif self.output_type == OutputType.HTML:
            r = report.to_html(include_buttons=False)
        elif self.output_type == OutputType.XLSX:
            r = report.to_csv(delimiter=";")
            workbook = Workbook(self.output_stream)
            worksheet = workbook.add_worksheet()
            for r, row in enumerate(r.splitlines()):
                for c, col in enumerate(row.split(";")):
                    worksheet.write(r, c, col)
            workbook.close()
            return
        else:
            raise NotImplementedError(f"Output Type {self.output_type} not supported")
        self.output_stream.write(r.encode("utf8"))

    def render_table(self):
        """
        Format for Root Band data as table
        :return:
        """
        r_format = self.report_template.bands_format["Root"]
        # Column title map
        HEADER_ROW = {}
        for col in r_format.columns:
            HEADER_ROW[col.name] = col.title
        data = self.root_band.rows
        if data is None:
            return
        out_columns = [c for c in data.columns]
        if self.output_type in {OutputType.CSV, OutputType.SSV, OutputType.CSV_ZIP}:
            r = self.csv_delimiter.join(HEADER_ROW.get(cc, cc) for cc in data.columns) + "\n"
            r += data.select(out_columns).write_csv(
                # header=[self.HEADER_ROW.get(cc, cc) for cc in out_columns],
                # columns=out_columns,
                sep=self.csv_delimiter,
                quote='"',
                has_header=False,
            )
            self.output_stream.write(r.encode("utf8"))
        elif self.output_type == OutputType.XLSX:
            book = Workbook(self.output_stream)
            cf1 = book.add_format({"bottom": 1, "left": 1, "right": 1, "top": 1})
            worksheet = book.add_worksheet("Alarms")
            for cn, col in enumerate(out_columns):
                worksheet.write(0, cn, HEADER_ROW.get(col, col), cf1)
            for cn, col in enumerate(out_columns):
                worksheet.write_column(1, cn, data[col], cf1)
            (max_row, max_col) = data.shape
            worksheet.autofilter(0, 0, max_row, len(out_columns))
            worksheet.freeze_panes(1, 0)
            for i, width in enumerate(self.get_col_widths(data)):
                worksheet.set_column(i, i, width)
            #
            book.close()

    @staticmethod
    def get_col_widths(dataframe, index_filed: Optional[str] = None):
        # Then, we concatenate this to the max of the lengths
        # of column name and its values for each column, left to right
        r = [max([len(str(s)) for s in dataframe[col]] + [len(col)]) for col in dataframe.columns]
        # First we find the maximum length of the index column
        if index_filed:
            idx_max = max([len(str(s)) for s in dataframe[index_filed]] + [len(str(index_filed))])
            return [idx_max] + r
        return r

    def get_report_data(self, columns: List[str] = None) -> List[Any]:
        """
        Convert Report Band to Report Data Section
        :return:
        """
        r = []
        for rb in self.root_band.iter_all_bands():
            # Section Row
            if not rb.is_root:  # Section
                bf = self.get_band_format(rb)
                if bf and bf.title_template:
                    r.append(SectionRow(self.get_title(rb, bf.title_template)))
                    if rb.rows is None:
                        continue
            # Out data
            if not rb.has_children and rb.rows is not None and not rb.rows.is_empty():
                row_columns = columns or rb.rows.columns
                for row in rb.rows.to_dicts():
                    r.append([row.get(c, "") for c in row_columns])
            elif not rb.has_children and rb.data:
                row_columns = columns or list(rb.data)
                r.append([rb.data.get(c, "") for c in row_columns])
        return r

    def get_band_format(self, band: BandData) -> Optional[BandFormat]:
        """

        :return:
        """
        if band.format:
            return band.format
        if (
            not self.report_template.bands_format
            or band.name not in self.report_template.bands_format
        ):
            return
        return self.report_template.bands_format[band.name]

    def get_columns(self) -> Tuple[List[Any], Optional[List[str]]]:
        """
        Return columns format and fields list
        :return:
        """
        # Try Root config first
        band_format = self.get_band_format(self.root_band)
        band = self.root_band.get_data_band()
        fields = None
        # Try DataBand
        if not band_format or not band_format.columns:
            band_format = self.get_band_format(band)
            fields = [c.name for c in band_format.columns] if band_format else None
        if not band_format:
            return ([fn for fn in band.rows.columns],) * 2
        columns = []
        for c in band_format.columns:
            if c.format_type or c.total:
                columns += [
                    TableColumn(
                        c.title or "",
                        align=c.align.name.lower(),
                        format=c.format_type,
                        total=c.total,
                        total_label=c.total_label,
                    )
                ]
            else:
                columns += [c.title or ""]
        return columns, fields

    @staticmethod
    def get_title(band, template: Optional[str] = None) -> str:
        """
        Render Band Title if setting template
        :return:
        """
        if not template:
            return band.name
        return Jinja2Template(template).render(band.get_data())
