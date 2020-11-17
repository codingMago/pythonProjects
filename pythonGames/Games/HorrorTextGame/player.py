class Player:
    userName = ""
    tools = []
    time = 0
    hitPoints = 100
    isAlive = True
    fearLevel = 0

    def init(self, userName, tools, time, hitPoints, isAlive, fearLevel):
        self.userName = userName
        self.tools = tools
        self.time = time
        self.hitPoints = hitPoints
        self.isAlive = isAlive
        self.fearLevel = fearLevel


    # def deathCheck():
    #     if hitPoints == 0:
    #         this.isAlive = False