#Question2
#Estimating the mean, assigning the error and calculating typical fluctuation about mean.
import matplotlib.pyplot as plt
import numpy as np
import math
#import data from given file
input = open('pandas.txt', 'r')
#Create an array to store panda weights
pandas = []
#Given 100 pandas, yet the code is general so can use any input file containing any number of pandas
#Number of pandas:
panda_num = 0
for weight in input:
    #Need to convert string to float:
    pandas.append(float(weight))
    #panda counter:
    panda_num = panda_num + 1
#Sum of weights:
weight_sum = 0.0
#Sum of squares of weights:
weight_sqr_sum = 0.0
for panda in pandas:
  weight_sum = weight_sum + panda
  weight_sqr_sum = weight_sqr_sum + (panda**2)

mean_weight = weight_sum/panda_num
#sum of squares of deviations:
sum_dev_sqr = 0.0
for i in range(panda_num):
    sum_dev_sqr = sum_dev_sqr + ((pandas[i]-mean_weight)**2)
#fluctuation about mean:
fluctuation = math.sqrt((1.0/(panda_num-1))*sum_dev_sqr)
#error_assigned = estimated std dev of sample mean
error_assigned = math.sqrt((1.0/(panda_num*(panda_num-1)))*sum_dev_sqr)
#create a scatter plot of the data
plt.figure(1)
plt.hist(pandas, 50, color = 'r')
plt.title("Histogram of panda weights")
plt.xlabel("Weight(kg)")
plt.ylabel("Frequency")
plt.show()
#create an output file to store acquired data
panda_out = open('panda_output.txt', 'w')
print("Mean weight is " + str(mean_weight)+"\n")
panda_out.write("Mean weight is " + str(mean_weight)+"\n")
print("Error assigned is " + str(error_assigned)+"\n")
panda_out.write("Error assigned is " + str(error_assigned)+"\n")
print("Typical fluctuation about mean is " + str(fluctuation)+"\n")
panda_out.write("Typical fluctuation about mean is " + str(fluctuation))
