import re
import os
os.chdir("C:/Users/86130/IBI1_2021-22/IBI1_2021-22/Practical8")
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
results=open('cut_genes.fa','w')
DNA = file.read()
DNA = ''.join(DNA.split('\n'))
DNA = DNA.lstrip('>')
genes=re.split(r'>',DNA)
output=''
for i in range(len(genes)):
	if re.search(r'GAATTC',genes[i]):
		name=str(re.findall(r'gene:(.+?)\s',genes[i]))
		x=str(re.findall(r'](.+)',genes[i]))
		x=x.strip("[']")
		y=len(x)
		output=output+'>'+name+str(y)+'\n'+x+'\n'
results.write(output)
file.close()
results.close()