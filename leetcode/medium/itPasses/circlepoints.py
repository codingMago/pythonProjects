# Runtime: 2412 ms, faster than 62.52% of Python3 online submissions for Queries on Number of Points Inside a Circle.
# Memory Usage: 14.8 MB, less than 19.86% of Python3 online submissions for Queries on Number of Points Inside a Circle.

points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]

def countPoints(points, queries):
    result = [] # Placeholder array
    for xq, yq, r in queries: # Loop queries and hold all values
        count = 0 # Keep track of how many are within query
        for x, y in points: # Loop within points
            if (x-xq)**2 + (y-yq)**2 <= r**2: #
                count += 1
                
        result.append(count)
        
    return result

print(countPoints(points, queries))