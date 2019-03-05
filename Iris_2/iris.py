# Load libraries

import csv
import random
import math
import matplotlib

import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class IrisData():
 def __init__(self, filename):
  with open(filename, "r") as f_input:
   csv_input = csv.reader(f_input)
   self.details = list(csv_input)

 def get_col_row(self, col, row):
  return self.details[row-1][col-1] 
  # Python index starts from 0 so we have to substract by 1

data = IrisData("iris.csv")


sepall=[]
sepalw=[]
petall=[]
petalw=[]
category1=[]
category2=[]


for x in range(0,150):
	sepall.append(float(data.get_col_row(1,x)))
	sepalw.append(float(data.get_col_row(2,x)))
	petall.append(float(data.get_col_row(3,x)))
	petalw.append(float(data.get_col_row(4,x)))

	category1.append(float(data.get_col_row(6,x)))
	category2.append(float(data.get_col_row(7,x)))


the1=random.uniform(0,1)
the2=random.uniform(0,1)
the3=random.uniform(0,1)
the4=random.uniform(0,1)
bias1=random.uniform(0,1)

the5=random.uniform(0,1)
the6=random.uniform(0,1)
the7=random.uniform(0,1)
the8=random.uniform(0,1)
bias2=random.uniform(0,1)

target1=0
target2=0
sigmoid1=0
sigmoid2=0
eror1=0
eror2=0
lrate=0.1
totalerror1=0
totalerror2=0
accurate=0



for y in range (0,100):
	print('epoch-',y)
	
	for x in range (0,150):
		target1=float(the1*sepall[x]+the2*sepalw[x]+the3*petall[x]+the4*petalw[x]+bias1)
		target2=float(the5*sepall[x]+the6*sepalw[x]+the7*petall[x]+the8*petalw[x]+bias2)

		sigmoid1=float(1/(1+math.exp(-target1)))
		sigmoid2=float(1/(1+math.exp(-target2)))


		if sigmoid1>0.5:
			prediction1=1.0
		else:
			prediction1=0.0

		if sigmoid2>0.5:
			prediction2=1.0
		else:
			prediction2=0.0
			
		if (category1[x] == prediction1 and category2[x] == prediction2):
			accurate=accurate+1
		
		
		eror1=float((abs(sigmoid1-category1[x]))**2)
		eror2=float((abs(sigmoid2-category2[x]))**2)

		totalerror1=totalerror1+eror1
		totalerror2=totalerror2+eror2

		dthe1=2*(sigmoid1-category1[x])*(1-sigmoid1)*sigmoid1*sepall[x]
		dthe2=2*(sigmoid1-category1[x])*(1-sigmoid1)*sigmoid1*sepalw[x]
		dthe3=2*(sigmoid1-category1[x])*(1-sigmoid1)*sigmoid1*petall[x]
		dthe4=2*(sigmoid1-category1[x])*(1-sigmoid1)*sigmoid1*petalw[x]
		dbias1=2*(sigmoid1-category1[x])*(1-sigmoid1)*sigmoid1*1
		
		dthe5=2*(sigmoid2-category2[x])*(1-sigmoid2)*sigmoid2*sepall[x]
		dthe6=2*(sigmoid2-category2[x])*(1-sigmoid2)*sigmoid2*sepalw[x]
		dthe7=2*(sigmoid2-category2[x])*(1-sigmoid2)*sigmoid2*petall[x]
		dthe8=2*(sigmoid2-category2[x])*(1-sigmoid2)*sigmoid2*petalw[x]
		dbias2=2*(sigmoid2-category2[x])*(1-sigmoid2)*sigmoid2*1

		the1=the1-lrate*dthe1
		the2=the2-lrate*dthe2
		the3=the3-lrate*dthe3
		the4=the4-lrate*dthe4
		bias1=bias1-lrate*bias1

		the5=the5-lrate*dthe5
		the6=the6-lrate*dthe6
		the7=the7-lrate*dthe7
		the8=the8-lrate*dthe8
		bias2=bias2-lrate*bias2



	erorav1=totalerror1/150
	eroeav2=totalerror2/150
	accuav=accurate/150
	totalerror1=0
	totalerror2=0
	accurate=0

	print(eroeav2)
	print(erorav1)
	print(accuav)

	y=y+1

	plt.figure('Eror1')
	plt.plot(y,erorav1,'-o')
	plt.figure('Eror2')
	plt.plot(y,eroeav2,'-o')
	plt.figure('Accurate')
	plt.plot(y,accuav,'-o')

	
	
plt.show()



