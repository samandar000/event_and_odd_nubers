#A four-digit integer is given. Find the number of even digits in it.
var_int=4567
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
x1=var_int%10 
x2=var_int%100-x1
x3=var_int%1000-x2-x1 
x4=var_int%10000-x3-x2-x1
print (x4)