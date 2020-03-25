class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # checking rows
        for i in range(9):
            arr = []
            for j in range(9):
                temp = board[i][j]
                if temp != '.':
                    if temp not in arr:
                        arr.append(temp)
                        continue
                    return False
        #Checking column

        for i in range(9):
            arr = []
            for j in range(9):
                temp = board[j][i]
                if temp != '.':
                    if temp not in arr:
                        arr.append(temp)
                        continue
                    return False

        # Checking 3*3
        for x in range(0,9,3):
            for y in range(0,9,3):
                arr = []
                for i in range(3):
                    for j in range(3):
                        temp = board[j][i]
                        if temp != '.':
                            if temp not in arr:
                                arr.append(temp)
                                continue
                            return False
        return True