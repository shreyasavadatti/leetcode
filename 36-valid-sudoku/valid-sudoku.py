class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N=9
        for i in range(N):
            row=[]
            for c in board[i]:
                if c!=".":
                    row.append(c)
            if len(row)!=len(set(row)):
                return False
        for j in range(N):
            col=[]
            for i in range(N):
                if board[i][j]!=".":
                    col.append(board[i][j])
            if len(col)!=len(set(col)):
                return False
        def helper(R,C):
            l=set()
            for i in range (R,R+3):
                for j in range(C,C+3):
                    if board[i][j]==".":
                        continue 
                    if board[i][j] not in l:
                        l.add(board[i][j])
                    else: 
                        return False
            return True
        for i in range(0,N,3):
            for j in range(0,N,3):
                if not helper(i,j):
                    return False
        return True