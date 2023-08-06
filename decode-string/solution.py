class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_count = 0

        for char in s:
            if char.isdigit():
                current_count = current_count * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_count))
                current_str = ""
                current_count = 0
            elif char == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + num * current_str
            else:
                current_str += char

        return current_str