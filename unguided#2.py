#UNGUIDED2
import timeit

def fibo_iter(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n-1):
            c = a + b
            a = b
            b = c
        return b

print("Hasil iteratif")    
for i in range (1, 101):
    start = timeit.default_timer()
    end = timeit.default_timer()
    print(f'Fibonacci data {i}:', end-start,'detik' '\t' 'bilangan Fibonacci ke:',i , 'adalah :', fibo_iter(i))

def fibo_rek(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo_rek(n-1) + fibo_rek(n-2)

print("Hasil Rekursif")
for i in range (1, 101):
    start = timeit.default_timer()
    end = timeit.default_timer()
    print(f'Fibonacci data {i}:', end-start,'detik' '\t' 'bilangan Fibonacci ke:',i , 'adalah :', fibo_rek(i))
