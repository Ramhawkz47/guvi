class alpha:
    def __init__(self):
        self.alphabets="abcdefghijklmnopqrstuvwxyz"
        self.inp=input()
    def checkalpha(self):
        if(self.inp in self.alphabets):
            print("Alphabet")
        else:
            print("No")

a1= alpha()
a1.checkalpha()
