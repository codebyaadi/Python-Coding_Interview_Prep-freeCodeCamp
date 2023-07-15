def permAlone(str):
    def swap(s, i, j):
        chars = list(s)
        chars[i], chars[j] = chars[j], chars[i]
        return ''.join(chars)

    def has_repeat(s):
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return True
        return False

    def permute(s, start, end):
        nonlocal counter
        if start == end:
            if not has_repeat(s):
                counter += 1
        else:
            for i in range(start, end + 1):
                s = swap(s, start, i)
                permute(s, start + 1, end)
                s = swap(s, start, i)  # backtrack

    counter = 0
    permute(str, 0, len(str) - 1)
    return counter

# Optimized Solution
#
# def permAlone(str):
#     def permute(chars, start, end):
#         nonlocal counter
#         if start == end:
#             if not any(chars[i] == chars[i + 1] for i in range(end)):
#                 counter += 1
#         else:
#             for i in range(start, end + 1):
#                 chars[start], chars[i] = chars[i], chars[start]
#                 if start == 0 or chars[start - 1] != chars[start]:
#                     permute(chars, start + 1, end)
#                 chars[start], chars[i] = chars[i], chars[start]  # backtrack

#     chars = list(str)
#     counter = 0
#     permute(chars, 0, len(chars) - 1)
#     return counter


print(permAlone('aab'))  # Output: 2
print(permAlone('aaa'))  # Output: 0
print(permAlone('aabb'))  # Output: 8
print(permAlone('abcdefa'))  # Output: 3600
print(permAlone('abfdefa'))  # Output: 2640
print(permAlone('zzzzzzzz'))  # Output: 0
print(permAlone('a'))  # Output: 1
print(permAlone('aaab'))  # Output: 0
print(permAlone('aaabb'))  # Output: 12
