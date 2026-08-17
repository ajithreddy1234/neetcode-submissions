class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        x=Counter(words)
        arr=list(x.items())
        arr.sort(key=lambda x:(-x[1],x[0]))
        return [word for word,freq in arr[:k]]
        