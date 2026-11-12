"""
605. Can Place Flowers - Easy
https://leetcode.com/problems/can-place-flowers/
Pattern: Greedy, array
Time: O(n)   Space: O(1)
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        j = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i != 0 and i != len(flowerbed) - 1:
                    if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                        flowerbed[i] = 1
                        j += 1
                elif i == 0:
                    if len(flowerbed) != 1:
                        if flowerbed[i+1] != 1:
                            flowerbed[i] = 1
                            j += 1
                    else:
                        j += 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] != 1:
                        flowerbed[i] = 1
                        j += 1
        return j >= n


if __name__ == "__main__":
    sol = Solution()
    assert sol.canPlaceFlowers([1,0,0,0,1], 1) == True
    assert sol.canPlaceFlowers([1,0,0,0,1], 2) == False
    print("all tests passed")