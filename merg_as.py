def M(a, b, c, d):
	n1 = c - b + 1
	n2 = d - c
	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = a[b + i]

	for j in range(0, n2):
		R[j] = a[c + 1 + j]
	i = 0	 
	j = 0	 
	k = b

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			a[k] = L[i]
			i += 1
		else:
			a[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		a[k] = L[i]
		i += 1
		k += 1

	
	while j < n2:
		a[k] = R[j]
		j += 1
		k += 1

def M_S(a, l, r):
	if l < r:

		
		m = l+(r-l)//2

		
		M_S(a, l, m)
		M_S(a, m+1, r)
		M(a, l, m, r)



a = [85, 4, 32, 150, 79, 200]
n = len(a)
for i in range(n):
	print("%d" % a[i],end=" ")
print(" ")
M_S(a, 0, n-1)
for i in range(n):
	print("%d" % a[i],end=" ")


