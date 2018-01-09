i = int(input())
str_list = []
men_ninteen_scr = 0
men_other_scr = 0
girl_ninteen_scr = 0
girl_other_scr = 0
ran = range(1,32)
newlist= []
for newran in ran:
    if newran != 19:
        if newran != 20:
            newlist.append(str(newran))
for num in range(i):
    str_list.append(input())
for msg in str_list:
    if msg.startswith("M:"):
        if '19' in msg:
            men_ninteen_scr += 1
        if '20' in msg and '19' not in msg:
            men_ninteen_scr += 1

        newmsg = msg.split()
        for pp in newmsg:
            if pp in newlist:
                men_other_scr += 1

    if msg.startswith('G:'):
        if '19' or '20' in msg:
            girl_ninteen_scr += 2

        newmsg = msg.split()
        for pp in newmsg:
            if pp in newlist:
                girl_other_scr += 2
new_dating_weightage = men_ninteen_scr + girl_ninteen_scr
no_dating = girl_other_scr + men_other_scr
if new_dating_weightage > no_dating:
    print("Date")
else:
    print("No Date")

