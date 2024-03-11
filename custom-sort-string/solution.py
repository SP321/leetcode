class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order+=ascii_lowercase
        return ''.join(sorted(s,key=order.index))