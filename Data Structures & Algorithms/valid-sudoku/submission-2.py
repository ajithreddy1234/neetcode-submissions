class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set1=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in set1 :
                    return False
                set1.add(board[i][j])
            set1.clear()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in set1:
                    return False
                set1.add(board[j][i])
            set1.clear()

        for i in range(0,9,3):
            for j in range(0,9,3):

                seen=set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] == ".":
                            continue

                        if board[k][l] in seen:
                            return False

                        seen.add(board[k][l])
        return True



                
         
            
        