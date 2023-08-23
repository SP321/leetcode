class Solution:
    def isValid(self, code: str) -> bool:
        def is_start_tag(s: str) -> bool:
            return 1 <= len(s) <= 9 and all(c.isupper() for c in s)

        def is_end_tag(s: str, stack: list) -> bool:
            return stack and stack[-1] == s

        stack, i, n = [], 0, len(code)
        
        while i < n:
            if i > 0 and not stack:
                return False
            if code[i] == '<':
                if code[i:i+9] == "<![CDATA[":
                    j = i + 9
                    while j < n and code[j:j+3] != "]]>":
                        j += 1
                    if j >= n:
                        return False
                    i = j + 3
                    continue

                if i < n - 1 and code[i+1] == '/':
                    j = i + 2
                    while j < n and code[j] != '>':
                        j += 1
                    tag = code[i+2:j]
                    if not is_end_tag(tag, stack):
                        return False
                    stack.pop()
                else:
                    j = i + 1
                    while j < n and code[j] != '>':
                        j += 1
                    if j >= n or j == i+1 or j - i - 1 > 9:
                        return False
                    tag = code[i+1:j]
                    if not is_start_tag(tag):
                        return False
                    stack.append(tag)
                i = j + 1
            else:
                i += 1

        return not stack
