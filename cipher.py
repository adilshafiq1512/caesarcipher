import subprocess
#-----------------------------------------encyption--------------------
def encrypt(string, shift):

  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  return cipher
#--------------------------------------decryption--------------------
def decrypt(string, shift):

  cipher = ''
  for char in string:
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

  return cipher
  #------------------------------------crack-------------------------
def crack(cipher):
	plaintext = ''

	for key in range(1, 27):
		plaintext += '[' + str(key) + '] '
		for char in cipher:
			if  char.isupper():
			  plaintext = plaintext + chr((ord(char) - key - 65) % 26 + 65)  
			else:
			  plaintext = plaintext + chr((ord(char) - key - 97) % 26 + 97)
		plaintext += '\n'

	print(plaintext)
#------------------------------------main-------------------------------
n = 'n'
d = ''

while n == 'n':
    d = input("select e/d/c for encryption(e), decryption(d) or crack(c): ")
    if 'e' == d:
        text = input("enter string: ")
        s = int(input("enter private pin: "))
        subprocess.run('clear')
        print("original string: ", text)
        print("after encryption: ", encrypt(text, s))

    elif 'd' == d:
        text = input("enter string: ")
        s = int(input("enter private pin: "))
        subprocess.run('clear')
        print("original string: ", text)
        print("after encryption: ", decrypt(text, s))
    elif 'c' == d:
        cipher = input("enter cipher text: ")
        crack(cipher)



    n  = input ( "do you want to exit (y/n):" )
    subprocess.run('clear')
