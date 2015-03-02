from ZenPacks.community.ConstructionKit.ClassHelper import *

def swFCportgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class swFCportInfo(ClassHelper.swFCportInfo):
    ''''''

def swFanSensorgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class swFanSensorInfo(ClassHelper.swFanSensorInfo):
    ''''''

def swPowerSensorgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class swPowerSensorInfo(ClassHelper.swPowerSensorInfo):
    ''''''

def swTempSensorgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class swTempSensorInfo(ClassHelper.swTempSensorInfo):
    ''''''


