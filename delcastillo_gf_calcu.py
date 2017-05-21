#Del Castillo, Mary Abigail V.
#2014-23666
#Galois Field Calculator

def pad_poly(poly,len_a,len_b):
	pad = len_a - len_b
	for x in range(pad):
		poly.insert(0,0)
	return poly


def poly_add(a,b):
	result = []
	for x in range(len(a)):
		xor_value = a[x] ^ b[x]
		result.append(xor_value)
	return result

def poly_subtract(a,b):
	result = []
	for x in range(len(a)):
		xor_value = a[x] ^ b[x]
		result.append(xor_value)
	return result

def s_mult(a,b,c):
	a=list(bin(a)[2:])
	b=list(bin(b)[2:])
	a=[int(n) for n in a]
	b=[int(n) for n in b]
	#pad binary representation according to the longest number
	if len(a)>len(b):
		b = pad_poly(b,len(a),len(b))
	else:
		a = pad_poly(a,len(b),len(a))

	temp=[]
	#multiply each element of b to a
	for x in range(len(b)-1,-1,-1):
		prod=[str(b[x]*a[y]) for y in range(len(a))] #temporary storage for current product
		prod.extend("0"*((len(b)-1)-x)) #pad-right depending on which place we are multiplying
		prod=[int(n) for n in prod]
		temp=pad_poly(temp,len(prod),len(temp)) #pad-left temporary depending on the place in preparation for XOR op 
		temp=poly_add(temp,prod) #add temp and the current product

	#mod P(x) as long as the resulting polynomial is longer than P(x)
	temp = int(''.join(map(str,temp)),2)
	temp= list(bin(temp)[2:])
	temp=[int(n) for n in temp]
	temp_c=c
	while(len(temp)>=len(c)):
		temp_c=c
		temp_c.extend("0"*(len(temp)-len(temp_c)))
		temp_c=[int(n) for n in temp_c]
		temp=poly_add(temp,temp_c)
		#pops the zero in front of binary
		temp = int(''.join(map(str,temp)),2)
		temp= list(bin(temp)[2:])
		temp=[int(n) for n in temp]

	return int(''.join(map(str,temp)),2)

def del_zeroes(a):
	new_a=a
	while(new_a[0]==0):
		new_a.pop(0)
	return new_a


def poly_multiply(a,b,c):
	temp=[]
	#multiply each element of b to a
	for x in range(len(b)-1,-1,-1):
		prod=[str(s_mult(a[y],b[x],c)) for y in range(len(a))] #temporary storage for current product
		prod.extend("0"*((len(b)-1)-x)) #pad-right depending on which place we are multiplying
		prod=[int(n) for n in prod]
		temp=pad_poly(temp,len(prod),len(temp)) #pad-left temporary depending on the place in preparation for XOR op 
		temp=poly_add(temp,prod) #add temp and the current product

	#delete leading zeroes
	temp=del_zeroes(temp)

	#may possibility pa ba lumagpas sa P(x)??
	#mod P(x) as long as the resulting polynomial is longer than P(x)
	# temp = int(''.join(map(str,temp)),2)
	# temp= list(bin(temp)[2:])
	# temp=[int(n) for n in temp]
	# temp_c=c
	# while(len(temp)>=len(c)):

	return temp

def poly_divide(a,b):
	result = 0
	'''insert operation here'''
	return result

#User Input
a_input = raw_input("Enter a polynomial separated by spaces: ")
b_input = raw_input("Enter a polynomial separated by spaces: ")
c_input = raw_input("Enter a polynomial separated by spaces: ")
operation = 0
while(operation<1 or operation>4):
	print "Choose an operation you want to perform:"
	print "1. A(x) + B(x)"
	print "2. A(x) - B(x)"
	print "3. A(x) x B(x)"
	print "4. A(x) / B(x)"
	operation = input("Enter the number of your choice: ")

#Main Program
#preprocess input
a_input = [int(n) for n in a_input.split()]
b_input = [int(n) for n in b_input.split()]
c_input = [int(n) for n in c_input.split()]
if len(a_input)>len(b_input):
	b_input = pad_poly(b_input,len(a_input),len(b_input))
else:
	a_input = pad_poly(a_input,len(b_input),len(a_input))

#operations
result = 0
if operation == 1:
	result = poly_add(a_input,b_input)

elif operation == 2:
	result = poly_subtract(a_input,b_input)

elif operation == 3:
	result = poly_multiply(a_input,b_input,c_input)

elif operation == 4:
	result = poly_divide(a_input,b_input)

#Printing result
print a_input
print b_input
print "The result of the operation gives us", result