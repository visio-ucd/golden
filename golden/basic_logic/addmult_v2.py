# File: bfloat16_addmult.cpp
# Name: UCD-Visio
# 		
# Description: Python libary for bfloat16, a truncated version of IEEE 754 float32.


#----------------------------------------------------------------------------------------------	
#Imports
#----------------------------------------------------------------------------------------------
from numpy import float32
from numpy import random
import struct
import sys

#----------------------------------------------------------------------------------------------	
#Class Declaration
#----------------------------------------------------------------------------------------------
#Depricated. Use bfloat16 instead.
class bfloat:
	def __init__(self, s, e = '', m = ''):
		if len(s) + len(e) + len(m) != 16:
			print("Argument isn't 16bits:" , s, e, m)
		else:
			#Unparsed string is provided 
			if s and e == '' and m == '':
				self.sign = s[0]
				self.exp = s[1:9]
				self.man = s[9:]
			#Parse string is provided
			else:
				self.sign = s
				self.exp = e
				self.man  = m

			self.value = ''

			#TODO: add -inf, -NaN, -zero
			if self.exp == '11111111':
				if int(self.man,2) == 0:
					self.value = 'inf'
				else:
					self.value = 'NaN'

			if int(self.exp ,2) + int(self.man ,2) == 0:
				self.value = 'zero'
	#end __init___() 
	
	#returns an array of parsed binary of the bfloat32
	def bin(self):
		return (self.sign, self.exp, self.man)
	
	
	#returns the decimal(numpy float32) value of bfloat16 
	def dec(self):
		exp_mag = int(self.exp,2)
		start = -1
		man_mag = 0.0
		for m in self.man:
			man_mag = man_mag + int(m) * 2 ** (start)
			start = start - 1

		if self.exp == '00000000':
			if self.man == '0000000':
				if(self.sign == '1'):
					return -0.0
				else:
					return 0.0
			else: 
				out = ((-1)**int(self.sign) * 2**(exp_mag - 126) * (man_mag)) 
				return (float32(out))
		elif self.value == 'inf':
			return float(int(self.sign)*'-' +'Inf')
		else:
			out = ((-1)**int(self.sign) * 2**(exp_mag - 127) * (man_mag + 1))
			return (float32(out)) 

	#Operator overloading
	#Only works if a and b are both bfloat objects
	def __add__(self, b):
		return bfloat_add(self, b)
	def __mul__(self, b):
		return bfloat_mult(self, b)

	#Depricated, use bfloat.bin()
	def display_bin(self):
		return (self.sign, self.exp, self.man)

	#Depricated, use bfloat.dec()
	def display_dec(self):
		exp_mag = int(self.exp,2)
		start = -1
		man_mag = 0.0
		for m in self.man:
			man_mag = man_mag + int(m) * 2 ** (start)
			start = start - 1

		if self.exp == '00000000':
			if self.man == '0000000':
				if(self.sign == '1'):
					return -0.0
				else:
					return 0.0
			else: 
				out = ((-1)**int(self.sign) * 2**(exp_mag - 126) * (man_mag)) 
				return (float32(out))
		elif self.value == 'inf':
			return float(int(self.sign)*'-' +'Inf')
		else:
			out = ((-1)**int(self.sign) * 2**(exp_mag - 127) * (man_mag + 1))
			return (float32(out))

