from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "Brocade"
VERSION = Version(1, 0, 0)

def getMapValue(ob, datapoint, map):
    ''' attempt to map number to data dict'''
    try:
        value = int(ob.getRRDValue(datapoint))
        return map[value]
    except:
        return 'unknown'
    
def getSensorState(ob): return ob.getMapValue('swSensorStatus_swSensorStatus', ob.sensorStatusMap)

sensorStatusMap = { 1: 'unknown', 2: 'faulty', 3: 'below-min',  4: 'nominal', 5: 'above-max', 6: 'absent', }

DATA = {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'swTempSensor',
        'componentData' : {
                          'singular': 'Temp Sensor',
                          'plural': 'Temp Sensors',
                          'properties': { 
                                        'swSensorInfo' : addProperty('swSensorInfo'),
                                        'getSensorState' : getReferredMethod('Sensor State', 'getSensorState'),
                                        },
                          },
        'componentAttributes' : {'sensorStatusMap': sensorStatusMap },
        'componentMethods' : [getMapValue, getSensorState]
        }

swTempSensorDefinition = type('swTempSensorDefinition', (BasicDefinition,), DATA)

DATA2 = DATA.copy()
DATA2['component'] = 'swFanSensor'
DATA2['componentData']['singular'] = 'Fan Sensor'
DATA2['componentData']['plural'] = 'Fan Sensors' 

swFanSensorDefinition = type('swFanSensorDefinition', (BasicDefinition,), DATA2)

DATA2 = DATA.copy()
DATA2['component'] = 'swPowerSensor'
DATA2['componentData']['singular'] = 'Power Supply Sensor'
DATA2['componentData']['plural'] = 'Power Supply Sensors'

swPowerSensorDefinition = type('swPowerSensorDefinition', (BasicDefinition,), DATA2)


def getswFCPortPhyState(ob):  return ob.getMapValue('swFCPortPhyState_swFCPortPhyState', ob.swFCPortPhyStateMap)
def getswFCPortOpStatus(ob):  return ob.getMapValue('swFCPortOpStatus_swFCPortOpStatus', ob.swFCPortOpStatusMap)
def getswFCPortAdmStatus(ob):  return ob.getMapValue('swFCPortAdmStatus_swFCPortAdmStatus', ob.swFCPortAdmStatusMap)
def getswFCPortLinkState(ob):  return ob.getMapValue('swFCPortLinkState_swFCPortLinkState', ob.swFCPortLinkStateMap)

swFCPortPhyStateMap = { 1: 'noCard', 2: 'noTransceiver', 3: 'laserFault', 4: 'noLight', 5: 'noSync', 6: 'inSync', 7: 'portFault', 8: 'diagFault', 9: 'lockRef', 255: 'unknown'}
swFCPortOpStatusMap = { 0: 'unknown', 1: 'online', 2: 'offline', 3: 'testing', 4:'faulty'}
swFCPortAdmStatusMap = { 1: 'online', 2: 'offline', 3: 'testing', 4:'faulty'}
swFCPortLinkStateMap = { 1: 'enabled', 2: 'disabled', 3: 'loopback'}
 
DATA = {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'swFCport',
        'componentData' : {
                          'singular': 'Fiber Channel Port',
                          'plural': 'Fiber Channel Ports',
                          'displayed': 'swFCPortName',
                          'primaryKey': 'swFCPortName',
                          'properties': { 
                                        'swFCPortType' : addProperty('swFCPortType', optional=False),
                                        'swFCPortName': addProperty('swFCPortName', 'Basic'),
                                        'swFCPortSpecifier': addProperty('swFCPortSpecifier', 'Basic', optional=False),
                                        'swFCPortBrcdType': addProperty('swFCPortBrcdType', 'Basic', optional=False),
                                        'getswFCPortPhyState' : getReferredMethod('Phys State', 'getswFCPortPhyState'),
                                        'getswFCPortOpStatus' : getReferredMethod('O', 'getswFCPortOpStatus'),
                                        'getswFCPortAdmStatus' : getReferredMethod('A', 'getswFCPortAdmStatus'),
                                        'getswFCPortLinkState' : getReferredMethod('Link State', 'getswFCPortLinkState'),

                                        },
                          },
        'componentAttributes' : { 'swFCPortPhyStateMap': swFCPortPhyStateMap,
                                  'swFCPortOpStatusMap': swFCPortOpStatusMap,
                                  'swFCPortAdmStatusMap': swFCPortAdmStatusMap, 
                                  'swFCPortLinkStateMap': swFCPortLinkStateMap
                                },
        'componentMethods' : [getMapValue, getswFCPortPhyState, getswFCPortOpStatus, getswFCPortAdmStatus, getswFCPortLinkState],
        }

