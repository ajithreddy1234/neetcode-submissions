class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        end=n*n
        start=1
        dq=deque([start])
        dice=0
        visited=set()
        visited.add(start)
        while dq:
            print(dq)
            for _ in range(len(dq)):
                x=dq.popleft()
                print(x)
                if x==end:
                    return dice
                for nxt in range(x+1,min(x+ 6, end)+1):
                    a=nxt-1
                    r=a//n
                    col=a%n
                    row=(n-1)-r
                    if r%2==1:
                        col=(n-1)-col
                    print(row,col)
                    if board[row][col]!=-1:
                        nxt=board[row][col]
                        print(nxt)
                    if nxt not in visited:
                        visited.add(nxt)
                        dq.append(nxt)
            dice+=1
        return -1
        
        

            


        