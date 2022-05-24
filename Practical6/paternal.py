import numpy as np
import matplotlib.pyplot as plt
#write the father's age in an array
paternal_age=[30,35,40,45,50,55,60,65,70,75]
#write the risk of CHD in an array
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
#make scatter chart
plt.scatter(paternal_age,chd,marker='d')
#define the title
plt.title('parental age vs offspring health') 
#define the xlable
plt.xlabel('parental age') 
#define the ylable
plt.ylabel('offspring health') 
#let the scatter chart show
plt.show()
#make a dictionary
relative = {30:1.03,35:1.07,40:1.11,45:1.17,50:1.23,55:1.32,60:1.42,65:1.55,70:1.72,75:1.94}
print (relative)
#input paternal age
age= input ("paternal age: ")
print ("When father's age is " + str(age) + ", " + "the risk of CHD is" + str(relative[a]))
