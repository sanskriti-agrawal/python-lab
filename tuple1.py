n=int(input())
t=()
for i in range(n):
	d=input()
	if d.isalpha():
		t +=(d,)
	else:
		t +=(eval(d),)
print(t)
