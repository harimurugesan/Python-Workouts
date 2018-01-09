import random
heads = 0
tails = 0
for i in range(1, 201):
    flip = random.randint(0, 1)
    if flip == 0:
        heads += 1
    else:
        tails += 1
print("heads count = {0}".format(heads))
print("tails count= {0}".format(tails))
 