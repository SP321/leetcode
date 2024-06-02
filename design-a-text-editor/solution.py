class TextEditor:

    def __init__(self):
        self.x = []
        self.y = []

    def addText(self, text: str) -> None:
        for x in text:
            self.x.append(x)

    def deleteText(self, k: int) -> int:
        for i in range(k):
            if not self.x:
                return i
            self.x.pop()
        return k

    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if not self.x:
                break
            self.y.append(self.x.pop())
        return ''.join(self.x[max(0, len(self.x) - 10):])

    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if not self.y:
                break
            self.x.append(self.y.pop())
        return ''.join(self.x[max(0, len(self.x) - 10):])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)