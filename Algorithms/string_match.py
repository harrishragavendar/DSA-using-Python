def string_match(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i
    return -1


if __name__ == '__main__':
    print(string_match('haystack', 'stack'))
    print(string_match('leetcode', 'leeto'))

# TC: O(n * m)
# SC: O(1)
