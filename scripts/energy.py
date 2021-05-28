weight = 250

# E = mc^2
def measureEnergy(weight):
    gravity = 9.81 # Earth's gravity
    speedOfLight = 299_792_458 

    mass = weight / gravity

    cs = speedOfLight**2 # C squared

    energy = mass * cs
    print(energy + "J")


measureEnergy(250)