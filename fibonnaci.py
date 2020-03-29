def fibonnaci(n):
    #la suite de fibonnaciccino
    a, b, c = 1, 1, 0
    while (c < n):
        print(f'{c+1:2} _ {a:8} : {b:9}')
        a, b, c = b, a+b, c+1
        
def fibon(n):
    #la suite de fibonnaci
    a, b, c = 1, 1, 0
    s = 'f_ibon('+ str(n) + ') = '
    while (c < n):
        a, b, c = b, a+b, c+1
    s = s + str(a)
    print(s)
