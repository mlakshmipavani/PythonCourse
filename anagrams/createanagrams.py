def toString(List):
	return ''.join(List)
def swap(a,i,j):
  t = a[i]
  a[i] = a[j]
  a[j] = t
  return a 
def permute(a, l, r):
	if l==r:
		print (toString(a));
	else:
		for i in range(l,r+1):
			swap(a,l,i)
			permute(a, l+1, r)
			swap(a,l,i)
			
string = input()
#a = input()
n = len(string)
#n = len(a)
a = list(string)
permute(a, 0, n-1)
