

def pad_poly(poly,len_a,len_b):
	pad = len_a - len_b
	for x in range(pad):
		poly.insert(0,0)
	return poly



def del_zeroes(a):
	new_a=a
	if (len(a)>0):
		while(new_a[0]==0):
			new_a.pop(0)
	return new_a

def s_div(s,delta,r):
	r.extend("0"*delta)
	x1 = r
	s_new = []
	#pad binary representation according to the longest number
	if len(x1)>len(s):
		s = pad_poly(s,len(x1),len(s))
	else:
		x1 = pad_poly(x1,len(s),len(x1))
	x1 = [int(n) for n in x1]
	s = [int(n) for n in s]
	for x in range(len(x1)):
		xor_value = s[x] ^ x1[x]
		s_new.append(xor_value)
	s_new = del_zeroes(s_new)
	return s_new

#division
c=[1,0,0,0,1,1,0,1,1]
b=[1,1,0,0,1,1,0,0]
s = c
r = b
v = [0]
u = [1]
while (len(r)!=0):
	delta= len(s) - len(r)
	if (delta < 0):
		s,r = r, s
		v,u = u,v
		delta = -delta

	s=s_div(s,delta,r)
	v=s_div(v,delta,u)
print u