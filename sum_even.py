#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".

var_int=4561
sum_juft=0
x1=var_int%10 
x2=var_int//10%10
x3=var_int//100%10 
x4=var_int//1000%10

s=(x1%2)+(x2%2)+(x3%2)+(x4%2)
print(x1)