
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }

    ZC.swFCportPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'swFCport',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "getswFCPortAdmStatus"
                    }, 
                    {
                        "name": "getswFCPortLinkState"
                    }, 
                    {
                        "name": "getswFCPortOpStatus"
                    }, 
                    {
                        "name": "getswFCPortPhyState"
                    }, 
                    {
                        "name": "swFCPortBrcdType"
                    }, 
                    {
                        "name": "swFCPortSpecifier"
                    }, 
                    {
                        "name": "swFCPortType"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "header": "A", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getswFCPortAdmStatus", 
                        "dataIndex": "getswFCPortAdmStatus"
                    }, 
                    {
                        "header": "Link State", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getswFCPortLinkState", 
                        "dataIndex": "getswFCPortLinkState"
                    }, 
                    {
                        "header": "O", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getswFCPortOpStatus", 
                        "dataIndex": "getswFCPortOpStatus"
                    }, 
                    {
                        "header": "Phys State", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getswFCPortPhyState", 
                        "dataIndex": "getswFCPortPhyState"
                    }, 
                    {
                        "header": "swFCPortBrcdType", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "swFCPortBrcdType", 
                        "dataIndex": "swFCPortBrcdType"
                    }, 
                    {
                        "header": "swFCPortSpecifier", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "swFCPortSpecifier", 
                        "dataIndex": "swFCPortSpecifier"
                    }, 
                    {
                        "header": "swFCPortType", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "swFCPortType", 
                        "dataIndex": "swFCPortType"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.swFCportPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('swFCportPanel', ZC.swFCportPanel);
    ZC.registerName('swFCport', _t('Fiber Channel Port'), _t('Fiber Channel Ports'));
    
    })();

