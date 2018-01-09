
def main():
    r = int(input())
    a =[]
    b = []
    for n in range(2, r):
        for x in range(2, n):
            if n % x == 0:
                a.append(n)
                #print(n, 'equals', x, '*', n // x, "so it is not a prime number")
                break
        else:
            b.append(n)
            #print(n, 'is a prime number')
    print("prime numbers are :",b)
    print("non prime numbers are :",a)
main()