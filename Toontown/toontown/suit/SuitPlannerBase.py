from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.building import SuitBuildingGlobals
from toontown.dna.DNAParser import DNASuitPoint, DNAStorage, loadDNAFileAI

class SuitPlannerBase:
    notify = directNotify.newCategory('SuitPlannerBase')
    SuitHoodInfo = [[2100,
      5,
      15,
      0,
      5,
      20,
      3,
      (1,
       5,
       10,
       40,
       60,
       80),
      (25,
       25,
       25,
       25),
      (1, 2, 3),
      []],
     [2200,
      3,
      10,
      0,
      5,
      15,
      3,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       70,
       10,
       10),
      (1, 2, 3),
      []],
     [2300,
      3,
      10,
      0,
      5,
      15,
      3,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       10,
       40,
       40),
      (1, 2, 3),
      []],
     [1100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (90,
       10,
       0,
       0),
      (2, 3, 4),
      []],
     [1200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       90,
       10),
      (3,
       4,
       5,
       6),
      []],
     [1300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (40,
       40,
       10,
       10),
      (3,
       4,
       5,
       6),
      []],
     [3100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (90,
       10,
       0,
       0),
      (5, 6, 7),
      []],
     [3200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       20,
       30,
       40),
      (5, 6, 7),
      []],
     [3300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       85,
       5,
       5),
      (6, 7, 8, 9),
      []],
     [4100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       50,
       50),
      (2, 3, 4),
      []],
     [4200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       90,
       10),
      (3,
       4,
       5,
       6),
      []],
     [4300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (50,
       50,
       0,
       0),
      (3,
       4,
       5,
       6),
      []],
     [5100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       20,
       10,
       70),
      (2, 3, 4),
      []],
     [5200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       70,
       0,
       20),
      (3,
       4,
       5,
       6),
      []],
     [5300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       5,
       5,
       85),
      (3,
       4,
       5,
       6),
      []],
     [9100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (25,
       25,
       25,
       25),
      (6,
       7,
       8,
       9),
      []],
     [9200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       5,
       85,
       5),
      (6,
       7,
       8,
       9),
      []],
    [10000,
      3,
      15,
      0,
      5,
      15,
      3,
      (1,
       5,
       10,
       40,
       60,
       80),
      (100,
       0,
       0,
       0),
      (7, 8, 9, 10),
      []],
     [11000,
      3,
      15,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       0,
       100),
      (3, 4, 5, 6),
      []],
     [11200,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       0,
       100),
      (4, 5, 6),
      []],
     [12000,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       100,
       0),
      (6, 7, 8, 9),
      []],
     [13000,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       100,
       0,
       0),
      (7, 8, 9),
      []]]
    SUIT_HOOD_INFO_ZONE = 0
    SUIT_HOOD_INFO_MIN = 1
    SUIT_HOOD_INFO_MAX = 2
    SUIT_HOOD_INFO_BMIN = 3
    SUIT_HOOD_INFO_BMAX = 4
    SUIT_HOOD_INFO_BWEIGHT = 5
    SUIT_HOOD_INFO_SMAX = 6
    SUIT_HOOD_INFO_JCHANCE = 7
    SUIT_HOOD_INFO_TRACK = 8
    SUIT_HOOD_INFO_LVL = 9
    SUIT_HOOD_INFO_HEIGHTS = 10
    TOTAL_BWEIGHT = 0
    TOTAL_BWEIGHT_PER_TRACK = [0,
     0,
     0,
     0]
    TOTAL_BWEIGHT_PER_HEIGHT = [0,
     0,
     0,
     0,
     0]
    for currHoodInfo in SuitHoodInfo:
        weight = currHoodInfo[SUIT_HOOD_INFO_BWEIGHT]
        tracks = currHoodInfo[SUIT_HOOD_INFO_TRACK]
        levels = currHoodInfo[SUIT_HOOD_INFO_LVL]
        heights = [0,
         0,
         0,
         0,
         0]
        for level in levels:
            minFloors, maxFloors = SuitBuildingGlobals.SuitBuildingInfo[level - 1][0]
            for i in xrange(minFloors - 1, maxFloors):
                heights[i] += 1

        currHoodInfo[SUIT_HOOD_INFO_HEIGHTS] = heights
        TOTAL_BWEIGHT += weight
        TOTAL_BWEIGHT_PER_TRACK[0] += weight * tracks[0]
        TOTAL_BWEIGHT_PER_TRACK[1] += weight * tracks[1]
        TOTAL_BWEIGHT_PER_TRACK[2] += weight * tracks[2]
        TOTAL_BWEIGHT_PER_TRACK[3] += weight * tracks[3]
        TOTAL_BWEIGHT_PER_HEIGHT[0] += weight * heights[0]
        TOTAL_BWEIGHT_PER_HEIGHT[1] += weight * heights[1]
        TOTAL_BWEIGHT_PER_HEIGHT[2] += weight * heights[2]
        TOTAL_BWEIGHT_PER_HEIGHT[3] += weight * heights[3]
        TOTAL_BWEIGHT_PER_HEIGHT[4] += weight * heights[4]

    def __init__(self):
        self.suitWalkSpeed = ToontownGlobals.SuitWalkSpeed
        self.dnaStore = None
        self.pointIndexes = {}
        return

    def setupDNA(self):
        if self.dnaStore:
            return None
        self.dnaStore = DNAStorage()
        dnaFileName = self.genDNAFileName()
        loadDNAFileAI(self.dnaStore, dnaFileName)
        self.initDNAInfo()

    def genDNAFileName(self):
        zoneId = ZoneUtil.getCanonicalZoneId(self.getZoneId())
        hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        hood = ToontownGlobals.dnaMap[hoodId]
        phase = ToontownGlobals.streetPhaseMap[hoodId]
        if hoodId == zoneId:
            zoneId = 'sz'
        return 'phase_%s/dna/%s_%s.dna' % (phase, hood, zoneId)

    def getZoneId(self):
        return self.zoneId

    def setZoneId(self, zoneId):
        self.notify.debug('setting zone id for suit planner')
        self.zoneId = zoneId
        self.setupDNA()

    def extractGroupName(self, groupFullName):
        return groupFullName.split(':', 1)[0]

    def initDNAInfo(self):
        numGraphs = self.dnaStore.discoverContinuity()
        if numGraphs != 1:
            self.notify.info('zone %s has %s disconnected suit paths.' % (self.zoneId, numGraphs))
        self.battlePosDict = {}
        self.cellToGagBonusDict = {}
        for i in xrange(self.dnaStore.getNumDNAVisGroupsAI()):
            vg = self.dnaStore.getDNAVisGroupAI(i)
            zoneId = int(self.extractGroupName(vg.getName()))
            if vg.getNumBattleCells() == 1:
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            elif vg.getNumBattleCells() > 1:
                self.notify.warning('multiple battle cells for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()
        self.streetPointList = []
        self.frontdoorPointList = []
        self.sidedoorPointList = []
        self.cogHQDoorPointList = []
        numPoints = self.dnaStore.getNumSuitPoints()
        for i in xrange(numPoints):
            point = self.dnaStore.getSuitPointAtIndex(i)
            if point.getPointType() == DNASuitPoint.pointTypeMap['FRONT_DOOR_POINT']:
                self.frontdoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.pointTypeMap['SIDE_DOOR_POINT']:
                self.sidedoorPointList.append(point)
            elif (point.getPointType() == DNASuitPoint.pointTypeMap['COGHQ_IN_POINT']) or (point.getPointType() == DNASuitPoint.pointTypeMap['COGHQ_OUT_POINT']):
                self.cogHQDoorPointList.append(point)
            else:
                self.streetPointList.append(point)
            self.pointIndexes[point.getIndex()] = point

    def performPathTest(self):
        if not self.notify.getDebug():
            return None
        startAndEnd = self.pickPath()
        if not startAndEnd:
            return None
        startPoint = startAndEnd[0]
        endPoint = startAndEnd[1]
        path = self.dnaStore.getSuitPath(startPoint, endPoint)
        numPathPoints = path.getNumPoints()
        for i in xrange(numPathPoints - 1):
            zone = self.dnaStore.getSuitEdgeZone(path.getPointIndex(i), path.getPointIndex(i + 1))
            travelTime = self.dnaStore.getSuitEdgeTravelTime(path.getPointIndex(i), path.getPointIndex(i + 1), self.suitWalkSpeed)
            self.notify.debug('edge from point ' + `i` + ' to point ' + `(i + 1)` + ' is in zone: ' + `zone` + ' and will take ' + `travelTime` + ' seconds to walk.')

    def genPath(self, startPoint, endPoint, minPathLen, maxPathLen):
        return self.dnaStore.getSuitPath(startPoint, endPoint, minPathLen, maxPathLen)

    def getDnaStore(self):
        return self.dnaStore
