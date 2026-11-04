"""
1456. Maximum Number of Vowels in a Substring of Given Length - Medium
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
Pattern: Sliding Window (fixed size)
Time: O(n)   Space: O(1)
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        first, last = 0, k
        max_v = 0
        for i in range(0,k):
            if s[i] in vowels:
                max_v += 1
        v = max_v
        while last < len(s):
            if s[last] in vowels:
                v += 1
            if s[first] in vowels:
                v -= 1
            first += 1
            last += 1
            max_v = max(max_v, v)
        return max_v

        '''
        First try
        O(n*k)
        max_v, v = 0, 0
        l = len(s)
        write,read = 0, 0
        while write <= (l-k):
            if read >= (write + k):
                write += 1
                read = write
                max_v = max(max_v, v)
                v = 0
            else:
                if s[read] in vowels:
                    v += 1
                read += 1
        return max_v
        '''


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxVowels("abciiidef", 3) == 3
    assert sol.maxVowels("aeiou", 2) == 2
    assert sol.maxVowels("leetcode", 3) == 2
    print("all tests passed")