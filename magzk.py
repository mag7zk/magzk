import cmath
v = 21
u = 33 
x = v + u
y = v / u
print("v + u = ",x)
z = complex(v,u);
print ("The phase of complex number is : ",end="")
print (cmath.phase(z))
print ("Sqrt(z): ",end="")
print (cmath.sqrt(z))
# using the exponentiation operator
ex = v ** u
#Modulus: returns the remainder when the first operand is divided by the second
mod =x % y



val1 = 3
val2 = 2
 
# using the floor division
res = val1 // val2
print(res)
res = val1 % val2
print(res)

if (v > 10): 
    print("v is larger than 10") 
print("I am not in if")

#find the arc cosine of a complex number
print (cmath.acos(2+3j))
