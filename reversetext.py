from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--string", dest="string")
(options, args) = parser.parse_args()

result = ""
for b in options.string:
	result = b+result
print(result)
