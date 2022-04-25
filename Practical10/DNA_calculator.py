def calculator(DNA):
	DNA=DNA.upper()
	n=0
	m=0
	p=0
	for i in range(0,len(DNA)):
		if DNA[i] == 'A':
			n=n+1
		if DNA[i] == 'C':
			m=m+1
		if DNA[i] == 'G':
			p=p+1
	x=len(DNA)
	a=n/x
	c=m/x
	g=p/x
	t=1-a-c-g
	print('In this DNA sequence, the ratio of A is'+ str(a))
	print('In this DNA sequence, the ratio of C is'+ str(c))
	print('In this DNA sequence, the ratio of G is'+ str(g))
	print('In this DNA sequence, the ratio of T is'+ str(t))
DNA='agtcAGTCCGTAGCTagtc'
calculator(DNA)
DNA=input("Please enter the DNA sequence:")
calculator(DNA)