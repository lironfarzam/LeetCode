# Q3. Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        char_dict = {}
        for i in range(len(s)):
            if s[i] in char_dict and char_dict[s[i]] >= start:
                start = char_dict[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            char_dict[s[i]] = i
        return max_len

if __name__ == "__main__":
    print("Q3. Longest Substring Without Repeating Characters")
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
    print("End of Q3. Longest Substring Without Repeating Characters")

