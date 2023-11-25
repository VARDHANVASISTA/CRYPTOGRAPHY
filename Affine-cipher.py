import string
from replit import clear
#string.ascii_lowercase
#string.ascii_uppercase
sm = list(string.ascii_lowercase)
lg = list(string.ascii_uppercase)
spch = ['!','@','#','$','^','&','*','(',')','_','','+','=','[',']','{','}','|',':',';',',','/','?','<','>','₹','%','"']
num = ['1','2','3','4','5','6','7','8','9','0']

logo = '''                                                                                                           
        ###    ######## ######## #### ##    ## ########     ######  #### ########  ##     ## ######## ########       
       ## ##   ##       ##        ##  ###   ## ##          ##    ##  ##  ##     ## ##     ## ##       ##     ##      
      ##   ##  ##       ##        ##  ####  ## ##          ##        ##  ##     ## ##     ## ##       ##     ##      
     ##     ## ######   ######    ##  ## ## ## ######      ##        ##  ########  ######### ######   ########       
     ######### ##       ##        ##  ##  #### ##          ##        ##  ##        ##     ## ##       ##   ##        
     ##     ## ##       ##        ##  ##   ### ##          ##    ##  ##  ##        ##     ## ##       ##    ##       
     ##     ## ##       ##       #### ##    ## ########     ######  #### ##        ##     ## ######## ##     ##      
'''

def encryption(pt, a, b):
    x = 0
    ct = ""
    for i in pt:
        x = sm.index(i)
        ct += sm[(a * x + b) % 26]
    clear()
    print(f"ENCRYPTED MESSAGE = {ct}")
    return ct

def decryption(ct, a, b):
    A=0
    for i in range (1,27):
        if (a * i) % 26 == 1:
            A = i
            break
    print(f"The multiplicative inverse key of {a} is >> {A}")
    pt = ""
    x = 0
    for i in ct:
        x = sm.index(i)
        pt += sm[(A * (x - b)) % 26]
    clear()
    print(f"ORIGINAL MESSAGE = {pt}")
    return pt
    
print(f"{logo}")
con = True
while con:
    ch = input("Choices are:\n 1. Encryption\n 2. Decryption\n Enter any other key to quit\nEnter your choice >> ")
    if ch == '1':
        pt = input("Enter the original message >> ")
        a = int(input("Enter first key >> "))
        b = int(input("Enter second key >> "))
        ct = encryption(pt, a, b)
        con1 = True
        while con1:
            op = input(f"Do you want to continue with {ct} as Cipher text and decrypt it?\nType 'Y' for yes or\nType 'N' for giving other Cipher text to decrypt or\nType 'S' for encrypting {ct}\nType 'C' for giving another Plain text to encrypt\nType any other key to quit\nEnter your choice >> ").upper()
            if op == 'Y':
                in1 = input(f"Do yo want to continue with the same keys ({a} and {b})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in1 == 'Y':
                    pt = decryption(ct, a, b)
                elif in1 == 'N':
                    a = int(input("Enter first key >> "))
                    b = int(input("Enter second key >> "))
                    pt = decryption(ct, a, b)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            elif op == 'N':
                ct = input("Enter the encrypted message >> ")
                a = int(input("Enter first key >> "))
                b = int(input("Enter second key >> "))
                pt = decryption(ct, a, b)
            elif op == 'S':
                pt = ct
                in2 = input(f"Do yo want to continue with the same keys ({a} and {b})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in2 == 'Y':
                    ct = encryption(pt, a, b)
                elif in2 == 'N':
                    a = int(input("Enter first key >> "))
                    b = int(input("Enter second key >> "))
                    ct = encryption(pt, a, b)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            elif op == 'C':
                pt = input("Enter the original message >> ")
                in3 = input(f"Do yo want to continue with the same keys ({a} and {b})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in3 == 'Y':
                    ct = encryption(pt, a, b)
                elif in3 == 'N': 
                    a = int(input("Enter first key >> "))
                    b = int(input("Enter second key >> "))
                    ct = encryption(pt, a, b)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            else:
                clear()
                print("Thank you...")
                con = False
                con1 = False
    elif ch == '2':
        ct = input("Enter the encrypted message >> ")
        a = int(input("Enter first key >> "))
        b = int(input("Enter second key >> "))
        pt = encryption(ct, a, b)
        con1 = True
        while con1:
            op = input(f"Do you want to continue with {pt} as Plain text and encrypt it?\nType 'Y' for yes or\nType 'N' for giving other Plain text to encrypt or\nType 'S' for decrypting {pt}\nType 'C' for giving another Cipher text to decrypt\nType any other key to quit\nEnter your choice >> ").upper()
            if op == 'Y':
                in1 = input(f"Do yo want to continue with the same keys ({a} and {b})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in1 == 'Y':
                    ct = encryption(pt, a, b)
                elif in1 == 'N':
                    a = int(input("Enter first key >> "))
                    b = int(input("Enter second key >> "))
                    ct = encryption(pt, a, b)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            elif op == 'N':
                pt = input("Enter the decrypted message >> ")
                a = int(input("Enter first key >> "))
                b = int(input("Enter second key >> "))
                ct = encryption(pt, a, b)
            elif op == 'S':
                ct = pt
                in2 = input(f"Do yo want to continue with the same keys ({a} and {b})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in2 == 'Y':
                    pt = decryption(ct, a, b)
                elif in2 == 'N':
                    a = int(input("Enter first key >> "))
                    b = int(input("Enter second key >> "))
                    pt = decryption(ct, a, b)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            elif op == 'C':
                ct = input("Enter the encrypted message >> ")
                in3 = input(f"Do yo want to continue with the same keys ({a} and {b})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in3 == 'Y':
                    pt = decryption(ct, a, b)
                elif in3 == 'N': 
                    a = int(input("Enter first key >> "))
                    b = int(input("Enter second key >> "))
                    pt = decryption(ct, a, b)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            else:
                clear()
                print("Thank you...")
                con = False
                con1 = False
    else:
        clear()
        print("Thank you...")
        con = False
