import numpy
import csv
import matplotlib.pyplot as plt

def turun(p,h,x):
    return (h-x)/(h-p)
def naik(p,h,x):
    return (x-p)/(h-p)

def pendapatan(p,h):

    if (p>=0 and p<=0.5):
        PT = 0
        PS = 0
        PR = 1
        a,b,c = hutang(h)
        l,tl = layak(0,0,PR,a,b,c)
    elif (p>=0.5 and p<0.8):
        PT = 0
        PS = naik(0.5,0.8,p)
        PR = turun(0.5,0.8,p)
        a,b,c = hutang(h)
        l,tl = layak(0,PS,PR,a,b,c)
    elif (p>=0.8 and p<=1.2):
        PT = 0
        PS = 1
        PR = 0
        a,b,c = hutang(h)
        l,tl = layak(0,PS,0,a,b,c)
    elif (p>=1.2 and p<=1.5):
        PT = naik(1.2,1.5,p)
        PS = turun(1.2,1.5,p)
        PR = 0
        a,b,c = hutang(h)
        l,tl = layak(PT,PS,0,a,b,c)
    elif (p>=1.5 and p<=2):
        PT = 1
        PS = 0
        PR = 0
        a,b,c = hutang(h)
        l,tl = layak(PT,0,0,a,b,c)

    return PT,PS,PR,a,b,c,l,tl

def hutang(p):
    if (p>=0 and p<=30):
        HT = 0
        HS = 0
        HR = 1
    elif (p>=30 and p<=40):
        HT = 0
        HS = naik(30,40,p)
        HR = turun(30,40,p)
    elif (p>=40 and p<=60):
        HT = 0
        HS = 1
        HR = 0
    elif (p>=60 and p<=70):
        HT = naik(60,70,p)
        HS = turun(60,70,p)
        HR = 0
    elif (p>=70 and p<=100):
        HT = 1
        HS = 0
        HR = 0

    return HT,HS,HR

def layak(PT,PS,PR,HT,HS,HR):
    l=0
    tl=0
    if (PT and HT):
        tl=nilai(PT,HT,tl)
    if (PT and HS):
        tl=nilai(PT,HS,tl)
    if (PT and HR):
        tl=nilai(PT,HR,tl)
    if (PS and HT):
        l=nilai(PS,HT,l)
    if (PS and HS):
        l=nilai(PS,HS,l)
    if (PS and HR):
        tl=nilai(PS,HR,tl)
    if (PR and HT):
        l=nilai(PR,HT,l)
    if (PR and HS):
        l=nilai(PR,HS,l)
    if (PR and HR):
        l=nilai(PR,HR,l)

    return l,tl

def nilai(pn, ht, ly):
    if (pn<=ht):
        if (pn>=ly):
            return pn
        else :
            return ly
    if (pn>=ht):
        if (ht>=ly):
            return ht
        else:
            return ly
        
def rumus(l,tl):
    return((tl*35)+(l*70))/(tl+l)
    
        
arr =[]
k = 0
from numpy import genfromtxt
my_data = genfromtxt('DataTugas2.csv', delimiter=',',skip_header=True)
o = open('test.csv', 'w')
w = csv.writer(o)
for i in range(len(my_data)):
    PT,PS,PR,a,b,c,l,tl = pendapatan(my_data[i][1],my_data[i][2])
    print(l,tl)
    n = rumus(float(l),float(tl))
    final = {
            "no" : int(my_data[i][0]),
            "nilai" : n
            }
    arr.append(final);
arr.sort(key=lambda x: x['nilai'], reverse=True)
lst = []
for x in range(20):
    lst.append(int(arr[x]['no']))
z = numpy.asarray(lst)
z.tofile('test.csv',sep=',',format='%10.5f')

xa = [0,30,40]
ya = [1, 1, 0]
xb = [30,40,60,70]
yb = [0,1,1,0]
xc = [60,70,105]
yc = [0, 1, 1]
plt.plot(xa, ya, label='rendah')
plt.plot(xb, yb, label='sedang')
plt.plot(xc, yc, label='tinggi')
plt.show()

o.close()       
k =input()  
