n=1
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
for i in range(len(seq)):
	if seq[i:i+6] == 'GAATTC':
		n=n+1
print (n)