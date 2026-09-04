class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        dq=deque([beginWord])
        visited={beginWord}
        level=1
        while dq:
            for _ in range(len(dq)):
                x=dq.popleft()
                if x==endWord:
                    return level
                for i in range(len(x)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
            
                        if ch==x[i]:
                            continue
                        y=x[:i]+ch+x[i+1:]
                        if y in wordList:
                            print(y)
                            if y not in visited:
                                visited.add(y)
                                dq.append(y)
            level+=1
        return 0
