#Del Castillo, Mary Abigail V.
#2014-23666
#Galois Field Calculator

def pad_poly(poly,len_a,len_b):
	pad = len_a - len_b
	for x in range(pad):
		poly.insert(0,0)
	return poly

def pad_poly_str(poly,len_a,len_b):
	pad = len_a - len_b
	for x in range(pad):
		poly.insert(0," ")
	return poly

def del_zeroes(a):
	new_a=a
	if (len(a)>0):
		while(new_a[0]==0):
			new_a.pop(0)
	return new_a

def print_output(poly,a):
	ctr = len(a)-1
	print poly,
	for x in range(0,len(a)):
		if (x == len(a)-1):
			print str(a[x])
		else:
			print str(a[x]) + "x^" + str(ctr) + " +",
		ctr-=1

def print_terms(a):
	for x in range(0,len(a)):
		if (x == len(a)-1):
			print str(a[x])
		else:
			print str(a[x]),

def input_check(a):
	b = a.split()
	for x in b:
		if (x.isdigit()==False):
			return 0
	return 1

#Polynomial Operations
def poly_add2(a,b):
	result = []
	print "Now, let's perform bitwise xor operation for every term in A(x) and B(x)."
	for x in range(len(a)):
		xor_value = a[x] ^ b[x]
		print "if we perform",str(a[x]),"xor",str(b[x]),", we get",str(xor_value)
		result.append(xor_value)

	print "Therefore, after joining all the individual xor results, we get,"
	print_terms(result)
	return result

def poly_subtract2(a,b):
	result = []
	print "Now, let's perform bitwise xor operation for every term in A(x) and B(x)."
	for x in range(len(a)):
		xor_value = a[x] ^ b[x]
		print "if we perform",str(a[x]),"xor",str(b[x]),", we get",str(xor_value)
		result.append(xor_value)
	print "Therefore, after joining all the individual xor results, we get,"
	print_terms(result)
	return result

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
	#delete leading zeroes
	temp = int(''.join(map(str,temp)),2)
	temp= list(bin(temp)[2:])
	temp=[int(n) for n in temp]

	temp_c=[int(n) for n in c]
	len_c = len(c)
	while(len(temp)>=len_c):
		temp_c=[int(n) for n in c]
		temp_c.extend("0"*(len(temp)-len(temp_c)))
		temp_c=[int(n) for n in temp_c]
		temp=poly_add(temp,temp_c)
		#delete leading zeroes
		temp = int(''.join(map(str,temp)),2)
		temp= list(bin(temp)[2:])
		temp=[int(n) for n in temp]
	
	return int(''.join(map(str,temp)),2)

def poly_multiply(a,b,c):
	temp=[]
	#multiply each element of b to a
	len_ba=len(b)+len(a)
	temp_c=[int(n) for n in c]
	for x in range(len(b)-1,-1,-1):
		temp_c=[int(n) for n in c]
		prod=[str(s_mult(a[y],b[x],temp_c)) for y in range(len(a))] #temporary storage for current product
		prod.extend("0"*((len(b)-1)-x)) #pad-right depending on which place we are multiplying
		prod=[int(n) for n in prod]
		temp2 = [str(n) for n in prod]
		temp2=pad_poly_str(temp2,len_ba,len(temp2))
		print_terms(temp2)
		temp=pad_poly(temp,len(prod),len(temp)) #pad-left temporary depending on the place in preparation for XOR op 
		
		temp=poly_add(temp,prod) #add temp and the current product
	
	print "---------------------------"
	temp3=[str(n) for n in temp]
	temp3=pad_poly_str(temp3,len_ba,len(temp3))
	print_terms(temp3)
	#delete leading zeroes
	temp=del_zeroes(temp)

	#mod P(x) as long as the resulting polynomial is longer than P(x)
	# temp_c=c
	# len_c = len(c)
	# while(len(temp)>=len_c):
	# 	print len(temp), len_c
	# 	temp_c=c
	# 	temp_c.extend("0"*(len(temp)-len(temp_c)))
	# 	temp_c=[int(n) for n in temp_c]
	# 	temp=poly_add(temp,temp_c)
	# 	print temp
	# 	#delete leading zeroes
	# 	temp=del_zeroes(temp)

	return temp

def div_mult(ctr,a,c):
		prod=[str(s_mult(a[y],ctr,c)) for y in range(len(a))] #temporary storage for current product
		prod=[int(n) for n in prod]
		return prod

def poly_divide(a,b,c):
	result2=[]
	result=[]
	ctr = 1
	ctr2 = len(a)-len(b)
	x = div_mult(ctr,b,c)
	len_b = len(b)
	len_a = len(a)
	for n in range(0,len(a)):
		if (n == len(a)-1):
			print str(a[n]),"= A"
		else:
			print str(a[n]),

	while (len(a)>=len_b):
		while(a[0]!=x[0]):
			ctr+=1
			x = div_mult(ctr,b,c)

		result.append(ctr)
		if (len(a) < len(b)):
			return result
		else: 
			len_x = len(x)
			x.extend("0"*((len(a))-len_x))
			x=[int(n) for n in x]

			#printing solution
			temp1=[str(n) for n in x]
			temp1=pad_poly_str(temp1,len_a,len(temp1))
			for n in range(0,len(temp1)):
				if (n == len(temp1)-1):
					print str(temp1[n])+" = B x "+str(ctr)+"x^"+str(ctr2)
				else:
					print str(temp1[n]),
			print "--------------------"

			a = poly_add(a,x)
			temp2=[str(n) for n in a]
			temp2=pad_poly_str(temp2,len_a,len(temp2))
			print_terms(temp2)
			a = del_zeroes(a)
			
		ctr=1
		ctr2-=1
	result2.append(result)
	result2.append(a)
	print "result =",
	print_terms(result2[0])
	print "remainder =",
	print_terms(result2[1])
	return result2

