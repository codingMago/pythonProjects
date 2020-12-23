def sumCost(tilePrice: int, floorHeight: int, floorWidth: int):
    return floorHeight * floorWidth * tilePrice

tileCost = int(input("Tile Cost: "))
floorH = int(input("Height: "))
floorW = int(input("Width: "))
total = sumCost(tileCost, floorH, floorW)

print(total)