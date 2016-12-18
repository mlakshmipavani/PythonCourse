tt = ['abc','bba','caa','dtd','ttt']  #[123 , 221 ,311,.... ]
t = list(tt)
sum =0
x=1
dic =[]
dup=[]
final =[]
for i in t:
  sum =0 
  for j in i:
   jj = ord(j) - 96
   sum = (sum*10 + jj)
   su =sum%13
  dic.append(su)     
  dup.append(sum)
  x = x+1
  y = dic[:]  
#nm = int()
nm = input()
num =int(nm)
nm = int(nm)%13
dic = [int(x) for x in dic]
print (dic)
f=0
print(nm)
while f<len(dic):
  g = dic[f]
  if(g == nm):
    final.append(f)
  f=f+1
#print(dup)
#print(final)
#print(num)
final = [int(x) for x in final]
dup = [int(x) for x in dup]
for i in final:
  if dup[i] == num:
   print(tt[i])












