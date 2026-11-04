"""
1768. Merge Strings Alternately - Easy
https://leetcode.com/problems/merge-strings-alternately
Pattern: simultaneous Iteration + slicing
Time: O(n+m)   Space: O(n+m)
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        l = len(word1) - len(word2)
        if l > 0:
            l = len(word2)
            for i in range(l):
                word3 += word1[i] + word2[i]
            word3 += word1[l:]
        elif l < 0:
            l = len(word1)
            for i in range(l):
                word3 += word1[i] + word2[i]
            word3 += word2[l:]
        else:
            l = len(word1)
            for i in range(l):
                word3 += word1[i] + word2[i]          
        return word3


if __name__ == "__main__":
    sol = Solution()
    assert sol.mergeAlternately("abc", "pqr") == "apbqcr"
    assert sol.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert sol.mergeAlternately("abcd", "pq") == "apbqcd"
    print("all tests passed")