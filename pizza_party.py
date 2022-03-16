#use "while" to calculate the number of the cake pieces that can be cut by the knife
#print the number of knives cut when the number of the cake pieces is bigger than 64
n=1
p=0
while p<64:
 p=(n*n+n)/2
 n=n+1
print ("cutting "+ str(n-1) +" knives is enough for each student")


