
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
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
                        "sortable": "true", 
                        "width": 120, 
                        "header": "A", 
                        "renderer": "pass_link", 
                        "id": "getswFCPortAdmStatus", 
                        "dataIndex": "getswFCPortAdmStatus"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Link State", 
                        "renderer": "pass_link", 
                        "id": "getswFCPortLinkState", 
                        "dataIndex": "getswFCPortLinkState"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "O", 
                        "renderer": "pass_link", 
                        "id": "getswFCPortOpStatus", 
                        "dataIndex": "getswFCPortOpStatus"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Phys State", 
                        "renderer": "pass_link", 
                        "id": "getswFCPortPhyState", 
                        "dataIndex": "getswFCPortPhyState"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "swFCPortBrcdType", 
                        "renderer": "pass_link", 
                        "id": "swFCPortBrcdType", 
                        "dataIndex": "swFCPortBrcdType"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "swFCPortSpecifier", 
                        "renderer": "pass_link", 
                        "id": "swFCPortSpecifier", 
                        "dataIndex": "swFCPortSpecifier"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "swFCPortType", 
                        "renderer": "pass_link", 
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

