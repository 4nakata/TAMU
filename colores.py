def textPrimario(text):
	print("\n\033[1;33m", text, "\033[0;m")

def textError(text):
	print("\n\033[1;31m", text, "\033[0;m")

def textBold(text):
	print("\n\033[1;0m", text, "\033[0;m")

def textSuccess(text):
	print("\n\033[1;32m", text, "\033[0;m")

def hr():
	print("\n============================================================================")

def inputBold(text):
	print("\n")
	return input("\033[1;0m"+ text +"\033[0;m")