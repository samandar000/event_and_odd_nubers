#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
#Print the number of even digits in the variable "var_int".
import numbers


var_int=4567
x1=var_int%10 
x2=var_int//10%10
x3=var_int//100%10 
x4=var_int//1000%10
s=x1+x2+x3+x4
print ()