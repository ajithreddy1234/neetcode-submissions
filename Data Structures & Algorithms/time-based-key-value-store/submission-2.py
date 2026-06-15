class TimeMap:

    def __init__(self):
        self.box = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.box:
            self.box[key] = []

        self.box[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.box:
            return ""

        values = self.box[key]

        left = 0
        right = len(values) - 1
        answer = ""

        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][0] <= timestamp:
                answer = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return answer