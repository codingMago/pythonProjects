class Tools:
    isSharp = False
    canFish = False
    toolMaker = False # Is this a prereq for other tools?

    def init(self, isSharp, canFish, toolMaker):
        self.isSharp = isSharp
        self.canFish = canFish
        self.toolMaker = toolMaker