import math 

def f(x):
    f = (x-1)**2*(x-2)*(x-3)
    return f

xalt = -10
xust = 40
dx = 0.0001
alpha = (1 + math.sqrt(5))/2
tau = 1 - 1/alpha
epsilon = dx /(xust-xalt)
N = round(-2.078*math.log(epsilon))

k = 0
x1 = xalt + tau*(xust-xalt)
f1 = f(x1)
x2 = xust - tau*(xust - xalt)
f2 = f(x2)
print(k,x1,x2,f1,f2)

for k in range(0,N):
    if f1>f2:
        xalt = 𝑥1
        x1 = x2
        f1 = f2
        x2 =  xust - tau*(xust - xalt)
        f2 = f(x2)
        k = k + 1
    else:
        xust = x2
        x2 = x1
        f2 = f1
        x1 = xalt + tau*(xust - xalt)
        f1 = f(x1)
    print(k+1,x1,x2,f1,f2)

x = 0.5*(x1+x2)
print(x)