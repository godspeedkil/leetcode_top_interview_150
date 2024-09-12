"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
        area = len(matrix) * len(matrix[0])
        result = list()
        while len(result) < area:
            for i in range(left, right+1):
                result.append(matrix[up][i])
            for i in range(up+1, down+1):
                result.append(matrix[i][right])
            if up != down:
                for i in range(right-1, left-1, -1):
                    result.append(matrix[down][i])
            if left != right:
                for i in range(down-1, up, -1):
                    result.append(matrix[i][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return result