#use "while" to calculate the number of the cake pieces that can be cut by the knife
#print the number of knives cut when the number of the cake pieces is bigger than 64
n=1
p=0
#Start with one cut
#The formula can be used to calculate the number of cakes.
#If the number of cakes is less than 64, increase the number of knives until the number of cakes is greater than 64
while p<64:
 p=(n*n+n)/2
 n=n+1
print ("cutting "+ str(n-1) +" knives is enough for each student")


