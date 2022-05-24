marks=[45,36,86,57,53,92,65,45]
#sort his grades
sorted(marks)
#print the marks
marks = sorted(marks)
print (marks)
#show the box plots
import matplotlib.pyplot as plt
import numpy as np
plt.boxplot(marks,
            labels= ["Rob"],
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
            )
plt.title("IBI scores")
plt.ylabel('scores')
plt.show()
#calculate average score
avr=(45+36+86+57+53+92+65+45)/8
print ("Rob's average score is " + str(avr))
if avr >= 60:
 print ("Rob's average score is higher than 60.")
else:
 print ("Rob's average score is lower than 60.")
