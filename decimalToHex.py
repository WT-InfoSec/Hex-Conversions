# Hex to Decimal Conversions
# decimalToHex.py
#Will Taylor

'''
ALGORITHM:

1. Divide Number by 16
2. Get integer quotient for next iteration
3. Get remainder for hex digit
4. Repeat until quotient is equal to zero

'''
 ###################################
##          DECIMAL TO HEX         ##
 ###################################

def decimalToHex(number):
	output = ""
	quotient = getHexQuotient(number)
	remainder = getHexRemainder(number)
	# Add hex eqivalent of each remainder to string until quotient = 0
	while (quotient>0):
		output+= getBaseHex(remainder)
		remainder = getHexRemainder(quotient)
		quotient /= 16
	# add last digit to string
	output += getBaseHex(remainder)
	# return output in correct orientation
	return reverseOutput(output)

def getHexQuotient(number):
	return number/16

def getHexRemainder(number):
	return number%16


def getBaseHex(remainder):
	hexList = ['A', 'B', 'C', 'D', 'E', 'F']
	if(remainder > 9) and (remainder < 16):
		return hexList[remainder%10]
	else: 
		return str(remainder)

def reverseOutput(input):
	output = ""
	for i in xrange(len(input)-1,0,-1):
		output += input[i]
	#adds first character to output string
	output += input[0]
	return output

 ###################################
##          HEX TO DECIMAL         ##
 ###################################

def hexToDecimal(hexString):
	power = len(hexString)-1
	position = len(hexString)-1
	output = 0
	for i in xrange(0,power+1):
		output += getHexValue(hexString[i])*(16**power)
		power -= 1
	return output

def getHexValue(string):
	hexVals = ['0','1','2','3',
				'4','5','6','7',
				'8','9','A','B',
				'C','D','E','F']
	hexValues = dict()
	# create key for each hex value with appropriate decimal value
	for i in xrange(len(hexVals)):
		hexValues[hexVals[i]] = i
	return hexValues[string]

 ###################################
##          TEST FUNCTIONS         ##
 ###################################

def testDecimalToHex():
	assert(decimalToHex(3033669) == '2E4A45')
	assert(decimalToHex(479298376) == '1C918348')
	assert(decimalToHex(83782) == '14746')
	assert(decimalToHex(12736) == '31C0')
	assert(decimalToHex(736812) == 'B3E2C')
	print('DECIMAL TO HEX TEST COMPLETE!')

def testHexToDecimal():
	assert(hexToDecimal('2E4A45') == 3033669)
	assert(hexToDecimal('1C918348') == 479298376)
	assert(hexToDecimal('14746') == 83782)
	assert(hexToDecimal('31C0') == 12736)
	assert(hexToDecimal('B3E2C') == 736812)
	print('HEX TO DECIMAL TEST COMPLETE!')

testDecimalToHex()
testHexToDecimal()
