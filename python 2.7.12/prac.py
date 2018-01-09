i = input()
j = raw_input().split()
j = [int(ii) for ii in j]
print j 
for jj in j:
    for rr in range(1,jj +1):
        if rr % 3 != 0 and rr % 5 != 0:
            print rr
        else:
            if rr % 3 == 0 and rr % 5 == 0 :
                print "FizzBuzz"
                continue
            if rr % 3 == 0:
                print "Fizz"
            if rr % 5 == 0:
                print "Buzz"
