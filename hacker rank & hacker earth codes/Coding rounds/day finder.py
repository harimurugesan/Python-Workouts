"""for i in range(1,int(input())):
    print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])"""
import time


def cal(x, y, z):
        year = z
        month = y
        mday = x
        my = (year, month, mday, 0, 0, 0, 0, 0, 0)
        new = time.localtime(time.mktime(my))
        print(new)
        if new[6] == 0:
            print("MONDAY")
        if new[6] == 1:
            print("TUESDAY")
        if new[6] == 2:
            print("WEDNESDAY")
        if new[6] == 3:
            print("THURSDAY")
        if new[6] == 4:
            print("FRIDAY")
        if new[6] == 5:
            print("SATURDAY")
       if  new[6] == 6:
            print("SUNDAY")
        
cal(int(input()), int(input()), int(input()))









