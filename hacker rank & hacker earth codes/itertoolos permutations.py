from itertools import permutations
a = raw_input().split()
k = int(a[1])
st = a[0]
re = (permutations(st,k))
re = sorted(re)
for i in re:
      print  "".join(i)
