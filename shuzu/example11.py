class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 统计长度
        size = len(matrix)
        # 行
        for i in range(size):
            # 列
            for j in range(i+1,size):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(size):
            matrix[i].reverse()

        return matrix


s=Solution()
result=s.rotate([

])
print(result)