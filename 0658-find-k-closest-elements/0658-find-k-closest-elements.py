
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def cmp(a,b):
            if abs(a-x)<abs(b-x) or (abs(a-x)==abs(b-x) and a<b):
                return -1
            else:
                return 1
        arr.sort(key=cmp_to_key(cmp))
        return sorted(arr[:k])