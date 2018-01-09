a = input()
b = input().split()
c = int(input())
d= []
for i in range(c):
	d.append(input())
for dd in d:
	if dd in b:
		print(b.index(dd)+1)