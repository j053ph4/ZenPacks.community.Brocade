
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }

    ZC.connUnitPortPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'connUnitPort',
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
                        "name": "connUnitPortModuleType"
                    }, 
                    {
                        "name": "connUnitPortTransmitterType"
                    }, 
                    {
                        "name": "connUnitPortType"
                    }, 
                    {
                        "name": "getCunitLink"
                    }, 
                    {
                        "name": "getPortHwState"
                    }, 
                    {
                        "name": "getPortState"
                    }, 
                    {
                        "name": "getPortStatus"
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
                        "header": "connUnitPortModuleType", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "connUnitPortModuleType", 
                        "dataIndex": "connUnitPortModuleType"
                    }, 
                    {
                        "header": "connUnitPortTransmitterType", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "connUnitPortTransmitterType", 
                        "dataIndex": "connUnitPortTransmitterType"
                    }, 
                    {
                        "header": "connUnitPortType", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "connUnitPortType", 
                        "dataIndex": "connUnitPortType"
                    }, 
                    {
                        "header": "Connectivity Unit", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getCunitLink", 
                        "dataIndex": "getCunitLink"
                    }, 
                    {
                        "header": "Port HW State", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getPortHwState", 
                        "dataIndex": "getPortHwState"
                    }, 
                    {
                        "header": "Port State", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getPortState", 
                        "dataIndex": "getPortState"
                    }, 
                    {
                        "header": "Port Status", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getPortStatus", 
                        "dataIndex": "getPortStatus"
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
            ZC.connUnitPortPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('connUnitPortPanel', ZC.connUnitPortPanel);
    ZC.registerName('connUnitPort', _t('Connectivity Unit Port'), _t('Connectivity Unit Ports'));
    
    })();

