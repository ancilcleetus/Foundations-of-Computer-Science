# Problem Description
# Given N rectangles with their length and breadth in array A and B.

# Create a class Rectangle that supports the following functionalities:

# Check if the given rectangle is a square.
# Find area of the rectangle.
# Check if the area is greater than K (K is passes as parameter in the function).
# Use this class to answer this question - Find the count of squares on the left with area greater than current rectangle area for all rectangles.


# Problem Constraints
# 1 <= N <= 103

# 1 <= A[i] <= 103

# 1 <= B[i] <= 103



# Input Format
# The two argument A and B are integer arrays that denote the length and breadth of the N rectangles respectively.



# Output Format
# Return an integer array where each element denotes the count of squares on the left with area greater than current rectangle area.


# Example Input
# Input 1:

# A = [4, 6, 7]
# B = [4, 6, 2]
# Input 2:

# A = [2, 5, 3, 6, 2]
# B = [4, 5, 1, 6, 2]


# Example Output
# Output 1:

# [0, 0, 2]
# Output 2:

# [0, 0, 1, 0, 2]


# Example Explanation
# Explanation 1:

# The area of rectangles are [16, 36, 14]. Of them 1-st and 2-nd are
# squares.
# Explanation 2:

# The area of rectangles are [8, 25, 3, 36, 4]. Of them only 2-nd and 4-th
# are squares.

from time import perf_counter_ns

class Rectangle:
    def __init__(self, x, y):
        self.length = x
        self.breadth = y
    
    def getArea(self):
        return self.length * self.breadth
    
    def isSquare(self):
        return self.length == self.breadth
    
    def isAreaGreaterThan(self, K):
        return self.getArea() > K

def getCountOfSquares(A, B):
    count_of_squares_data = []
    rectangles = [Rectangle(x, y) for x, y in zip(A, B)]
    for i, (rectangle) in enumerate(rectangles):
        count_of_squares = 0
        area = rectangle.getArea()
        for j in range(i):
            if rectangles[j].isSquare() and rectangles[j].isAreaGreaterThan(area):
                count_of_squares += 1
        
        count_of_squares_data.append(count_of_squares)
    
    return count_of_squares_data

A = [2, 5, 3, 6, 2]
B = [4, 5, 1, 6, 2]
tic = perf_counter_ns()
print(f"Output = {getCountOfSquares(A, B)}")
toc = perf_counter_ns()
print(f"Took {(toc-tic)/1000} us")