from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.Brocade.Definition import *

__doc__ = """swFCportMap

swFCportMap detects Brocade Fiber Channel Ports.

"""


swFCPortTypeMap = {1: 'stitch', 2: 'flannel', 7: 'other'}
swFCPortBrcdTypeMap = { 1: 'unknown', 2: 'other', 3: 'fl-port', 4: 'f-port', 5: 'e-port', 6:'g-port', 7: 'ex-port'}
swFCPortOpStatusMap = { 0: 'unknown', 1: 'online', 2: 'offline', 3: 'testing', 4:'faulty'}

class swFCportMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(swFCportDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpEntryName = 'swFCPortEntry'
    snmpEntryOID = '.1.3.6.1.4.1.1588.2.1.1.1.6.2.1'
    snmpIndexName = 'swFCPortIndex'
    snmpTitleName = 'swFCPortName'
    
    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.1': snmpIndexName,
            '.2': 'swFCPortType',
            '.3': 'swFCPortPhyState',
            '.4': 'swFCPortOpStatus',
            '.5': 'swFCPortAdmStatus',
            '.6': 'swFCPortLinkState',
            '.36': snmpTitleName,
            '.37': 'swFCPortSpecifier',
            '.39': 'swFCPortBrcdType',
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
            om = self.objectMap(trunk)
            name = "%s_%s" % (trunk[self.snmpTitleName], trunk[self.snmpIndexName])
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = getattr(om, self.snmpIndexName)
            om.swFCPortBrcdType = swFCPortBrcdTypeMap[int(trunk['swFCPortBrcdType'])]
            try:
                om.swFCPortType = swFCPortTypeMap[int(trunk['swFCPortType'])]
            except:
                om.swFCPortType = 'other'
            #if swFCPortOpStatusMap[int(trunk['swFCPortLinkState'])] == 'offline':
            #    om.monitor = False
            rm.append(om)
        maps.append(rm)
        return maps
