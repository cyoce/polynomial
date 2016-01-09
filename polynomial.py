import itertools
import re
class Poly:
	def __init__ (self, terms):
		self.terms = terms

	def __len__ (self):
		return len (self.terms)

	def __getitem__ (self, idx):
		if len (self) <= idx:
			return 0
		return self.terms [idx]

	def __setitem__ (self, idx, value):
		if len (self) <= idx:
			if value:
				while len (self) <= idx:
					self.terms.append(0)
			else:
				return None
		self.terms [idx] = value
		return value
	def __str__ (self):
		out = list(enumerate (self.terms))
		out = list(filter (lambda x: x[1], out))
		out = ['%sx^%s' % (j,i)  if j > 1 else (('%sx' if j == 1 else '%s') % (j)) for i,j in out]
		out.reverse()
		return re.sub(r'x\^0|\^1', '', ' + '.join(out).replace ('+ -', ' - '))
