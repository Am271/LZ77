class Olc:
    def __init__(self,o,l,c):
        self.offset = o
        self.length = l
        self.character = c
def decode(L):
    #input is given as a list of objects of class Olc
    sb = []
    lab = []
    decstr = ""
    for values in L:
        if values.offset == 0 and values.length == 0:
            decstr = decstr + values.character
        else:
            while(values.offset < values.length):
                decstr = decstr + decstr[-values.offset:-values.length] + values.character
    print(decstr)
                #declist.append(values.character)
    #decstr = "".join(declist)
    print(declist)
o1 = Olc(0,0,'c')
o2 = Olc(0,0,'a')
o3 = Olc(0,0,'b')
o4 = Olc(0,0,'r')
o5 = Olc(3,1,'c')
o6 = Olc(2,1,'d')
o7 = Olc(7,4,'r')
o8 = Olc(3,5,'d')
l = []
l.append(o1)
l.append(o2)
l.append(o3)
l.append(o4)
l.append(o5)
l.append(o6)
l.append(o7)
l.append(o8)
for obj in l:
    print(vars(obj))
decode(l)