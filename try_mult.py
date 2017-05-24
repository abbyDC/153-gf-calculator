a=6
b=21

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

a=list(bin(a)[2:])
b=list(bin(b)[2:])
a=[int(n) for n in a]
b=[int(n) for n in b]
c=[1,0,1,1,1,1]
#pad-left binary representation according to the longest number
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
len_c=len(c)
while(len(temp)>=len_c):
	temp_c=c
	temp_c.extend("0"*(len(temp)-len(temp_c)))
	temp_c=[int(n) for n in temp_c]
	temp=poly_add(temp,temp_c)
	#pops the zero in front of binary
	temp = int(''.join(map(str,temp)),2)
	temp= list(bin(temp)[2:])
	temp=[int(n) for n in temp]

print int(''.join(map(str,temp)),2)

