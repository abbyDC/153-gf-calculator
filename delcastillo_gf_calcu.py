#Del Castillo, Mary Abigail V.
#2014-23666
#Galois Field Calculator

def binary_converter(original):
	converted=0
	return converted

def poly_add(a,b):
	result = 0
	'''insert operation here'''
	return result

def poly_subtract(a,b):
	result = 0
	'''insert operation here'''
	return result

def poly_multiply(a,b):
	result = 0
	'''insert operation here'''
	return result

def poly_divide(a,b):
	result = 0
	'''insert operation here'''
	return result

#User Input
a_input = input("Enter a polynomial separated by spaces: ")
b_input = input("Enter a polynomial separated by spaces: ")
operation = 0
while(operation<1 and operation>4):
	print "Choose an operation you want to perform:"
	print "1. A(x) + B(x)"
	print "2. A(x) - B(x)"
	print "3. A(x) x B(x)"
	print "4. A(x) / B(x)"
	operation = input("Enter the number of your choice: ")

#Main Program
result = 0
if operation == 1:
	result = poly_add(a_input,b_input)

elif operation == 2:
	result = poly_subtract(a_input,b_input)

elif operation == 3:
	result = poly_multiply(a_input,b_input)

elif operation == 4:
	result = poly_divide(a_input,b_input)

#Printing result
print a_input
print b_input
print "The result of the operation gives us", result