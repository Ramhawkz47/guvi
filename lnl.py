class largest:
    def __init__(self):
        self.n=input()
        self.nlist= (self.n).split(" ")
        self.nlist=[int(i) for i in self.nlist]
    def find(self):
        if(self.nlist[0]>self.nlist[1] and self.nlist[0]>self.nlist[2]):
            print(self.nlist[0])
        elif(self.nlist[1]>self.nlist[0] and self.nlist[1]>self.nlist[2]):
            print(self.nlist[1])
        else:
            print(self.nlist[2])

l= largest()
l.find()