#Valid inputs to construct the object:
#	- parsed binary string of (1 bit sign, 8 bit exponent, 7 bit mantissa).
#	- unparsed binary string of (16 bit bfloat16)
#	
#TO convert float32 to bfloat16 use f2bfloat()
class bfloat16:
	def __init__(self, s, e = '', m = ''):
		if len(s) + len(e) + len(m) != 16:
			print("Argument isn't 16bits:" , s, e, m)
		else:
			#Unparsed string is provided 
			if s and e == '' and m == '':
				self.sign = s[0]
				self.exp = s[1:9]
				self.man = s[9:]
			#Parse string is provided
			else:
				self.sign = s
				self.exp = e
				self.man  = m

			self.value = ''

			#TODO: add -inf, -NaN, -zero
			if self.exp == '11111111':
				if int(self.man,2) == 0:
					self.value = 'inf'
				else:
					self.value = 'NaN'

			if int(self.exp ,2) + int(self.man ,2) == 0:
				self.value = 'zero'
	#end __init___() 
	
	#returns an array of parsed binary of the bfloat32
	def bin(self):
		return (self.sign, self.exp, self.man)
	
	
	#returns the decimal(numpy float32) value of bfloat16 
	def dec(self):
		exp_mag = int(self.exp,2)
		start = -1
		man_mag = 0.0
		for m in self.man:
			man_mag = man_mag + int(m) * 2 ** (start)
			start = start - 1

		if self.exp == '00000000':
			if self.man == '0000000':
				if(self.sign == '1'):
					return -0.0
				else:
					return 0.0
			else: 
				out = ((-1)**int(self.sign) * 2**(exp_mag - 126) * (man_mag)) 
				return (float32(out))
		elif self.value == 'inf':
			return float(int(self.sign)*'-' +'Inf')
		else:
			out = ((-1)**int(self.sign) * 2**(exp_mag - 127) * (man_mag + 1))
			return (float32(out)) 

	#Operator overloading
	#Only works if a and b are both bfloat objects
	def __add__(self, b):
		return bfloat_add(self, b)
	def __mul__(self, b):
		return bfloat_mult(self, b)

	#Depricated, use bfloat.bin()
	def display_bin(self):
		return (self.sign, self.exp, self.man)

	#Depricated, use bfloat.dec()
	def display_dec(self):
		exp_mag = int(self.exp,2)
		start = -1
		man_mag = 0.0
		for m in self.man:
			man_mag = man_mag + int(m) * 2 ** (start)
			start = start - 1

		if self.exp == '00000000':
			if self.man == '0000000':
				if(self.sign == '1'):
					return -0.0
				else:
					return 0.0
			else: 
				out = ((-1)**int(self.sign) * 2**(exp_mag - 126) * (man_mag)) 
				return (float32(out))
		elif self.value == 'inf':
			return float(int(self.sign)*'-' +'Inf')
		else:
			out = ((-1)**int(self.sign) * 2**(exp_mag - 127) * (man_mag + 1))
			return (float32(out))


#----------------------------------------------------------------------------------------------	
#Local Functions
#----------------------------------------------------------------------------------------------
#Randomly generates a 16bit binary string
def rand16():
	a = random.randint(2, size = 16)
	s = ''.join(str(i) for i in a)
	return s


#Converters float32 to bfloat
def f2bfloat(num):
    packed = struct.pack('!f', num)
    integers = [c for c in packed]
    binaries = [bin(i) for i in integers]
    stripped_binaries = [s.replace('0b', '') for s in binaries]
    padded = [s.rjust(8, '0') for s in stripped_binaries]
    
    return bfloat(''.join(padded)[:16])


#parsers single binary string into its sign, exp, and man components
#Use *bin_parser(str) to unpack the tuples
#TODO: check if a is 16bits or not.
def bin_parser(a):
	return a[0] , a[1:9] , a[9:]
#-----------------------------------------------------------------------------------------------


#bfloat_mult:
#   input: (a, b) two 16bit binary string in Bfloat format, where a[0], b[0] are the MSBs
#   output: (mult_out) 16bit binary string in Bfloat format, where mult_out[0] is the
def bfloat_mult(a, b):

	#output sign
	o_sign = int(a.sign) ^ int(b.sign)
	o_sign = bin(o_sign)[2:]

	#Edge cases for +-Inf, +-NaN, +-Zero
	#Order of precedence: NaN -> Zero -> Inf
	if a.value == 'NaN' or b.value == 'NaN':
		return bfloat(o_sign, '11111111', '0000001')

	if a.value == 'zero' or b.value == 'zero':
		return bfloat(o_sign, '00000000', '0000000')

	if a.value == 'inf' or b.value == 'inf':
		return bfloat(o_sign, '11111111', '0000000')

	#Substrate the bias and add the exponents.
	o_exp = (int(a.exp,2) - 127)  + (int(b.exp,2) - 127)

	#normalize
	a_man = '1' + a.man
	b_man = '1' + b.man

	if a.exp == '00000000':
		a_man = a.man
	if b.exp == '00000000':
		b_man = b.man

	o_man = int(a_man,2) * int(b_man,2)
	o_man = bin(o_man)[2:]
	#Normalize output mantissa, adding the extra exponents, and add the bias
	dec_len =(len(a_man) - 1) + (len(b_man) - 1)
	o_exp += 127
	if len(o_man) <= dec_len + 1 and o_exp == 0:
		o_man = o_man.rjust(14,'0')
	else:
		o_exp += len(o_man) - (dec_len) - (1)

	#shift mantissa to right to accomudate for negative exp 
	if o_exp <= 0: 
		o_man = '0'*(-o_exp) + o_man
		o_man = o_man[0:7].ljust(7, '0')
		return bfloat(o_sign, '0'*8, o_man)
		
	if o_exp >= 255:  #if o_exp > '1111_1111'
		return bfloat(o_sign, '1'*8, '0'*7)

	o_exp = bin(o_exp)[2:].rjust(8, '0')
	o_man = o_man[1:8].ljust(7, '0')
	
	return bfloat(o_sign, o_exp, o_man)

    
