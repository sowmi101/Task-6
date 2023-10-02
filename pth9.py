lis=[1,4,10,12,11,31,77,67]

prime=[]

for i in lis:

    c=0

    for j in range(1,i):

       if i%j==0:

          c+=1

    if c==1:

       prime.append(i)

print(prime)