'''Main Program'''
#User Input
a_input = raw_input("Enter A(x) separated by spaces: ")
while (input_check(a_input)!=1):
	print "You have entered a non-digit in the polynomial."
	a_input = raw_input("Enter A(x) separated by spaces: ")
a_input = [int(n) for n in a_input.split()]
a_div = [int(n) for n in a_input]

b_input = raw_input("Enter B(x) separated by spaces: ")
while (input_check(b_input)!=1):
	print "You have entered a non-digit in the polynomial."
	b_input = raw_input("Enter B(x) separated by spaces: ")
b_input = [int(n) for n in b_input.split()]
b_div = [int(n) for n in b_input]

c_input = raw_input("Enter P(x) separated by spaces: ")
while (input_check(c_input)!=1):
	print "You have entered a non-digit in the polynomial."
	c_input = raw_input("Enter P(x) separated by spaces: ")
c_input = [int(n) for n in c_input.split()]

#preprocess input
if len(a_input)>len(b_input):
	b_input = pad_poly(b_input,len(a_input),len(b_input))
else:
	a_input = pad_poly(a_input,len(b_input),len(a_input))

max_value=2**(len(c_input)-1)
for x in a_input:
	if (x >= max_value):
		f=raw_input("One of the coefficients is greater than the limit set by the P(x)")
		exit()

for x in b_input:
	if (x >= max_value):
		f=raw_input("One of the coefficients is greater than the limit set by the P(x)")
		exit()

operation = 0
while(operation<1 or operation>4):
	print "Choose an operation you want to perform:"
	print "1. A(x) + B(x)"
	print "2. A(x) - B(x)"
	print "3. A(x) x B(x)"
	print "4. A(x) / B(x)"
	operation = input("Enter the number of your choice: ")

#operations
result = 0
len_ba = len(b_input)+len(a_input)
if operation == 1:
	print "\nDetailed solution for A(x) + B(x) (addition):\n"
	print "We can pad the terms to have equal number of terms."
	print "After padding, we have"
	print "A(x) =",
	print_terms(a_input)
	print "B(x) =",
	print_terms(b_input)
	print "\n"
	result = poly_add2(a_input,b_input)
	print "\nOutput:"
	print_output("A(x) =",a_input)
	print_output("B(x) =",b_input)
	print_output("A(x) + B(x) =",result)

elif operation == 2:
	print "\nDetailed solution for A(x) - B(x) (subtraction):\n"
	print "We can pad the terms to have equal number of terms."
	print "After padding, we have"
	print "A(x) =",
	print_terms(a_input)
	print "B(x) =",
	print_terms(b_input)
	print "\n"
	result = poly_subtract2(a_input,b_input)
	print "\nOutput:"
	print_output("A(x) =",a_input)
	print_output("B(x) =",b_input)
	print_output("A(x) - B(x) =",result)

elif operation == 3:
	print "\nDetailed solution for A(x) x B(x) (multiplication):\n"
	print "1) Using the Galois Field GF(2^" + str(len(c_input)-1)+") based on the primitive P(x) =",
	print_terms(c_input)
	print "2) Multiply each term by their binary values (with modulo 2 addition) and then the result is computed modulo P(x)"
	print "3) After multiplying each term of B(x) with A(x), perform bitwise xor on those terms."
	print "4) For the solution itself, please look at the following: "
	temp=[str(n) for n in a_input]
	temp=pad_poly_str(temp,len_ba,len(temp))
	print_terms(temp)
	temp2=[str(n) for n in b_input]
	temp2=pad_poly_str(temp2,len_ba,len(temp2))
	print_terms(temp2)
	print "---------------------------"
	result = poly_multiply(a_input,b_input,c_input)
	print "\nOutput:"
	print_output("A(x) =",a_input)
	print_output("B(x) =",b_input)
	print_output("A(x) x B(x) =",result)

elif operation == 4:
	print "\nDetailed solution for A(x) / B(x) (division):\n"
	print "1) Try to multiply integers to B(x) starting from 1 until the first term is equal to the dividend's first term."
	print "2) Perform xor on the dividend and the product of the integer and B(x)."
	print "3) Divide this result to B(x) again and repeat the process from step 1 until the number of terms of the dividend is less than the length of B(x)."
	print "4) For a detailed solution, please look at the following."
	result = poly_divide(a_div,b_div,c_input)
	print "\nOutput:"
	print_output("A(x) =",a_input)
	print_output("B(x) =",b_input)
	print_output("A(x) / B(x) =",result[0])
	print_output("remainder =",result[1])
last = raw_input("Press enter to exit the program")
