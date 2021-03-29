'''
문자열 중에서 가장 긴 palindrome 찾기

입력 : "babad"
출력 : "bab" or "aba"
'''

def longestPalindrome(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    # sliding window 우측이동 (2 pointer sliding : even, odd)
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result


if __name__ == "__main__":
    input_str = "babad";
    result = longestPalindrome(input_str)
    print("result = ", result)