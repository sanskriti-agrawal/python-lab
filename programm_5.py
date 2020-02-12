lst=list(map(int,input().split()))
d=[ ]
for i in lst:
	if i not in d:
		d.append(i)
print(*d,sep='*')
