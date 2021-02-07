from timeit import default_timer

class Engine:
    isAlive = False
    runAmount = 0 # How many times the engine' been used
    start = default_timer()
    duration = 0


    def __init__(self):
        pass

    def updateDuration(self):
        self.duration = default_timer() - self.start
        
    def startEngine(self):
        self.isAlive = True
        self.runAmount += 1
        self.updateDuration()
    
# u = Engine()

# u.startEngine()
# print(u.isAlive)


# for a in range(0, 20):
#     print(a)

# u.updateDuration()

# print(u.duration)


start = default_timer()
print(start)
duration = default_timer() - start
print(duration)

