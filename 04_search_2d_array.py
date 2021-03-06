"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # time O(m+n), space O(1)
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        return self.search_matrix(matrix, target, 0, 0, len(matrix)-1, len(matrix[0])-1)

    def search_matrix(self, matrix, target, x1, y1, x2, y2):
        if x1 == x2:
            for i in range(y1, y2+1):
                if matrix[x1][i] == target:
                    return True
            return False
        if y1 == y2:
            for i in range(x1, x2+1):
                if matrix[i][y1] == target:
                    return True
            return False
        i, j = x1, y1
        while i < x2 and j < y2 and matrix[i][j] < target:
            i += 1
            j += 1
        return self.search_matrix(matrix, target, i, y1, x2, j) or self.search_matrix(matrix, target, x1, j, i, y2)


class Solution1:
    # time O(m+n), space O(1)
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            if matrix[i][j] < target:
                i += 1
        return False

test = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
solution = Solution()
print(solution.findNumberIn2DArray(test, 5))
print(solution.findNumberIn2DArray(test, 20))
print(solution.findNumberIn2DArray([[2]], 2))