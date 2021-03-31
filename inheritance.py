class Omega:
	def __init__(self, a):
		print("Constructor Omega")
		self.var_a = a


class Alpha(Omega):				#Single level inheritance
	def __init__(self, a, b):
		super().__init__(a)
		print("Constructor Alpha")
		self.var_b = b



class Beta(Alpha):				#Multi level inheritance
	def __init__(self, a, b, c):
		super().__init__(a, b)
		print("Constructor Beta")
		self.var_c = c



class Theta:				
	def __init__(self, x):
		print("Constructor Theta")
		self.var_x = x	    


class Zero:
	COUNT = 0
	def __init__():
		print("No Argument")
		Zero.COUNT+=1
		print(f'incrementing count by one: value={Zero.COUNT}')

class Gamma(Beta,Theta):		#Multiple/Hybrid
	def __init__(self, a, b, c, d, e):
		Beta.__init__(self, a, b, c)
		Theta.__init__(self, d)
		Zero.__init__()
		print("Constructor Gamma")
		self.var_e = e		


if __name__ == "__main__":
	#beta_obj = Beta(1, 2, 3)
	gamma_obj = Gamma(True,'d','#','8', None)
	print(f'gamma_obj var_a={gamma_obj.var_a}, var_b={gamma_obj.var_b}, var_c={gamma_obj.var_c}, var_d={gamma_obj.var_x}, var_e={gamma_obj.var_e}')
