import numpy as np

def error(w0,w1,points,m):
    err=0
    for i in range(0,m):
        x=points[i][0]
        y=points[i][1]
        err=+ (y-(w0+w1*x))**2  #Error Function
    err=err/float(m)
    print(err)



def gradiant(w0,w1,points,m,lr):
    new0=0
    new1=0
    n=float(m)
    for i in range(0,m):
        x = points[i][0]
        y = points[i][1]
        new0+=(-(2/n)*(y-(w0+w1*x)))        # dj(o0,o1)/dx  ---->> formula
        new1+=(-(2/n)*((y-(w0+w1*x))*x))

    new0=w0-lr*new0
    new1=w1- lr*new1
    return [new0,new1]


def run(w0,w1,ltr,lr):
    points=np.genfromtxt('data.csv', delimiter=',')
    print(points)
    m=len(points)
    print('input:: W and m')
    print(w0,w1)
    print("Error is:: ")
    error(w0,w1,points,m)

    for i in range(1,itr):
        [w0,w1]=gradiant(w0,w1,points,m,lr)

    print("Final error:: ")
    error(w0,w1,points,m)
    print("Output :: w and m")
    print(w0,w1)
    return [w0,w1]


def check(a):
    print("Prediction is::")
    print(w0+w1*a)

if __name__=='__main__':
    w0 = 4
    w1 = 9
    itr = 10000
    lr = 0.001
    [w0,w1]=run(w0,w1,itr,lr)

    check(11)