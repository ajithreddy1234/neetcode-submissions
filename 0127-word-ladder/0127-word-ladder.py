class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        dq = deque([beginWord])
        level = 1

        words.discard(beginWord)

        while dq:
            for _ in range(len(dq)):
                word = dq.popleft()

                if word == endWord:
                    return level

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        nxt = word[:i] + ch + word[i + 1:]

                        if nxt in words:
                            words.remove(nxt)
                            dq.append(nxt)

            level += 1

        return 0