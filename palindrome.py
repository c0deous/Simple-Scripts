from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", dest="string", help="the string to test")
(options, args) = parser.parse_args()

testString = options.string
result = ""
for b in testString:
	result = b+result
if testString == result:
	palindrome = "true"
else:
	palindrome = "false"
print("Original text: " + testString)
print("Reverse text: " + result)
print("Palindrome?: " + palindrome)

