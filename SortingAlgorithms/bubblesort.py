# bubblesort O(n^2) : comparisons(n) = n (n - 1) / 2 
def bubblesort(n):
	l = len(n)
	for i in range(l - 1):
		for j in range(l - i - 1):
			if n[j] > n[j + 1]:
				n[j], n[j + 1] = n[j + 1], n[j]
	return n
