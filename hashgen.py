#import

import time, os, sys, subprocess

#req

 #HashGen

HASHLANG = {
    'A': 'au001X', 'B': 'au002X', 'C': 'au003X', 'D': 'au004X', 'E': 'au005x', 'F': 'au006X', 'G': 'au007X', 'H': 'au008X', 'I': 'au009X',
    'J': 'au0010X', 'K': 'au0011X', 'L': 'au0012X', 'M': 'au0013X', 'N': 'au0014X', 'O': 'au0015X', 'P': 'au0016X', 'Q': 'au0017X', 'R': 'au0018X',
    'S': 'au0019X', 'T': 'au0020X', 'U': 'au0021X', 'V': 'au0022X', 'W': 'au0023X', 'X': 'au0024X', 'Y': 'au0025X', 'Z': 'au0026X',
    '0': 'au10q', '1': 'au20w', '2': 'au30e', '3': 'au40r', '4': 'au50t', '5': 'au60y', '6': 'au70u', '7': 'au80i',
    '8': 'au90o', '9': 'auX0p'
}


BNLANG = {
	'0': 'x', '1': 'y'
}

def bndash(text):
    text = text.upper()
    bndash = ' '.join(BNLANG.get(char, '') for char in text)
    return bndash

def pvlang(text):
    pvlang = []
    for char in text.upper():
        if char == ' ':
            pvlang.append(' ')
        elif char in HASHLANG:
            pvlang.append(HASHLANG[char])
    return ' '.join(pvlang)

def text_to_binary(text):
    binary_code = ' '.join(format(ord(char), '08b') for char in text)
    return binary_code

def create_unique_filename(filename):
    index = 0
    base_name, extension = filename.split('.')
    new_filename = f"{base_name}.{extension}"
    
    while True:
        try:
            with open(new_filename, 'x'):
                return new_filename
        except FileExistsError:
            index += 1
            new_filename = f"{base_name}{index}.{extension}"

filename = "HashGen.txt"

 #Compiler

def pvlangcompiler(compiler):
    compiler = compiler.split(' ')
    text = ''
    for code in compiler:
        for char, morse in HASHLANG.items():
            if code == morse:
                text += char
                break
        else:
            text += ' '
    return text

def binary_to_text(binary_code):
    binary_list = binary_code.split()
    text = ''.join(chr(int(binary, 2)) for binary in binary_list)
    return text

def bnhashcompiler(compiler):
    compiler = compiler.split(' ')
    text = ''
    for code in compiler:
        for char, morse in BNLANG.items():
            if code == morse:
                text += char
                break
        else:
            text += ' '
    return text


class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

def typewriter(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

url = "https://github.com/TnYtCoder"

#logo & options

time.sleep(0.5)
os.system("clear")
time.sleep(0.5)

def logo():
	logo = '''
\033[32m    __ __         __   _____
   / // /__ ____ / /  / ___/__ ___
  / _  / _ `(_-</ _ \/ (_ / -_) _ \ 
 /_//_/\_,_/___/_//_/\___/\__/_//_/
 <-------------------------------->
 | GitHub : TnYtCoder             |
 | A Powerful Password Hider      |
 +--------------------------------+
	'''
	typewriter(logo)

logo()

time.sleep(0.5)
print("\n\033[35m [1] Start HashGen")
print("\033[35m [2] Complile HashGen")
print("\033[35m [3] Help")
print("\033[31m [4] Exit")

#input

time.sleep(0.5)
opt = int(input("\n\033[32m Your Option : "))

#process

if opt == 1:
	text = input("\n\033[32m Your Text : \033[34m")
	pvgen = pvlang(text)
	bngen = text_to_binary(pvgen)
	tngen = bndash(bngen)
	time.sleep(1)
	print("\n\033[32m HashGen : \033[35m\n " , tngen)
	unique_filename = create_unique_filename(filename)
	try:
		f = open(unique_filename, 'w')
		f.write(tngen)
		f.close()
		print("\n [+] HashGen Saved {} \n".format(unique_filename))
	except:
		print("\n\033[32m [+] Error To Save .txt\n")

	time.sleep(0.5)
	typewriter("\n\033[32m Thank You For Using !!")
	time.sleep(0.5)
elif opt == 2:
	cotext = input("\n\033[32m Your HashGen : ")
	cotngen = bnhashcompiler(cotext)
	cobngen = binary_to_text(cotngen)
	copvgen = pvlangcompiler(cobngen)
	time.sleep(1)
	print("\n\033[32m HashGen Compiler : \033[35m\n " + copvgen)
	time.sleep(0.5)
	typewriter("\n\033[32m Thank You For Using !!")
	time.sleep(0.5)

elif opt == 3:
	time.sleep(1)
	subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	time.sleep(0.5)
	typewriter("\n\033[32m Thank You For Using !!")
	time.sleep(0.5)
	sys.exit(1)

elif opt == 4:
	time.sleep(0.5)
	typewriter("\n\033[32m Thank You For Using !!")
	time.sleep(0.5)
	sys.exit(1)

else:
	time.sleep(0.5)
	typewriter("\n\033[31m Please Select Correct Option !!")
	time.sleep(0.5)
	sys.exit(1)
