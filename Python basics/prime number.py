lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper + 1):
   x=' '
   print(num,"val in f1")
   # prime numbers are greater than 1
   if num > 1:
       print((10*x),num ,"in if")
       for i in range(2,num):
           print((20*x), num,"val in f2","i=",i)
           if (num % i) == 0:
               print((50*x),num,"is not p")
               break
       else:
           print((40*x),num,"is prime num")
