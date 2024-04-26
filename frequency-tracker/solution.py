class FrequencyTracker:
    def __init__(self):
        self.c=Counter()
        self.rev=Counter()

    def add(self, number: int) -> None:
        self.rev[self.c[number]]-=1
        if self.rev[self.c[number]]<1:
            del self.rev[self.c[number]]
        self.c[number]+=1
        self.rev[self.c[number]]+=1

    def deleteOne(self, number: int) -> None:
        if number in self.c:
            self.rev[self.c[number]]-=1
            if self.rev[self.c[number]]<1:
                del self.rev[self.c[number]]
            self.c[number]-=1
            if self.c[number]<1:
                del self.c[number]
            else:
                self.rev[self.c[number]]+=1
        

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.rev