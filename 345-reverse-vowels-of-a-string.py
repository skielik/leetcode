"""
345. Reverse Vowels of a String - Easy
https://leetcode.com/problems/reverse-vowels-of-a-string/
Pattern: Strings, collect and reverse
Time: O(n)   Space: O(n)
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        vowels_in_s = []
        result = ''
        for i in s:
            for j in vowels:
                if i == j:
                    vowels_in_s.append(i)
                    break
        index = 0
        for i in s:
            if index < len(vowels_in_s) and i == vowels_in_s[index]:
                result += vowels_in_s[-(index+1)]
                index += 1
            else:
                result += i
        return result     


if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseVowels("IceCreAm") == "AceCreIm"
    assert sol.reverseVowels("leetcode") == "leotcede"
    print("all tests passed")