swFCportDefinition = type('swFCportDefinition', (BasicDefinition,), DATA)

def getUnitState(ob):  return ob.getMapValue('connUnitState_connUnitState', ob.connUnitStateMap) 
def getUnitStatus(ob):  return ob.getMapValue('connUnitStatus_connUnitStatus', ob.connUnitStatusMap)
DATA = {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'connUnit',
        'componentData' : {
                          'singular': 'Connectivity Unit',
                          'plural': 'Connectivity Units',
                          'properties': { 
                                        'connUnitId' : addProperty('connUnitId'),
                                        'connUnitGlobalId' : addProperty('connUnitGlobalId'),
                                        'connUnitType' : addProperty('connUnitType'),
                                        'connUnitNumports' : addProperty('connUnitNumports'),
                                        'connUnitProduct' : addProperty('connUnitProduct'),
                                        'connUnitSn' : addProperty('connUnitSn'),
                                        'connUnitUrl': addProperty('connUnitUrl'),
                                        'connUnitDomainId' : addProperty('connUnitDomainId'),
                                        'connUnitProxyMaster' : addProperty('connUnitProxyMaster'),
                                        'connUnitModuleId' : addProperty('connUnitModuleId'),
                                        'connUnitName' : addProperty('connUnitName'),
                                        'connUnitInfo' : addProperty('connUnitInfo'),
                                        'connUnitControl' : addProperty('connUnitControl'),
                                        'connUnitContact' : addProperty('connUnitContact'),
                                        'getUnitState' : getReferredMethod('Unit State', 'getUnitState'),
                                        'getUnitStatus' : getReferredMethod('Unit Status', 'getUnitStatus'),
                                        },
                          },
        
        'componentAttributes' : {
                                 'connUnitStateMap': { 1: 'unknown', 2: 'online', 3: 'offline'}, 
                                 'connUnitStatusMap': { 1: 'unknown', 2: 'unused', 3: 'ready', 4: 'warning', 5: 'failed'}, 
                                 },
        'componentMethods' : [getMapValue, getUnitState, getUnitStatus],
        }

connUnitDefinition = type('connUnitDefinition', (BasicDefinition,), DATA)

def getPortState(ob):  return ob.getMapValue('connUnitPortState_connUnitPortState', ob.connUnitPortStateMap) 
def getPortStatus(ob):  return ob.getMapValue('connUnitPortStatus_connUnitPortStatus', ob.connUnitPortStatusMap)
def getPortHwState(ob):  return ob.getMapValue('connUnitPortHWState_connUnitPortHWState', ob.connUnitPortHWStateMap)

connUnitPortStateMap = { 1: 'unknown', 2: 'online', 3: 'offline', 4: 'bypassed', 5: 'diagnostics', }
connUnitPortStatusMap = { 1: 'unknown', 2: 'unused', 3: 'ready', 4: 'warning', 5: 'failure', 6: 'notparticipating', 7: 'initializing', 8: 'bypass', 9: 'ols' }
connUnitPortHWStateMap = { 1: 'unknown', 2: 'failed', 3: 'bypassed', 4: 'active', 5: 'loopback', 6: 'txfault', 7: 'noMedia', 8: 'linkDown',}

