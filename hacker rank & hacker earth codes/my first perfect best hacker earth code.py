i = int(input())
a = []
for loop in range(i):
    a.append(input())
for new in a:
    SUVO = 0
    SUVOJIT = 0
    if "SUVOJIT" or "SUVO" in new:
        sj = new.count("SUVOJIT")
        if "SUVO" in new:
            ss = new.count("SUVO")
            if ss > sj:
                diff = ss - sj
                SUVO += diff
                SUVOJIT += sj
            if ss == sj:
                SUVOJIT += sj


    print("SUVO = {0}, SUVOJIT = {1}".format(SUVO, SUVOJIT))



