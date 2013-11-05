from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.Brocade.Definition import *

class connUnitLinkMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(connUnitLinkDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpEntryName = 'connUnitLinkEntry'
    snmpEntryOID = '.1.3.6.1.3.94.1.12.1'
    snmpIndexName = 'connUnitLinkUnitId'
    snmpTitleName = 'connUnitLinkAgentAddressY'

    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.1': snmpIndexName,
            '.2': 'connUnitLinkIndex',
            '.3': 'connUnitLinkNodeIdX',
            '.4': 'connUnitLinkPortNumberX',
            '.5': 'connUnitLinkPortWwnX',
            '.6': 'connUnitLinkNodeIdY',
            '.7': 'connUnitLinkPortNumberY',
            '.8': 'connUnitLinkPortWwnY',
            '.9': 'connUnitLinkAgentAddressY',
            '.10': 'connUnitLinkAgentAddressTypeY',
            '.11': 'connUnitLinkAgentPortY',
            '.12': 'connUnitLinkUnitTypeY',
            '.13': 'connUnitLinkConnIdY',
            }),
        )
    
    def dotify(self, octets): return ".".join( [ '%d'%(ord(c)) for c in octets ] )
    
    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get(self.snmpEntryName)
        snmpindex = 1
        for trunk in trunktable.values():
            om = self.objectMap(trunk)
            name = "%s" % getattr(om, self.snmpTitleName)
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = "%s.%s" % (self.dotify(getattr(om, self.snmpIndexName)), getattr(om, 'connUnitLinkIndex'))
            om.connUnitLinkUnitId = self.dotify(getattr(om, 'connUnitLinkUnitId'))
            om.connUnitLinkNodeIdX = self.dotify(getattr(om, 'connUnitLinkNodeIdX'))
            om.connUnitLinkPortWwnX = self.dotify(getattr(om, 'connUnitLinkPortWwnX'))
            om.connUnitLinkNodeIdY = self.dotify(getattr(om, 'connUnitLinkNodeIdY'))
            om.connUnitLinkPortWwnY = self.dotify(getattr(om, 'connUnitLinkPortWwnY'))
            om.connUnitLinkConnIdY = self.dotify(getattr(om, 'connUnitLinkConnIdY'))
            #om.setCunit = om.connUnitLinkUnitId
            om.setCunitdevice = om.connUnitLinkAgentAddressY
            om.setFromunit = om.connUnitLinkNodeIdX
            om.setTounit = om.connUnitLinkNodeIdY
            rm.append(om)
            log.debug("om: %s" % om)
        maps.append(rm)
        return maps
