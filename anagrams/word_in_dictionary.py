tt = ['bakj','call','hello','grey','callme','callok','callon','zzzzz','cbjkoj']  #[123 , 221 ,311,.... ]
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
   if jj==1 or jj==2 or jj==3: #a,b,c
     jj=2
     #print("hi")
   elif jj==4 or jj==5 or jj==6 : #d,e,f
     jj=3
   elif jj==7 or jj==8 or jj==9 : #g,h,i
     jj=4
   elif jj==10 or jj==11 or jj==12: #j,k,l
     jj=5
   elif jj==13 or jj==14 or jj==15: #m,n,o
     jj=6
   elif jj==16 or jj==17 or jj==18 or jj==19: #p,q,r,s
     jj=7   
   elif jj==20 or jj==21 or jj==22 : #t,u,v
     jj=8
   elif jj==23 or jj==24 or jj==25 or jj==26: #w,x,y,z
     jj=9
   sum = (sum*10 + jj)
   su =sum%13
  dic.append(su)     
  dup.append(sum)
  x = x+1
  y = dic[:]  
#nm = int()
nm = input()
#num =int(nm)
nm = int(nm)%13
dic = [int(x) for x in dic]
#print (dic)
f=0
#print(nm)
while f<len(dic):
  g = dic[f]
  if(g == nm):
    final.append(f)
  f=f+1
final = [int(x) for x in final]
dup = [int(x) for x in dup]
for i in final:
  print(tt[i])

#print(final)




