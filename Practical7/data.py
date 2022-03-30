import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data = pd.read_csv("full_data.csv")
#Look at the first five rows in the data table.
print (covid_data.head(5))
#View the basic information in the data table.
print (covid_data.info())
print (covid_data.describe())
#This shows you what's in the first row,second column.
print (covid_data.iloc[0,1])
print (covid_data.iloc[2,0:5])
#":" represents all rows or columns.
print (covid_data.iloc[0:2,:])
#The second colon represents the interval taken
print (covid_data.iloc[0:10:2,0:5])
#The answer about "How would you show the first and third columns rows 10~20 (inclusive)?
print (covid_data.iloc[9:20,0:4:2])
#Use Boolean to access entries
my_columns = [True, True, False, True, False, False]
print (covid_data.iloc[0:3,my_columns])
#Use column names to locate items
print (covid_data.loc[2:4,"date"])
print (covid_data.loc[0:81,"total_cases"])
#find the required in the row
my_rows=[]
for i in range(0,len(covid_data)):
 if covid_data.loc[i,"location"] == "Afghanistan":
  my_rows.append(True)
 else:
  my_rows.append(False)
print (covid_data.loc[my_rows,"total_cases"])
#store data from China
china_new_data=covid_data.loc[covid_data['location']=='China',['date','new_cases','new_deaths']]
print (china_new_data)
#calculated the mean of new cases and new deaths
new_cases_mean=np.mean(china_new_data["new_cases"])
print (new_cases_mean)
new_deaths_mean=np.mean(china_new_data["new_deaths"])
print (new_deaths_mean)
#calculate the death rate
death_rate=new_deaths_mean/new_cases_mean
print (death_rate)
#plot the new cases and new deaths in China as a box plot
l1=china_new_data["new_cases"]
l2=china_new_data["new_deaths"]
plt.boxplot([l1,l2],labels=['new_cases','new_deaths'],showfliers=False)
plt.title("Box chart of cases and deaths in China")
plt.ylabel("number")
plt.show()
#plot the data over time
china_dates=china_new_data.iloc[:,0]
china_new_cases=china_new_data.iloc[:,1]
china_new_deaths=china_new_data.iloc[:,2]
plt.plot(china_dates,china_new_cases,'bo',china_dates,china_new_deaths,'r+')
plt.title("plot of China new cases over time")
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.ylabel("number")
plt.show()
#answer about the question"– Are there places in the World where there have not yet been more than 10 total infections(as of 31 March)? If so, where are they?
places=covid_data.loc[covid_data['date']=='2020/3/31',['location','total_cases']]
print (places.loc[places['total_cases']<=10,'location'])

