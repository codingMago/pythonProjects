# Runtime: 208 ms, faster than 44.06% of Python3 online submissions for Subrectangle Queries.
# Memory Usage: 16.1 MB, less than 49.77% of Python3 online submissions for Subrectangle Queries.
rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]

class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle # Copy over the initial rectangle instantiation
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # Loop through entirety of rows and columns assigning all to newValue on the way
        # Loop within a loop, O(N^2)
        for i in range(row1, row2+1): 
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
        

def useRectangle(rectangle):
    obj = SubrectangleQueries(rectangle)
    print(obj.getValue(0,2))
    obj.updateSubrectangle(0,0,3,2,5)
    print(obj.getValue(0,2))
    print(obj.getValue(3,1))
    obj.updateSubrectangle(3,0,3,2,10)
    print(obj.getValue(3,1))
    print(obj.getValue(0,2))
# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
useRectangle(rectangle)