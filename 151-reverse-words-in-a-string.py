"""
151. Reverse Words in a String - Medium
https://leetcode.com/problems/reverse-words-in-a-string/
Pattern: Strings, manual split
Time: O(n)   Space: O(n)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = []
        is_word = False
        for c in s:
            if c != ' ':
                word.append(c)
                is_word = True
            elif is_word == True:
                words.append(''.join(word))
                is_word = False
                word = []
        if is_word:
            words.append(''.join(word))
        words.reverse()
        return ' '.join(words)


if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseWords("the sky is blue") == "blue is sky the"
    assert sol.reverseWords("  hello world  ") == "world hello"
    print("all tests passed")