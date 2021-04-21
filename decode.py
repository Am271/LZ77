class Olc:
    def __init__(self,o,l,c):
        self.offset = o
        self.length = l
        self.character = c
def sliding(compstr,L):#(compstr,L)
    sb = 7
    lab = 6
    window = []
    sep = ("|")
    for i in range(sb):
        window.append('_')
    window.append(sep)
    for i in range(lab):
        window.append(compstr[i])
    print(compstr)
    print(window)
    for values in L:
        if(values.offset == 0 and values.length == 0):
            if window[sb-1] == '_':
                window[sb-1] = window[sb+1]
            else:
                window[sb-3] = window[sb-2]
                window[sb-2] = window[sb-1]
                window[sb-1] = window[sb+3]     
        else:   
            break 
        print(window)    
    #print(window.index('|'))
def decode(L):
    #input is given as a list of objects of class Olc
    c = 0
    tl = []
    declist = []
    for values in L:
        if(values.offset == 0 and values.length == 0):
            declist.append(values.character)
        while(values.offset != 0 and values.length != 0):
            tl = declist[-values.offset:-(values.length-1)]
            declist.extend(tl)
            declist.append(values.character)
            break;
    decstr = "".join(declist)
    print(decstr)
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
#l.append(o4)
#l.append(o5)
#l.append(o6)
#l.append(o7)
#l.append(o8)
#for obj in l:
#    print(vars(obj))
#decode(l)
st = "bfcbbacbbcrccac"
sliding(st,l)
    
