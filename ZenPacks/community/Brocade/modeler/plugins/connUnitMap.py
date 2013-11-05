from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.Brocade.Definition import *

class connUnitMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(connUnitDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpEntryName = 'connUnitEntry'
    snmpEntryOID = '.1.3.6.1.3.94.1.6.1'
    snmpIndexName = 'connUnitId'
    snmpTitleName = 'connUnitName'

    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.1': snmpIndexName,
            '.2': 'connUnitGlobalId',
            '.3': 'connUnitType',
            '.4': 'connUnitNumports',
            '.7': 'connUnitProduct',
            '.8': 'connUnitSn',
            '.10': 'connUnitUrl',
            '.11': 'connUnitDomainId',
            '.12': 'connUnitProxyMaster',
            '.13': 'connUnitPrincipal',
            '.14': 'connUnitNumSensors',
            '.15': 'connUnitStatusChangeTime',
            '.16': 'connUnitConfigurationChangeTime',
            '.17': 'connUnitNumRevs',
            '.18': 'connUnitNumZones',
            '.19': 'connUnitModuleId',
            '.20': 'connUnitName',
            '.21': 'connUnitInfo',
            '.22': 'connUnitControl',
            '.23': 'connUnitContact',
            '.24': 'connUnitLocation',
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
            om.snmpindex = self.dotify(getattr(om, self.snmpIndexName))
            om.connUnitId = self.dotify(om.connUnitId)
            om.connUnitDomainId = self.dotify(om.connUnitDomainId)
            om.connUnitModuleId = self.dotify(om.connUnitModuleId)
            om.connUnitGlobalId = self.dotify(om.connUnitGlobalId)
            om.connUnitModuleId = self.dotify(om.connUnitModuleId)
            rm.append(om)
            log.debug("om: %s" % om)
        maps.append(rm)
        return maps
