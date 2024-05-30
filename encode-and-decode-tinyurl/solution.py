class Codec:
    def __init__(self):
        self.x=[]

    @cache
    def encode(self, longUrl: str) -> str:
        self.x.append(longUrl)
        return len(self.x)-1

    def decode(self, shortUrl: str) -> str:
        return self.x[int(shortUrl)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))