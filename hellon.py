class hello:
    def __init__(self):
        self.n= int(input())
    def printing(self):
        for i in range(0,self.n):
            print("Hello")

h= hello()
h.printing()
