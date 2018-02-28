# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# RMON2-MIB
#     Compiled MIB
#     Do not modify this file directly
#     Run ./noc make-cmib instead
# ----------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# MIB Name
NAME = "RMON2-MIB"
# Metadata
LAST_UPDATED = "1999-06-22"
COMPILED = "2018-02-28"
# MIB Data: name -> oid
MIB = {
    "RMON2-MIB::etherStats2Table": "1.3.6.1.2.1.16.1.4",
    "RMON2-MIB::etherStats2Entry": "1.3.6.1.2.1.16.1.4.1",
    "RMON2-MIB::etherStatsDroppedFrames": "1.3.6.1.2.1.16.1.4.1.1",
    "RMON2-MIB::etherStatsCreateTime": "1.3.6.1.2.1.16.1.4.1.2",
    "RMON2-MIB::tokenRingMLStats2Table": "1.3.6.1.2.1.16.1.5",
    "RMON2-MIB::tokenRingMLStats2Entry": "1.3.6.1.2.1.16.1.5.1",
    "RMON2-MIB::tokenRingMLStatsDroppedFrames": "1.3.6.1.2.1.16.1.5.1.1",
    "RMON2-MIB::tokenRingMLStatsCreateTime": "1.3.6.1.2.1.16.1.5.1.2",
    "RMON2-MIB::tokenRingPStats2Table": "1.3.6.1.2.1.16.1.6",
    "RMON2-MIB::tokenRingPStats2Entry": "1.3.6.1.2.1.16.1.6.1",
    "RMON2-MIB::tokenRingPStatsDroppedFrames": "1.3.6.1.2.1.16.1.6.1.1",
    "RMON2-MIB::tokenRingPStatsCreateTime": "1.3.6.1.2.1.16.1.6.1.2",
    "RMON2-MIB::historyControl2Table": "1.3.6.1.2.1.16.2.5",
    "RMON2-MIB::historyControl2Entry": "1.3.6.1.2.1.16.2.5.1",
    "RMON2-MIB::historyControlDroppedFrames": "1.3.6.1.2.1.16.2.5.1.1",
    "RMON2-MIB::hostControl2Table": "1.3.6.1.2.1.16.4.4",
    "RMON2-MIB::hostControl2Entry": "1.3.6.1.2.1.16.4.4.1",
    "RMON2-MIB::hostControlDroppedFrames": "1.3.6.1.2.1.16.4.4.1.1",
    "RMON2-MIB::hostControlCreateTime": "1.3.6.1.2.1.16.4.4.1.2",
    "RMON2-MIB::matrixControl2Table": "1.3.6.1.2.1.16.6.4",
    "RMON2-MIB::matrixControl2Entry": "1.3.6.1.2.1.16.6.4.1",
    "RMON2-MIB::matrixControlDroppedFrames": "1.3.6.1.2.1.16.6.4.1.1",
    "RMON2-MIB::matrixControlCreateTime": "1.3.6.1.2.1.16.6.4.1.2",
    "RMON2-MIB::channel2Table": "1.3.6.1.2.1.16.7.3",
    "RMON2-MIB::channel2Entry": "1.3.6.1.2.1.16.7.3.1",
    "RMON2-MIB::channelDroppedFrames": "1.3.6.1.2.1.16.7.3.1.1",
    "RMON2-MIB::channelCreateTime": "1.3.6.1.2.1.16.7.3.1.2",
    "RMON2-MIB::filter2Table": "1.3.6.1.2.1.16.7.4",
    "RMON2-MIB::filter2Entry": "1.3.6.1.2.1.16.7.4.1",
    "RMON2-MIB::filterProtocolDirDataLocalIndex": "1.3.6.1.2.1.16.7.4.1.1",
    "RMON2-MIB::filterProtocolDirLocalIndex": "1.3.6.1.2.1.16.7.4.1.2",
    "RMON2-MIB::ringStationControl2Table": "1.3.6.1.2.1.16.10.7",
    "RMON2-MIB::ringStationControl2Entry": "1.3.6.1.2.1.16.10.7.1",
    "RMON2-MIB::ringStationControlDroppedFrames": "1.3.6.1.2.1.16.10.7.1.1",
    "RMON2-MIB::ringStationControlCreateTime": "1.3.6.1.2.1.16.10.7.1.2",
    "RMON2-MIB::sourceRoutingStats2Table": "1.3.6.1.2.1.16.10.8",
    "RMON2-MIB::sourceRoutingStats2Entry": "1.3.6.1.2.1.16.10.8.1",
    "RMON2-MIB::sourceRoutingStatsDroppedFrames": "1.3.6.1.2.1.16.10.8.1.1",
    "RMON2-MIB::sourceRoutingStatsCreateTime": "1.3.6.1.2.1.16.10.8.1.2",
    "RMON2-MIB::protocolDir": "1.3.6.1.2.1.16.11",
    "RMON2-MIB::protocolDirLastChange": "1.3.6.1.2.1.16.11.1",
    "RMON2-MIB::protocolDirTable": "1.3.6.1.2.1.16.11.2",
    "RMON2-MIB::protocolDirEntry": "1.3.6.1.2.1.16.11.2.1",
    "RMON2-MIB::protocolDirID": "1.3.6.1.2.1.16.11.2.1.1",
    "RMON2-MIB::protocolDirParameters": "1.3.6.1.2.1.16.11.2.1.2",
    "RMON2-MIB::protocolDirLocalIndex": "1.3.6.1.2.1.16.11.2.1.3",
    "RMON2-MIB::protocolDirDescr": "1.3.6.1.2.1.16.11.2.1.4",
    "RMON2-MIB::protocolDirType": "1.3.6.1.2.1.16.11.2.1.5",
    "RMON2-MIB::protocolDirAddressMapConfig": "1.3.6.1.2.1.16.11.2.1.6",
    "RMON2-MIB::protocolDirHostConfig": "1.3.6.1.2.1.16.11.2.1.7",
    "RMON2-MIB::protocolDirMatrixConfig": "1.3.6.1.2.1.16.11.2.1.8",
    "RMON2-MIB::protocolDirOwner": "1.3.6.1.2.1.16.11.2.1.9",
    "RMON2-MIB::protocolDirStatus": "1.3.6.1.2.1.16.11.2.1.10",
    "RMON2-MIB::protocolDist": "1.3.6.1.2.1.16.12",
    "RMON2-MIB::protocolDistControlTable": "1.3.6.1.2.1.16.12.1",
    "RMON2-MIB::protocolDistControlEntry": "1.3.6.1.2.1.16.12.1.1",
    "RMON2-MIB::protocolDistControlIndex": "1.3.6.1.2.1.16.12.1.1.1",
    "RMON2-MIB::protocolDistControlDataSource": "1.3.6.1.2.1.16.12.1.1.2",
    "RMON2-MIB::protocolDistControlDroppedFrames": "1.3.6.1.2.1.16.12.1.1.3",
    "RMON2-MIB::protocolDistControlCreateTime": "1.3.6.1.2.1.16.12.1.1.4",
    "RMON2-MIB::protocolDistControlOwner": "1.3.6.1.2.1.16.12.1.1.5",
    "RMON2-MIB::protocolDistControlStatus": "1.3.6.1.2.1.16.12.1.1.6",
    "RMON2-MIB::protocolDistStatsTable": "1.3.6.1.2.1.16.12.2",
    "RMON2-MIB::protocolDistStatsEntry": "1.3.6.1.2.1.16.12.2.1",
    "RMON2-MIB::protocolDistStatsPkts": "1.3.6.1.2.1.16.12.2.1.1",
    "RMON2-MIB::protocolDistStatsOctets": "1.3.6.1.2.1.16.12.2.1.2",
    "RMON2-MIB::addressMap": "1.3.6.1.2.1.16.13",
    "RMON2-MIB::addressMapInserts": "1.3.6.1.2.1.16.13.1",
    "RMON2-MIB::addressMapDeletes": "1.3.6.1.2.1.16.13.2",
    "RMON2-MIB::addressMapMaxDesiredEntries": "1.3.6.1.2.1.16.13.3",
    "RMON2-MIB::addressMapControlTable": "1.3.6.1.2.1.16.13.4",
    "RMON2-MIB::addressMapControlEntry": "1.3.6.1.2.1.16.13.4.1",
    "RMON2-MIB::addressMapControlIndex": "1.3.6.1.2.1.16.13.4.1.1",
    "RMON2-MIB::addressMapControlDataSource": "1.3.6.1.2.1.16.13.4.1.2",
    "RMON2-MIB::addressMapControlDroppedFrames": "1.3.6.1.2.1.16.13.4.1.3",
    "RMON2-MIB::addressMapControlOwner": "1.3.6.1.2.1.16.13.4.1.4",
    "RMON2-MIB::addressMapControlStatus": "1.3.6.1.2.1.16.13.4.1.5",
    "RMON2-MIB::addressMapTable": "1.3.6.1.2.1.16.13.5",
    "RMON2-MIB::addressMapEntry": "1.3.6.1.2.1.16.13.5.1",
    "RMON2-MIB::addressMapTimeMark": "1.3.6.1.2.1.16.13.5.1.1",
    "RMON2-MIB::addressMapNetworkAddress": "1.3.6.1.2.1.16.13.5.1.2",
    "RMON2-MIB::addressMapSource": "1.3.6.1.2.1.16.13.5.1.3",
    "RMON2-MIB::addressMapPhysicalAddress": "1.3.6.1.2.1.16.13.5.1.4",
    "RMON2-MIB::addressMapLastChange": "1.3.6.1.2.1.16.13.5.1.5",
    "RMON2-MIB::nlHost": "1.3.6.1.2.1.16.14",
    "RMON2-MIB::hlHostControlTable": "1.3.6.1.2.1.16.14.1",
    "RMON2-MIB::hlHostControlEntry": "1.3.6.1.2.1.16.14.1.1",
    "RMON2-MIB::hlHostControlIndex": "1.3.6.1.2.1.16.14.1.1.1",
    "RMON2-MIB::hlHostControlDataSource": "1.3.6.1.2.1.16.14.1.1.2",
    "RMON2-MIB::hlHostControlNlDroppedFrames": "1.3.6.1.2.1.16.14.1.1.3",
    "RMON2-MIB::hlHostControlNlInserts": "1.3.6.1.2.1.16.14.1.1.4",
    "RMON2-MIB::hlHostControlNlDeletes": "1.3.6.1.2.1.16.14.1.1.5",
    "RMON2-MIB::hlHostControlNlMaxDesiredEntries": "1.3.6.1.2.1.16.14.1.1.6",
    "RMON2-MIB::hlHostControlAlDroppedFrames": "1.3.6.1.2.1.16.14.1.1.7",
    "RMON2-MIB::hlHostControlAlInserts": "1.3.6.1.2.1.16.14.1.1.8",
    "RMON2-MIB::hlHostControlAlDeletes": "1.3.6.1.2.1.16.14.1.1.9",
    "RMON2-MIB::hlHostControlAlMaxDesiredEntries": "1.3.6.1.2.1.16.14.1.1.10",
    "RMON2-MIB::hlHostControlOwner": "1.3.6.1.2.1.16.14.1.1.11",
    "RMON2-MIB::hlHostControlStatus": "1.3.6.1.2.1.16.14.1.1.12",
    "RMON2-MIB::nlHostTable": "1.3.6.1.2.1.16.14.2",
    "RMON2-MIB::nlHostEntry": "1.3.6.1.2.1.16.14.2.1",
    "RMON2-MIB::nlHostTimeMark": "1.3.6.1.2.1.16.14.2.1.1",
    "RMON2-MIB::nlHostAddress": "1.3.6.1.2.1.16.14.2.1.2",
    "RMON2-MIB::nlHostInPkts": "1.3.6.1.2.1.16.14.2.1.3",
    "RMON2-MIB::nlHostOutPkts": "1.3.6.1.2.1.16.14.2.1.4",
    "RMON2-MIB::nlHostInOctets": "1.3.6.1.2.1.16.14.2.1.5",
    "RMON2-MIB::nlHostOutOctets": "1.3.6.1.2.1.16.14.2.1.6",
    "RMON2-MIB::nlHostOutMacNonUnicastPkts": "1.3.6.1.2.1.16.14.2.1.7",
    "RMON2-MIB::nlHostCreateTime": "1.3.6.1.2.1.16.14.2.1.8",
    "RMON2-MIB::nlMatrix": "1.3.6.1.2.1.16.15",
    "RMON2-MIB::hlMatrixControlTable": "1.3.6.1.2.1.16.15.1",
    "RMON2-MIB::hlMatrixControlEntry": "1.3.6.1.2.1.16.15.1.1",
    "RMON2-MIB::hlMatrixControlIndex": "1.3.6.1.2.1.16.15.1.1.1",
    "RMON2-MIB::hlMatrixControlDataSource": "1.3.6.1.2.1.16.15.1.1.2",
    "RMON2-MIB::hlMatrixControlNlDroppedFrames": "1.3.6.1.2.1.16.15.1.1.3",
    "RMON2-MIB::hlMatrixControlNlInserts": "1.3.6.1.2.1.16.15.1.1.4",
    "RMON2-MIB::hlMatrixControlNlDeletes": "1.3.6.1.2.1.16.15.1.1.5",
    "RMON2-MIB::hlMatrixControlNlMaxDesiredEntries": "1.3.6.1.2.1.16.15.1.1.6",
    "RMON2-MIB::hlMatrixControlAlDroppedFrames": "1.3.6.1.2.1.16.15.1.1.7",
    "RMON2-MIB::hlMatrixControlAlInserts": "1.3.6.1.2.1.16.15.1.1.8",
    "RMON2-MIB::hlMatrixControlAlDeletes": "1.3.6.1.2.1.16.15.1.1.9",
    "RMON2-MIB::hlMatrixControlAlMaxDesiredEntries": "1.3.6.1.2.1.16.15.1.1.10",
    "RMON2-MIB::hlMatrixControlOwner": "1.3.6.1.2.1.16.15.1.1.11",
    "RMON2-MIB::hlMatrixControlStatus": "1.3.6.1.2.1.16.15.1.1.12",
    "RMON2-MIB::nlMatrixSDTable": "1.3.6.1.2.1.16.15.2",
    "RMON2-MIB::nlMatrixSDEntry": "1.3.6.1.2.1.16.15.2.1",
    "RMON2-MIB::nlMatrixSDTimeMark": "1.3.6.1.2.1.16.15.2.1.1",
    "RMON2-MIB::nlMatrixSDSourceAddress": "1.3.6.1.2.1.16.15.2.1.2",
    "RMON2-MIB::nlMatrixSDDestAddress": "1.3.6.1.2.1.16.15.2.1.3",
    "RMON2-MIB::nlMatrixSDPkts": "1.3.6.1.2.1.16.15.2.1.4",
    "RMON2-MIB::nlMatrixSDOctets": "1.3.6.1.2.1.16.15.2.1.5",
    "RMON2-MIB::nlMatrixSDCreateTime": "1.3.6.1.2.1.16.15.2.1.6",
    "RMON2-MIB::nlMatrixDSTable": "1.3.6.1.2.1.16.15.3",
    "RMON2-MIB::nlMatrixDSEntry": "1.3.6.1.2.1.16.15.3.1",
    "RMON2-MIB::nlMatrixDSTimeMark": "1.3.6.1.2.1.16.15.3.1.1",
    "RMON2-MIB::nlMatrixDSSourceAddress": "1.3.6.1.2.1.16.15.3.1.2",
    "RMON2-MIB::nlMatrixDSDestAddress": "1.3.6.1.2.1.16.15.3.1.3",
    "RMON2-MIB::nlMatrixDSPkts": "1.3.6.1.2.1.16.15.3.1.4",
    "RMON2-MIB::nlMatrixDSOctets": "1.3.6.1.2.1.16.15.3.1.5",
    "RMON2-MIB::nlMatrixDSCreateTime": "1.3.6.1.2.1.16.15.3.1.6",
    "RMON2-MIB::nlMatrixTopNControlTable": "1.3.6.1.2.1.16.15.4",
    "RMON2-MIB::nlMatrixTopNControlEntry": "1.3.6.1.2.1.16.15.4.1",
    "RMON2-MIB::nlMatrixTopNControlIndex": "1.3.6.1.2.1.16.15.4.1.1",
    "RMON2-MIB::nlMatrixTopNControlMatrixIndex": "1.3.6.1.2.1.16.15.4.1.2",
    "RMON2-MIB::nlMatrixTopNControlRateBase": "1.3.6.1.2.1.16.15.4.1.3",
    "RMON2-MIB::nlMatrixTopNControlTimeRemaining": "1.3.6.1.2.1.16.15.4.1.4",
    "RMON2-MIB::nlMatrixTopNControlGeneratedReports": "1.3.6.1.2.1.16.15.4.1.5",
    "RMON2-MIB::nlMatrixTopNControlDuration": "1.3.6.1.2.1.16.15.4.1.6",
    "RMON2-MIB::nlMatrixTopNControlRequestedSize": "1.3.6.1.2.1.16.15.4.1.7",
    "RMON2-MIB::nlMatrixTopNControlGrantedSize": "1.3.6.1.2.1.16.15.4.1.8",
    "RMON2-MIB::nlMatrixTopNControlStartTime": "1.3.6.1.2.1.16.15.4.1.9",
    "RMON2-MIB::nlMatrixTopNControlOwner": "1.3.6.1.2.1.16.15.4.1.10",
    "RMON2-MIB::nlMatrixTopNControlStatus": "1.3.6.1.2.1.16.15.4.1.11",
    "RMON2-MIB::nlMatrixTopNTable": "1.3.6.1.2.1.16.15.5",
    "RMON2-MIB::nlMatrixTopNEntry": "1.3.6.1.2.1.16.15.5.1",
    "RMON2-MIB::nlMatrixTopNIndex": "1.3.6.1.2.1.16.15.5.1.1",
    "RMON2-MIB::nlMatrixTopNProtocolDirLocalIndex": "1.3.6.1.2.1.16.15.5.1.2",
    "RMON2-MIB::nlMatrixTopNSourceAddress": "1.3.6.1.2.1.16.15.5.1.3",
    "RMON2-MIB::nlMatrixTopNDestAddress": "1.3.6.1.2.1.16.15.5.1.4",
    "RMON2-MIB::nlMatrixTopNPktRate": "1.3.6.1.2.1.16.15.5.1.5",
    "RMON2-MIB::nlMatrixTopNReversePktRate": "1.3.6.1.2.1.16.15.5.1.6",
    "RMON2-MIB::nlMatrixTopNOctetRate": "1.3.6.1.2.1.16.15.5.1.7",
    "RMON2-MIB::nlMatrixTopNReverseOctetRate": "1.3.6.1.2.1.16.15.5.1.8",
    "RMON2-MIB::alHost": "1.3.6.1.2.1.16.16",
    "RMON2-MIB::alHostTable": "1.3.6.1.2.1.16.16.1",
    "RMON2-MIB::alHostEntry": "1.3.6.1.2.1.16.16.1.1",
    "RMON2-MIB::alHostTimeMark": "1.3.6.1.2.1.16.16.1.1.1",
    "RMON2-MIB::alHostInPkts": "1.3.6.1.2.1.16.16.1.1.2",
    "RMON2-MIB::alHostOutPkts": "1.3.6.1.2.1.16.16.1.1.3",
    "RMON2-MIB::alHostInOctets": "1.3.6.1.2.1.16.16.1.1.4",
    "RMON2-MIB::alHostOutOctets": "1.3.6.1.2.1.16.16.1.1.5",
    "RMON2-MIB::alHostCreateTime": "1.3.6.1.2.1.16.16.1.1.6",
    "RMON2-MIB::alMatrix": "1.3.6.1.2.1.16.17",
    "RMON2-MIB::alMatrixSDTable": "1.3.6.1.2.1.16.17.1",
    "RMON2-MIB::alMatrixSDEntry": "1.3.6.1.2.1.16.17.1.1",
    "RMON2-MIB::alMatrixSDTimeMark": "1.3.6.1.2.1.16.17.1.1.1",
    "RMON2-MIB::alMatrixSDPkts": "1.3.6.1.2.1.16.17.1.1.2",
    "RMON2-MIB::alMatrixSDOctets": "1.3.6.1.2.1.16.17.1.1.3",
    "RMON2-MIB::alMatrixSDCreateTime": "1.3.6.1.2.1.16.17.1.1.4",
    "RMON2-MIB::alMatrixDSTable": "1.3.6.1.2.1.16.17.2",
    "RMON2-MIB::alMatrixDSEntry": "1.3.6.1.2.1.16.17.2.1",
    "RMON2-MIB::alMatrixDSTimeMark": "1.3.6.1.2.1.16.17.2.1.1",
    "RMON2-MIB::alMatrixDSPkts": "1.3.6.1.2.1.16.17.2.1.2",
    "RMON2-MIB::alMatrixDSOctets": "1.3.6.1.2.1.16.17.2.1.3",
    "RMON2-MIB::alMatrixDSCreateTime": "1.3.6.1.2.1.16.17.2.1.4",
    "RMON2-MIB::alMatrixTopNControlTable": "1.3.6.1.2.1.16.17.3",
    "RMON2-MIB::alMatrixTopNControlEntry": "1.3.6.1.2.1.16.17.3.1",
    "RMON2-MIB::alMatrixTopNControlIndex": "1.3.6.1.2.1.16.17.3.1.1",
    "RMON2-MIB::alMatrixTopNControlMatrixIndex": "1.3.6.1.2.1.16.17.3.1.2",
    "RMON2-MIB::alMatrixTopNControlRateBase": "1.3.6.1.2.1.16.17.3.1.3",
    "RMON2-MIB::alMatrixTopNControlTimeRemaining": "1.3.6.1.2.1.16.17.3.1.4",
    "RMON2-MIB::alMatrixTopNControlGeneratedReports": "1.3.6.1.2.1.16.17.3.1.5",
    "RMON2-MIB::alMatrixTopNControlDuration": "1.3.6.1.2.1.16.17.3.1.6",
    "RMON2-MIB::alMatrixTopNControlRequestedSize": "1.3.6.1.2.1.16.17.3.1.7",
    "RMON2-MIB::alMatrixTopNControlGrantedSize": "1.3.6.1.2.1.16.17.3.1.8",
    "RMON2-MIB::alMatrixTopNControlStartTime": "1.3.6.1.2.1.16.17.3.1.9",
    "RMON2-MIB::alMatrixTopNControlOwner": "1.3.6.1.2.1.16.17.3.1.10",
    "RMON2-MIB::alMatrixTopNControlStatus": "1.3.6.1.2.1.16.17.3.1.11",
    "RMON2-MIB::alMatrixTopNTable": "1.3.6.1.2.1.16.17.4",
    "RMON2-MIB::alMatrixTopNEntry": "1.3.6.1.2.1.16.17.4.1",
    "RMON2-MIB::alMatrixTopNIndex": "1.3.6.1.2.1.16.17.4.1.1",
    "RMON2-MIB::alMatrixTopNProtocolDirLocalIndex": "1.3.6.1.2.1.16.17.4.1.2",
    "RMON2-MIB::alMatrixTopNSourceAddress": "1.3.6.1.2.1.16.17.4.1.3",
    "RMON2-MIB::alMatrixTopNDestAddress": "1.3.6.1.2.1.16.17.4.1.4",
    "RMON2-MIB::alMatrixTopNAppProtocolDirLocalIndex": "1.3.6.1.2.1.16.17.4.1.5",
    "RMON2-MIB::alMatrixTopNPktRate": "1.3.6.1.2.1.16.17.4.1.6",
    "RMON2-MIB::alMatrixTopNReversePktRate": "1.3.6.1.2.1.16.17.4.1.7",
    "RMON2-MIB::alMatrixTopNOctetRate": "1.3.6.1.2.1.16.17.4.1.8",
    "RMON2-MIB::alMatrixTopNReverseOctetRate": "1.3.6.1.2.1.16.17.4.1.9",
    "RMON2-MIB::usrHistory": "1.3.6.1.2.1.16.18",
    "RMON2-MIB::usrHistoryControlTable": "1.3.6.1.2.1.16.18.1",
    "RMON2-MIB::usrHistoryControlEntry": "1.3.6.1.2.1.16.18.1.1",
    "RMON2-MIB::usrHistoryControlIndex": "1.3.6.1.2.1.16.18.1.1.1",
    "RMON2-MIB::usrHistoryControlObjects": "1.3.6.1.2.1.16.18.1.1.2",
    "RMON2-MIB::usrHistoryControlBucketsRequested": "1.3.6.1.2.1.16.18.1.1.3",
    "RMON2-MIB::usrHistoryControlBucketsGranted": "1.3.6.1.2.1.16.18.1.1.4",
    "RMON2-MIB::usrHistoryControlInterval": "1.3.6.1.2.1.16.18.1.1.5",
    "RMON2-MIB::usrHistoryControlOwner": "1.3.6.1.2.1.16.18.1.1.6",
    "RMON2-MIB::usrHistoryControlStatus": "1.3.6.1.2.1.16.18.1.1.7",
    "RMON2-MIB::usrHistoryObjectTable": "1.3.6.1.2.1.16.18.2",
    "RMON2-MIB::usrHistoryObjectEntry": "1.3.6.1.2.1.16.18.2.1",
    "RMON2-MIB::usrHistoryObjectIndex": "1.3.6.1.2.1.16.18.2.1.1",
    "RMON2-MIB::usrHistoryObjectVariable": "1.3.6.1.2.1.16.18.2.1.2",
    "RMON2-MIB::usrHistoryObjectSampleType": "1.3.6.1.2.1.16.18.2.1.3",
    "RMON2-MIB::usrHistoryTable": "1.3.6.1.2.1.16.18.3",
    "RMON2-MIB::usrHistoryEntry": "1.3.6.1.2.1.16.18.3.1",
    "RMON2-MIB::usrHistorySampleIndex": "1.3.6.1.2.1.16.18.3.1.1",
    "RMON2-MIB::usrHistoryIntervalStart": "1.3.6.1.2.1.16.18.3.1.2",
    "RMON2-MIB::usrHistoryIntervalEnd": "1.3.6.1.2.1.16.18.3.1.3",
    "RMON2-MIB::usrHistoryAbsValue": "1.3.6.1.2.1.16.18.3.1.4",
    "RMON2-MIB::usrHistoryValStatus": "1.3.6.1.2.1.16.18.3.1.5",
    "RMON2-MIB::probeConfig": "1.3.6.1.2.1.16.19",
    "RMON2-MIB::probeCapabilities": "1.3.6.1.2.1.16.19.1",
    "RMON2-MIB::probeSoftwareRev": "1.3.6.1.2.1.16.19.2",
    "RMON2-MIB::probeHardwareRev": "1.3.6.1.2.1.16.19.3",
    "RMON2-MIB::probeDateTime": "1.3.6.1.2.1.16.19.4",
    "RMON2-MIB::probeResetControl": "1.3.6.1.2.1.16.19.5",
    "RMON2-MIB::probeDownloadFile": "1.3.6.1.2.1.16.19.6",
    "RMON2-MIB::probeDownloadTFTPServer": "1.3.6.1.2.1.16.19.7",
    "RMON2-MIB::probeDownloadAction": "1.3.6.1.2.1.16.19.8",
    "RMON2-MIB::probeDownloadStatus": "1.3.6.1.2.1.16.19.9",
    "RMON2-MIB::serialConfigTable": "1.3.6.1.2.1.16.19.10",
    "RMON2-MIB::serialConfigEntry": "1.3.6.1.2.1.16.19.10.1",
    "RMON2-MIB::serialMode": "1.3.6.1.2.1.16.19.10.1.1",
    "RMON2-MIB::serialProtocol": "1.3.6.1.2.1.16.19.10.1.2",
    "RMON2-MIB::serialTimeout": "1.3.6.1.2.1.16.19.10.1.3",
    "RMON2-MIB::serialModemInitString": "1.3.6.1.2.1.16.19.10.1.4",
    "RMON2-MIB::serialModemHangUpString": "1.3.6.1.2.1.16.19.10.1.5",
    "RMON2-MIB::serialModemConnectResp": "1.3.6.1.2.1.16.19.10.1.6",
    "RMON2-MIB::serialModemNoConnectResp": "1.3.6.1.2.1.16.19.10.1.7",
    "RMON2-MIB::serialDialoutTimeout": "1.3.6.1.2.1.16.19.10.1.8",
    "RMON2-MIB::serialStatus": "1.3.6.1.2.1.16.19.10.1.9",
    "RMON2-MIB::netConfigTable": "1.3.6.1.2.1.16.19.11",
    "RMON2-MIB::netConfigEntry": "1.3.6.1.2.1.16.19.11.1",
    "RMON2-MIB::netConfigIPAddress": "1.3.6.1.2.1.16.19.11.1.1",
    "RMON2-MIB::netConfigSubnetMask": "1.3.6.1.2.1.16.19.11.1.2",
    "RMON2-MIB::netConfigStatus": "1.3.6.1.2.1.16.19.11.1.3",
    "RMON2-MIB::netDefaultGateway": "1.3.6.1.2.1.16.19.12",
    "RMON2-MIB::trapDestTable": "1.3.6.1.2.1.16.19.13",
    "RMON2-MIB::trapDestEntry": "1.3.6.1.2.1.16.19.13.1",
    "RMON2-MIB::trapDestIndex": "1.3.6.1.2.1.16.19.13.1.1",
    "RMON2-MIB::trapDestCommunity": "1.3.6.1.2.1.16.19.13.1.2",
    "RMON2-MIB::trapDestProtocol": "1.3.6.1.2.1.16.19.13.1.3",
    "RMON2-MIB::trapDestAddress": "1.3.6.1.2.1.16.19.13.1.4",
    "RMON2-MIB::trapDestOwner": "1.3.6.1.2.1.16.19.13.1.5",
    "RMON2-MIB::trapDestStatus": "1.3.6.1.2.1.16.19.13.1.6",
    "RMON2-MIB::serialConnectionTable": "1.3.6.1.2.1.16.19.14",
    "RMON2-MIB::serialConnectionEntry": "1.3.6.1.2.1.16.19.14.1",
    "RMON2-MIB::serialConnectIndex": "1.3.6.1.2.1.16.19.14.1.1",
    "RMON2-MIB::serialConnectDestIpAddress": "1.3.6.1.2.1.16.19.14.1.2",
    "RMON2-MIB::serialConnectType": "1.3.6.1.2.1.16.19.14.1.3",
    "RMON2-MIB::serialConnectDialString": "1.3.6.1.2.1.16.19.14.1.4",
    "RMON2-MIB::serialConnectSwitchConnectSeq": "1.3.6.1.2.1.16.19.14.1.5",
    "RMON2-MIB::serialConnectSwitchDisconnectSeq": "1.3.6.1.2.1.16.19.14.1.6",
    "RMON2-MIB::serialConnectSwitchResetSeq": "1.3.6.1.2.1.16.19.14.1.7",
    "RMON2-MIB::serialConnectOwner": "1.3.6.1.2.1.16.19.14.1.8",
    "RMON2-MIB::serialConnectStatus": "1.3.6.1.2.1.16.19.14.1.9",
    "RMON2-MIB::rmon2MIBCompliances": "1.3.6.1.2.1.16.20.1",
    "RMON2-MIB::rmon2MIBGroups": "1.3.6.1.2.1.16.20.2"
}
