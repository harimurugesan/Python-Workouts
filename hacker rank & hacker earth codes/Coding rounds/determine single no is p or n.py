def main():
    i = int(input())
    for n in range(2,i):
        if i % n == 0:
            print("not prime")
            print(i, "=", n, "*", i//n )
            break
    else:
        print("prime")
main()