DATA = {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'connUnitPort',
        'componentData' : {
                          'singular': 'Connectivity Unit Port',
                          'plural': 'Connectivity Unit Ports',
                          'properties': { 
                                        'connUnitPortUnitId' : addProperty('connUnitPortUnitId'),
                                        'connUnitPortIndex' : addProperty('connUnitPortIndex'),
                                        'connUnitPortName' : addProperty('connUnitPortName'),
                                        'connUnitPortType' : addProperty('connUnitPortType', optional=False, order=2),
                                        'connUnitPortTransmitterType' : addProperty('connUnitPortTransmitterType', optional=False, order=3),
                                        'connUnitPortModuleType' : addProperty('connUnitPortModuleType', optional=False, order=4),
                                        'connUnitPortFCId' : addProperty('connUnitPortFCId'),
                                        'connUnitPortSn' : addProperty('connUnitPortSn'),
                                        'connUnitPortSpeed' : addProperty('connUnitPortSpeed'),
                                        'connUnitPortPhysicalNumber' : addProperty('connUnitPortPhysicalNumber'),
                                        'getPortState' : getReferredMethod('Port State', 'getPortState'),
                                        'getPortStatus' : getReferredMethod('Port Status', 'getPortStatus'),
                                        'getPortHwState' : getReferredMethod('Port HW State', 'getPortHwState'),
                                        },
                          },
        
        'componentAttributes' : {
                                 'connUnitPortStateMap': connUnitPortStateMap, 
                                 'connUnitPortStatusMap': connUnitPortStatusMap, 
                                 'connUnitPortHWStateMap': connUnitPortHWStateMap
                                 },
        'componentMethods' : [getMapValue, getPortState, getPortStatus, getPortHwState],
        }

connUnitPortDefinition = type('connUnitPortDefinition', (BasicDefinition,), DATA)

addDefinitionSelfComponentRelation(connUnitPortDefinition, 
                          'cunitports',  ToMany, 'ZenPacks.community.Brocade.connUnitPort', 'connUnitPortUnitId',
                          'cunit', ToOne, 'ZenPacks.community.Brocade.connUnit','connUnitGlobalId',
                          'Connectivity Unit', 'id')


DATA = {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'connUnitLink',
        'componentData' : {
                          'singular': 'Connectivity Unit Link',
                          'plural': 'Connectivity Units Links',
                          'properties': { 
                                        'connUnitLinkUnitId' : addProperty('connUnitLinkUnitId'),
                                        'connUnitLinkIndex' : addProperty('connUnitLinkIndex'),
                                        'connUnitLinkNodeIdX' : addProperty('connUnitLinkNodeIdX'),
                                        'connUnitLinkPortNumberX' : addProperty('connUnitLinkPortNumberX'),
                                        'connUnitLinkPortWwnX' : addProperty('connUnitLinkPortWwnX'),
                                        'connUnitLinkNodeIdY' : addProperty('connUnitLinkNodeIdY'),
                                        'connUnitLinkPortWwnY' : addProperty('connUnitLinkPortWwnY'),
                                        'connUnitLinkPortNumberY' : addProperty('connUnitLinkPortNumberY'),
                                        'connUnitLinkAgentAddressY' : addProperty('connUnitLinkAgentAddressY'),
                                        'connUnitLinkAgentAddressTypeY' : addProperty('connUnitLinkAgentAddressTypeY'),
                                        'connUnitLinkAgentPortY' : addProperty('connUnitLinkAgentPortY'),
                                        'connUnitLinkUnitTypeY' : addProperty('connUnitLinkUnitTypeY'),
                                        'connUnitLinkConnIdY' : addProperty('connUnitLinkConnIdY'),
                                        'connUnitLinkCurrIndex' : addProperty('connUnitLinkCurrIndex'), 
                                        },
                          },

        'componentMethods' : [],
        }

connUnitLinkDefinition = type('connUnitLinkDefinition', (BasicDefinition,), DATA)

addDefinitionDeviceRelation(connUnitLinkDefinition,
                          'cunitlinks', ToMany, 'ZenPacks.community.Brocade.connUnitLink','connUnitLinkAgentAddressY',
                          'cunitdevice',  ToOne, 'Products.ZenModel.Device', 'manageIp',
                          "To Device")

addDefinitionAnyComponentRelation(connUnitLinkDefinition,
                          'tolinks', ToMany, 'ZenPacks.community.Brocade.connUnitLink','connUnitLinkNodeIdY',
                          'tounit',  ToOne, 'ZenPacks.community.Brocade.connUnit', 'connUnitGlobalId',
                          "To Unit", 'id')

addDefinitionAnyComponentRelation(connUnitLinkDefinition,
                            'fromlinks', ToMany, 'ZenPacks.community.Brocade.connUnitLink','connUnitLinkNodeIdX',
                            'fromunit',  ToOne, 'ZenPacks.community.Brocade.connUnit', 'connUnitGlobalId',
                            'From Unit', 'id')
