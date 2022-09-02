"""
Question Link
    https://leetcode.com/problems/surrounded-regions/    
"""
# This Problem can be done in a similar way
class Solution(object):
    def checkBorder(self,i,j,board,checkBoard):
        if (i==len(board)-1 or j==len(board[0])-1 or i==0 or j==0) and board[i][j]=="O":
            return False
        return True
    def flip(self,board,i,j):
        if board[i][j]=="X":
            return
        board[i][j]="X"        
        if i+1<len(board):
            self.flip(board,i+1,j)
        if i-1>=0:
            self.flip(board,i-1,j)
        if j+1<len(board[0]):
            self.flip(board,i,j+1)
        if j-1>=0:
            self.flip(board,i,j-1)        
    def markedDanger(self,board,checkBoard,i,j):        
        if checkBoard[i][j]==-1 or board[i][j]=="X":
            return
        if board[i][j]=="O":
            checkBoard[i][j]=-1
        if i+1<len(board):
            self.markedDanger(board,checkBoard,i+1,j)
        if i-1>=0:
            self.markedDanger(board,checkBoard,i-1,j)
        if j+1<len(board[0]):
            self.markedDanger(board,checkBoard,i,j+1)
        if j-1>=0:
            self.markedDanger(board,checkBoard,i,j-1)
        
    def checkSurrounded(self,i,j,board,checkBoard):
        l=len(board[0])
        h=len(board)
        if not (self.checkBorder(i+1,j,board,checkBoard) and self.checkBorder(i-1,j,board,checkBoard) and self.checkBorder(i,j+1,board,checkBoard) and self.checkBorder(i,j-1,board,checkBoard)):
            checkBoard[i][j]=1
            return False
        status=True
        checkBoard[i][j]=1
        if i+1<h-1 and board[i+1][j]=="O" and checkBoard[i+1][j]!=1:      
            s=self.checkSurrounded(i+1,j,board,checkBoard)
            if s==False:
                status=False                
        if i-1>0 and board[i-1][j]=="O" and checkBoard[i-1][j]!=1:
            s=self.checkSurrounded(i-1,j,board,checkBoard)
            if s==False:
                status=False
        if j+1<l-1 and board[i][j+1]=="O" and checkBoard[i][j+1]!=1:
            s=self.checkSurrounded(i,j+1,board,checkBoard)
            if s==False:
                status=False
        if j-1>0 and board[i][j-1]=="O" and checkBoard[i][j-1]!=1:
            s=self.checkSurrounded(i,j-1,board,checkBoard)
            if s==False:
                status=False
        return status
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        l=len(board[0])
        h=len(board)
        if l<3:
            return
        checkBoard=[ [0] * l for i1 in range(h)]
        for i in range(1,h-1):
            for j in range(1,l-1):                
                if board[i][j]=="O" and checkBoard[i][j]!=1 and checkBoard[i][j]!=-1:         
                    st=self.checkSurrounded(i,j,board,checkBoard)
                    if st==True:
                        self.flip(board,i,j)
                    else:
                        self.markedDanger(board,checkBoard,i,j)
