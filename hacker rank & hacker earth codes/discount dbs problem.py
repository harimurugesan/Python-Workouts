def disc(prices):
    newprice = []
    discountprice = []
    list1 = []
    lenp = len(prices)
    for i in range(lenp):
        discountprice.append(int(input()))
    print(discountprice)
    for num1, num2 in enumerate(prices):
        newprice.append(num2 - discountprice[num1])
    print(newprice)
    for p1,p2 in enumerate(prices):
        if p2 == newprice[p1]:
            list1.append(p1)
    print(list1)
    list1 = map(str,list1)
    print(" ".join(list1))
disc([50,30,20,33,53,90])

