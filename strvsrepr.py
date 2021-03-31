import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))

class Complex(object):
	"""docstring for Complex"""
	def __init__(self, real, imag):
		#super(Complex, self).__init__()
		self.real = real
		self.imag = imag

	def __repr__(self):
		return f'Rational({self.real},{self.imag})'

	def __str__(self):
		return f'{self.real}+i{self.imag}'


c = Complex(10,20)
print(repr(c))
print(str(c))
		