//---------------------------------------------------------------------
// NOC.core.RepoPreview
//---------------------------------------------------------------------
// Copyright (C) 2007-2012 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.core.RepoPreview");

Ext.define("NOC.core.RepoPreview", {
    extend: "Ext.Window",
    autoShow: true,
    closable: true,
    maximizable: true,
    modal: true,
    msg: "",
    layout: "fit",
    padding: 4,
    width: 800,
    height: 600,
    syntax: null,

    initComponent: function() {
        var me = this;

        me.revCombo = Ext.create("Ext.form.ComboBox", {
            fieldLabel: "Version",
            labelWidth: 45,
            width: 300,
            queryMode: "local",
            displayField: "ts",
            valueField: "id",
            store: Ext.create("Ext.data.Store", {
                fields: [
                    {
                        name: "id",
                        type: "auto"
                    },
                    {
                        name: "ts",
                        type: "date"
                    }
                ],
                data: []
            }),
            listeners: {
                scope: me,
                select: me.onSelectRev
            }
        });

        me.diffCombo = Ext.create("Ext.form.ComboBox", {
            fieldLabel: "Compare with",
            disabled: true,
            labelWidth: 75,
            width: 300,
            queryMode: "local",
            displayField: "ts",
            valueField: "id",
            store: Ext.create("Ext.data.Store", {
                fields: [
                    {
                        name: "id",
                        type: "auto"
                    },
                    {
                        name: "ts",
                        type: "date"
                    }
                ],
                data: []
            }),
            listeners: {
                scope: me,
                select: me.onSelectDiff
            }
        });

        Ext.apply(me, {
            dockedItems: [{
                xtype: "toolbar",
                dock: "top",
                items: [
                    me.revCombo,
                    me.diffCombo
                ]
            }],
            items: [{
                xtype: "container",
                autoScroll: true
            }]
        });
        me.callParent();
        me.requestText();
        me.requestRevisions();
    },
    //
    requestText: function() {
        var me = this;
        Ext.Ajax.request({
            url: me.rootUrl,
            method: "GET",
            scope: me,
            success: function(response) {
                me.renderText(Ext.decode(response.responseText));
            },
            failure: function() {
                NOC.error("Failed to get text");
            }
        });
    },
    //
    requestRevisions: function() {
        var me = this;
        Ext.Ajax.request({
            url: me.rootUrl + "revisions/",
            method: "GET",
            scope: me,
            success: function(response) {
                var data = Ext.decode(response.responseText);
                me.revCombo.store.loadData(data);
                me.diffCombo.store.loadData(data);
            },
            failure: function() {
                NOC.error("Failed to get revisions");
            }
        });
    },
    //
    requestRevision: function(rev) {
        var me = this;
        Ext.Ajax.request({
            url: me.rootUrl + rev + "/",
            method: "GET",
            scope: me,
            success: function(response) {
                me.renderText(Ext.decode(response.responseText));
            },
            failure: function() {
                NOC.error("Failed to get text");
            }
        });
    },
    //
    requestDiff: function(rev1, rev2) {
        var me = this;
        Ext.Ajax.request({
            url: me.rootUrl + rev1 + "/" + rev2 + "/",
            method: "GET",
            scope: me,
            success: function(response) {
                me.renderText(Ext.decode(response.responseText), "diff");
            },
            failure: function() {
                NOC.error("Failed to get diff");
            }
        });
    },
    //
    renderText: function(text, syntax) {
        var me = this;
        syntax = syntax || me.syntax;
        NOC.SyntaxHighlight.highlight(me.items.first(), text, syntax);
    },
    //
    onSelectRev: function(combo, records, eOpts) {
        var me = this;
        me.requestRevision(records[0].get("id"));
        me.diffCombo.setDisabled(false);
    },
    //
    onSelectDiff: function(combo, records, eOpts) {
        var me = this;
        me.requestDiff(
            me.revCombo.getValue(),
            me.diffCombo.getValue()
        );
    }
});
