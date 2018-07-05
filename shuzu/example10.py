class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for item in board:
            temp={}
            for i in item:
                if (i not in temp.keys()) or (i == '.'):
                    temp[i]=1
                else:
                    return False

        for row in range(0,9):
            temp = {}
            for lie in range(0,9):
                if (board[row][lie] not in temp.keys()) or (board[row][lie] == '.'):
                    temp[board[row][lie]] = 1
                else:
                    return False


        return True


s=Solution()
result=s.isValidSudoku(
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
)
print(result)