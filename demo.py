a = open("aaa.txt", "r")
cc=len(open("aaa.txt",'r').readlines())
num = 1
while num <= cc:
    line = a.readlines(num)
    line_1=str(line)
    ii = line_1.rstrip()
    kk = ii.ljust(30)
    g = "#"+str(num)
    sh = kk+g
    num = num+1
    print(sh)

'''a = open("aaa.txt", "r")
cc=len(open("aaa.txt",'r').readlines())
for line in a.readlines():
    ii = line.rstrip()
    kk = ii.ljust(30)
    g = '#1'
    hh = kk+g
    print(hh)'''
