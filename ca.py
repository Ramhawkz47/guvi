class alphabet:
    def __init__(self):
        self.str= input()
        self.vowels=["a","e","i","o","u"]
        self.alpha="abcdefghijklmnopqrstuvwxyz"
    def check(self):
        if(self.str in self.alpha):
            if(self.str in self.vowels):
                print("Vowel")
            else:
                print("Consonant")
        else:
            print("invalid")

a= alphabet()
a.check()
