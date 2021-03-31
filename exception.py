import time

'''while True:
	try:
		print("hurrah")
		time.sleep(0.1)
	except:
		print('no')'''
while True:
	try:
		print("hurrah")
		time.sleep(0.1)
		raise Exception('woah!')
	except Exception:				#keyboard exception not a subclass of Exception. Does not get cAUGHT
		print('no')