from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.Brocade.Definition import *

sensorTypeMap = {'temperature': 1, 'fan': 2, 'power-supply': 3}

class swTempSensorMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(swTempSensorDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpEntryName = 'swSensorEntry'
    snmpEntryOID = '.1.3.6.1.4.1.1588.2.1.1.1.1.22.1'
    snmpIndexName = 'swSensorIndex'
    snmpTitleName = 'swSensorInfo'
    
    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.1': snmpIndexName,
            '.2': 'swSensorType',
            '.5': snmpTitleName,
            }),
        )
    
    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get(self.snmpEntryName)
        snmpindex = 1
        for trunk in trunktable.values():
            if trunk['swSensorType'] == sensorTypeMap['temperature']:  
                om = self.objectMap(trunk)
                name = "%s" % getattr(om, self.snmpTitleName)
                om.id = self.prepId(name)
                om.title = name
                om.snmpindex = getattr(om, self.snmpIndexName)
                rm.append(om)
        maps.append(rm)
        return maps