def bfloat_add(a, b):
    if a.exp == "11111111":
        return a
    elif b.exp == "11111111":
        return b
    elif (a.exp == "00000000" and a.man == "0000000") and (b.exp == "00000000" and b.man == "0000000"):
        return bfloat("0","00000000", "0000000")
    elif (a.exp == "00000000" and a.man == "0000000") and not(b.exp == "00000000" and b.man == "0000000"):
        return b
    elif not(a.exp == "00000000" and a.man == "0000000") and (b.exp == "00000000" and b.man == "0000000"):
        return a

    if(a.exp == "00000000" and a.man != "0000000"):
        a_man = "0" + a.man
        a_exp = -126
    else:
        a_man = "1" + a.man
        a_exp = int(a.exp, 2) -127
    if(b.exp == "00000000" and b.man != "0000000"):
        b_man = "0" + b.man
        b_exp = -126
    else:
        b_man = "1" + b.man
        b_exp = int(b.exp, 2) - 127
    
    if(int(a_man,2) < int(b_man,2)):
        a_man = a_man + '0'
        a_exp = a_exp - 1
    elif(int(b_man,2) < int(a_man,2)):
        b_man = b_man + '0'
        b_exp = b_exp - 1
    # print(a_man, b_man)
    diff = a_exp - b_exp

    if(diff >= 0):
        b_man = int(b_man, 2) >> diff
        a_man = int(a_man, 2)
        b_exp = a_exp
    elif(diff < 0):
        a_man = int(a_man, 2) >> (-diff)
        b_man = int(b_man, 2)
        a_exp = b_exp
    # print(a_man, b_man)
    # print(bin(a_man)[2:], bin(b_man)[2:])
    if(a.sign == b.sign): 
        out_man = a_man + b_man
    elif(a.sign == "1" and b.sign == "0"):
        out_man = b_man - a_man
    elif(a.sign == "0" and b.sign == "1"):
        out_man = a_man - b_man
    
    if(out_man < 0):
        out_sign = "1"
        out_man = -out_man
    else:
        out_sign = "0"
        if a.sign == '1' and b.sign == '1':
            out_sign = '1'

    # print(bin(out_man))
    if len(bin(out_man)[2:]) > 8:
        shift_amt = len(bin(out_man)[2:]) - 8
        out_man = out_man >> shift_amt
        out_exp = a_exp + shift_amt + 127
    elif len(bin(out_man)[2:]) < 8:
        shift_amt = 8 - len(bin(out_man)[2:])
        out_man = out_man << shift_amt
        out_exp = a_exp - shift_amt + 127

    else:
        out_exp = a_exp + 127
        
    if out_exp <= 0:
        out_man = bin(out_man >> -out_exp)[2:]
        out_man = out_man.rjust(8, '0')
        return bfloat(out_sign, '0'*8, out_man[0:7])

    # print(out_exp)
    out_exp = bin(out_exp)[2:]
    if len(out_exp) < 8:
        exp_fill = 8 - len(out_exp)
        for i in range(0, exp_fill):
            out_exp = "0" + out_exp

    out_man = bin(out_man)[2:]
    if len(out_man) < 8:
        out_man = out_man.rjust(8, '0')
    
    # print(out_sign, out_exp, out_man)
    return bfloat(out_sign, out_exp, (out_man)[1:8])

#----------------------------------------------------------------------------------------------	
#Main Function
#----------------------------------------------------------------------------------------------

#Use for Debugging.
if __name__ == '__main__':
	# s1,e1,m1 = bin_parser('0111111010100011')
	# s2,e2,m2 = bin_parser('1111110101110110')
	# a = bfloat(s1,e1,m1)
	# b = bfloat(s2,e2,m2)
	# sum = bfloat_mult(a,b)
	# sum32 = a.display_dec() + b.display_dec() 
	# print("sum bin: ", sum.display_bin())
	
	# a = bfloat(rand16())
	# b = bfloat(rand16())
	# c = a*b
	# print(a.bin(), b.bin(), c.bin())
	
	a = bfloat("1010110110011110")
	b = bfloat("0101100110110011")
	c = a+b
	d = bfloat("0111110000110111")
	print(a.display_bin(), b.display_bin(), c.display_bin())
	print(a.display_dec(), b.display_dec(), c.display_dec())
	print(d.display_bin(), d.display_dec())
	
