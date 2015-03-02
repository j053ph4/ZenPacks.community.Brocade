from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "Brocade"
VERSION = Version(1, 1, 0)

def getMapValue(ob, datapoint, map):
    ''' attempt to map number to data dict'''
    try:
        value = int(ob.getRRDValue(datapoint))
        return map[value]
    except:
        return 'unknown'
    
def getSensorState(ob): return ob.getMapValue('swSensorStatus_swSensorStatus', ob.sensorStatusMap)

sensorStatusMap = { 1: 'unknown', 2: 'faulty', 3: 'below-min',  4: 'nominal', 5: 'above-max', 6: 'absent', }

def getData(component, singular, plural):
    return {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : component,
        'componentData' : {
                          'singular': singular,
                          'plural': plural,
                          'properties': { 
                                        'swSensorInfo' : addProperty('swSensorInfo'),
                                        'getSensorState' : getReferredMethod('Sensor State', 'getSensorState'),
                                        },
                          },
        'componentAttributes' : {'sensorStatusMap': sensorStatusMap },
        'componentMethods' : [getMapValue, getSensorState]
        }


swTempSensorDefinition = type('swTempSensorDefinition', (BasicDefinition,), getData('swTempSensor', 'Temp Sensor', 'Temp Sensors'))

swFanSensorDefinition = type('swFanSensorDefinition', (BasicDefinition,), getData('swFanSensor', 'Fan Sensor', 'Fan Sensors'))

swPowerSensorDefinition = type('swPowerSensorDefinition', (BasicDefinition,), getData('swPowerSensor', 'Power Supply Sensor', 'Power Supply Sensors'))


def getswFCPortPhyState(ob):  return ob.getMapValue('swFCPortPhyState_swFCPortPhyState', ob.swFCPortPhyStateMap)
def getswFCPortOpStatus(ob):  return ob.getMapValue('swFCPortOpStatus_swFCPortOpStatus', ob.swFCPortOpStatusMap)
def getswFCPortAdmStatus(ob):  return ob.getMapValue('swFCPortAdmStatus_swFCPortAdmStatus', ob.swFCPortAdmStatusMap)
def getswFCPortLinkState(ob):  return ob.getMapValue('swFCPortLinkState_swFCPortLinkState', ob.swFCPortLinkStateMap)

swFCPortPhyStateMap = { 1: 'noCard', 2: 'noTransceiver', 3: 'laserFault', 4: 'noLight', 5: 'noSync', 6: 'inSync', 7: 'portFault', 8: 'diagFault', 9: 'lockRef', 255: 'unknown'}
swFCPortOpStatusMap = { 0: 'unknown', 1: 'online', 2: 'offline', 3: 'testing', 4:'faulty'}
swFCPortAdmStatusMap = { 1: 'online', 2: 'offline', 3: 'testing', 4:'faulty'}
swFCPortLinkStateMap = { 1: 'enabled', 2: 'disabled', 3: 'loopback'}
 
swFCportDefinition = type('swFCportDefinition', (BasicDefinition,), {
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
)

