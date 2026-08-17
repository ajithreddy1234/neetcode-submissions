class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        n=len(matrix)*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(heap,matrix[i][j])
                if len(heap)>n-k+1:
                    heapq.heappop(heap)
        return heap[0]