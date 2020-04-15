#importing the necessary libraries
import math
import matplotlib.pyplot as plt 

#Allow the user to enter the value of x to be computed!(uncomment only to find single value of x)
#x = input("Value of x : ")
#x = float(x)

#kth term of the series to be solved
k = 0
k = int(k)

#The number of time the recursive function is to be repeated! improves the accuracy!.
#(uncomment only to find single value of x)
#i = input("Accuracy :  ")
#i = int(i)

#List to hold the computed value. (using list here help to organize the data and to better visualize it.)
recursive_function_element = []
series_function_element = []

#The change in recursive function is handeled by this values.
f1 = 2
f2 = 3

#min and max values of x for ploting.
min_x = input("From : ")
max_x = input("To : ")
plot_accuracy = input("Acurracy of the plot : ")
plot_accuracy_1 = input("Acurracy of the plot : ")
plot_accuracy_2 = input("Acurracy of the plot : ")
plot_accuracy_3 = input("Acurracy of the plot : ")
plot_accuracy_4 = input("Acurracy of the plot : ")
min_x = int(min_x)
max_x = int(max_x)
plot_accuracy = int(plot_accuracy)
plot_accuracy_1 = int(plot_accuracy_1)
plot_accuracy_2 = int(plot_accuracy_2)
plot_accuracy_3 = int(plot_accuracy_3)
plot_accuracy_4 = int(plot_accuracy_4)

#Plot data store
plot_X = []
plot_Y = []
plot_X_1 = []
plot_Y_1 = []
plot_X_2 = []
plot_Y_2 = []
plot_X_3 = []
plot_Y_3 = []
plot_X_4 = []
plot_Y_4 = []


#This function only deals with the situation when k = 0.
def initial_function(k,x):
	a = pow(x,((2*k)+1))
	b = pow(-1,k)
	c = pow(2,((2*k)+1))
	d = ((2*k)+1)
	funu = b * a
	fund = d * c
	funf = funu/fund
	return funf

#This function is the function which has a general pattern of repitition.
def recursive_function(x,f1,f2):
	a = pow(x,2)
	b = f1 * f2
	c = pow(2,2)
	funu = a * (-1)
	fund = b * c
	funf = funu/fund
	return funf

#These are for loops are the ones that compute and puts the value into the list
def final_function(i,x,f1,f2,k):
	for y in range(i):	
		e = recursive_function(float(x), int(f1), int(f2))
		f1 = f1 + 2
		f2 = f2 + 2
		recursive_function_element.append(e)

	a_0 = initial_function(k,x)
	series_function_element.append(a_0)
	for v in range(1,i):
		series_function_element.append(recursive_function_element[v-1] * series_function_element[v-1])
	return sum(series_function_element)

#Loop the final_function for diffrent values with given accuracy to be stored.
for u in range(min_x,max_x):
	#adds the x cordinate for plotting which are the x value results to the list plot_Y
	plot_Y.append(final_function(plot_accuracy,u,f1,f2,k))
	recursive_function_element.clear()
	series_function_element.clear()
	#adds the y cordinate for plotting which are the x values to the list plot_Y
	plot_X.append(u)
	#adds the x cordinate for plotting which are the x value results to the list plot_Y
	plot_Y_1.append(final_function(plot_accuracy_1,u,f1,f2,k))
	recursive_function_element.clear()
	series_function_element.clear()
	#adds the y cordinate for plotting which are the x values to the list plot_Y
	plot_X_1.append(u)
	#adds the x cordinate for plotting which are the x value results to the list plot_Y
	plot_Y_2.append(final_function(plot_accuracy_2,u,f1,f2,k))
	recursive_function_element.clear()
	series_function_element.clear()
	#adds the y cordinate for plotting which are the x values to the list plot_Y
	plot_X_2.append(u)
	#adds the x cordinate for plotting which are the x value results to the list plot_Y
	plot_Y_3.append(final_function(plot_accuracy_3,u,f1,f2,k))
	recursive_function_element.clear()
	series_function_element.clear()
	#adds the y cordinate for plotting which are the x values to the list plot_Y
	plot_X_3.append(u)
	#adds the x cordinate for plotting which are the x value results to the list plot_Y
	plot_Y_4.append(final_function(plot_accuracy_4,u,f1,f2,k))
	recursive_function_element.clear()
	series_function_element.clear()
	#adds the y cordinate for plotting which are the x values to the list plot_Y
	plot_X_4.append(u)

#plotting handel function
def plot_fun(plot_X,plot_Y):
	print(plot_X)
	print(plot_Y)
	plt.plot(plot_X, plot_Y, label = plot_accuracy) 
	plt.plot(plot_X_1, plot_Y_1, label = plot_accuracy_1) 
	plt.plot(plot_X_2, plot_Y_2, label = plot_accuracy_2) 
	plt.plot(plot_X_3, plot_Y_3, label = plot_accuracy_3) 
	plt.plot(plot_X_4, plot_Y_4, label = plot_accuracy_4) 
	plt.xlabel('x - axis') 
	plt.ylabel('y - axis') 
	plt.title('Graph of the requested interval!') 
	plt.legend() 
	plt.show() 


#List of print statements which outputs the computed value.
#(uncomment only to find single value of x)
#print(final_function(i,x,f1,f2,k))
#print(math.sin(x/2))
plot_fun(plot_X,plot_Y)

