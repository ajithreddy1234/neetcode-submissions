from collections import Counter
import heapq
from typing import List


class Pair:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        # Lower frequency = worse
        if self.freq != other.freq:
            return self.freq < other.freq

        # Same frequency:
        # lexicographically larger word = worse
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = []

        for word, freq in count.items():
            heapq.heappush(heap, Pair(freq, word))

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        while heap:
            ans.append(heapq.heappop(heap).word)

        return ans[::-1]