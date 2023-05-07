class FrequencyTracker:

    def __init__(self):
        self.c={}
        self.fc={}
    def dec_fc(self,count):
        if count in self.fc:
            self.fc[count]-=1
            if self.fc[count]<0:
                self.fc[count]=0

    def int_fc(self,count):
        if count not in self.fc:
            self.fc[count]=0
        self.fc[count]+=1

    def add(self, number: int) -> None:
        if number not in self.c:
            self.c[number]=0
        self.dec_fc(self.c[number])
        self.c[number]+=1
        self.int_fc(self.c[number])


    def deleteOne(self, number: int) -> None:
        if number in self.c and self.c[number]>0:
            self.dec_fc(self.c[number])
            self.c[number]-=1
            self.int_fc(self.c[number])

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.fc and self.fc[frequency]>0