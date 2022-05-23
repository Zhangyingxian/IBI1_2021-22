from xml.dom.minidom import parse 
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
print ('There are '+str(len(terms)) + ' of tems in GO.')

dic={}
for term in terms:
	is_aes=[]
	for i in term.getElementsByTagName('is_a'):
		is_aes.append(i.childNodes[0].data)
	ids=term.getElementsByTagName('id')[0].childNodes[0].data
	for is_a in is_aes:
		if is_a in dic:
			dic[is_a].append(ids)
		else:
			dic[is_a]=[ids]

def number(list0):
	for i in list0:
		if i in list0:
			if i not in list1:
				list1.append(i)
				if i in dic:
					number(dic[i])
	return len(list1)

alllist=[]
translationlist=[]

for term in terms:
	childnodes=0
	list1=[]
	ids=term.getElementsByTagName('id')[0].childNodes[0].data
	if ids in dic:
		childnodes=number(dic[ids])
	alllist.append(childnodes)
	if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data:
		translationlist.append(childnodes)

plt.boxplot(alllist,labels=['GO'])
plt.title('childNodes distribution diagram of term')
plt.ylabel('the number of childNodes')
plt.show()

plt.boxplot(translationlist,labels=['translation GO'])
plt.title('childNodes distribution diagram of term related to translation')
plt.ylabel('the number of childNodes')
plt.show()

aver1=sum(alllist)/len(alllist)
aver2=sum(translationlist)/len(translationlist)
if aver1>aver2:
	print("The terms related to translation have a smaller number of childNodes than the overall Gene Ontology on average.")
else:
	print("The terms related to translation have a greater number of childNodes than the overall Gene Ontology on average.")