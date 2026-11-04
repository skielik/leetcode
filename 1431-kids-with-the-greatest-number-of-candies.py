"""
1431. Kids With the Greatest Number of Candies - Easy
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Pattern: Array, brute force
Time: O(n²)   Space: O(n)
"""

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = [False] * len(candies)
        
        for i in range(len(candies)):
            for j in range(len(candies)):
                if candies[i] + extraCandies >= candies[j]:
                    result[i] = True
                else:
                    result[i] = False
                    break

        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True] 
    assert sol.kidsWithCandies([4,2,1,1,2], 1) == [True,False,False,False,False] 
    assert sol.kidsWithCandies([12,1,12], 10) == [True,False,True]
    print("all tests passed")