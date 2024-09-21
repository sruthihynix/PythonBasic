import re
import re
# module for regular expressio
# print(r'\na') # 'r' given in print to identify it is a regular string
#------------------re.search('sequence', string name)

# txt='rain rain come again'
# print(re.search('hai',txt))# output none or truer
# print(re.search('a',txt))

# txt1 = 'i saw tigers and zeebra'
# pattern= r'\b\w{3,5}\s'
# re.findall(pattern,'i saw tigers and zebra')
# print(re.findall())
# pat=r'\b(a)\w |e\w*'
# re.findall(pat,"I appple europe")
pat=r'[,.\s]'
patten