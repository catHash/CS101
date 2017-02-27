def polygon_area(x,y):
    z=0
    n=len(x)
    w=0
    print('x: ' + str(x))
    print('y: ' + str(y))
    for i in range (0, len(x)-1):
        w+=(x[i]*y[i+1])
        z+=(y[i]*x[i+1])
        print('w+=(' + str(x[i-1]) + '' + '*' + str(y[i]) + ')')
        print('i: ' + str(i) + ' w: ' + str(w))
        print('z+=(' + str(y[i-1]) + '' + '*' + str(x[i]) + ')')
        print('i: ' + str(i) + ' z: ' + str(z))
    w+=(x[n-1]*y[0])
    z+=(y[n-1]*x[0])
    print('i: ' + str(i) + ' w: ' + str(w))
    print('i: ' + str(i) + ' z: ' + str(z))
    A=abs(.5*(w-z))
    print('area: ' + str(A))
    return A
#polygon_area( [0, 1, 1, 0],[0, 0, 1, 1] )#1
polygon_area( [0, -1, -1, 0, 0, 1],[-1, -1, 0, 1, 1, 0] )#4
