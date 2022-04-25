def chocolate_bar(total_number,prize):
	n=total_number//prize
	m=total_number-n*prize
	return('You can buy '+ str(n) + ' chocolate bars. And there are '+str(m) +' dollars left.')
#example
print(chocolate_bar(100,7))