def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower = 1
        upper = n
        while True:
            target = lower + ((upper - lower) // 2)
            if upper - lower <= 1:
                if isBadVersion(lower):
                    return lower
                return upper
            if isBadVersion(target):
                upper = target
            else:
                lower = target


##ans
def firstBadVersion(self, n: int) -> int:
    left = 1
    right = n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left
