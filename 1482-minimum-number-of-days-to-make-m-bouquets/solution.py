class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        # Not enough flowers
        if m * k > n:
            return - 1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day <= mid:
                    flowers +=1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                        flowers = 0
            if bouquets >= m:
                        # possible, try fewer days
                        right = mid
            else:
                        # Not possible, need more days
                        left = mid + 1
        return left               
        