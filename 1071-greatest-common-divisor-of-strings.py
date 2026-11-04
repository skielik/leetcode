"""
1071. Greatest Common Divisor of Strings - Easy
https://leetcode.com/problems/greatest-common-divisor-of-strings/
Pattern: Math (GCD), strings
Time: O(n + m)   Space: O(n + m)
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        resultLen = 0
        result = ""
        if(len(str1) >= len(str2)):
            resultLen = len(str2)
            longest = str1
        else:
            resultLen = len(str1)
            longest = str2

        if(resultLen > 1):
            while((len(str1) % resultLen != 0) or (len(str2) % resultLen != 0)):
                resultLen -= 1

        for i in range(resultLen):
            if(str1[i] == str2[i]):
                result += str1[i]
            else:
                break
        if(len(result) != resultLen):
            result = ""

        if(result != ""):
            i = 0
            for letter in str1:
                if (i >= (resultLen)):
                    i = 0
                if(letter == result[i]):
                    i += 1
                    continue
                else:
                    result = ""
                    return result
                    break
            i = 0
            for letter in str2:
                if (i >= (resultLen)):
                    i = 0
                if(letter == result[i]):
                    i += 1
                    continue
                else:
                    result = ""
                    return result
                    break
            
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert sol.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert sol.gcdOfStrings("LEET", "CODE") == ""
    print("all tests passed")