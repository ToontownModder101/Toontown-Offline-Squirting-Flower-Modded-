# File: D (Python 2.4)

import DistributedSZTreasureAI

class DistributedMMTreasureAI(DistributedSZTreasureAI.DistributedSZTreasureAI):
    
    def __init__(self, air, treasurePlanner, x, y, z):
        DistributedSZTreasureAI.DistributedSZTreasureAI.__init__(self, air, treasurePlanner, x, y, z)


