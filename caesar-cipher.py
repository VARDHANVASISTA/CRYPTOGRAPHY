def encryption(msg, shift):
    encm = ""
    for i in range(len(msg)):
        pc = msg[i]
        pos = 0
        if pc in cap:
            while pc != cap[pos]:
                pos += 1
            pos = (pos + shift) % 26
            encm += cap[pos]
        elif pc in sm:
            while pc != sm[pos]:
                pos += 1
            pos = (pos + shift) % 26
            encm += sm[pos]
        elif pc in num:
            while pc != num[pos]:
                pos += 1
            pos = (pos + shift) % 10
            encm += num[pos]
        elif pc in spch:
            while pc != spch[pos]:
                pos += 1
            pos = (pos + shift) % 28
            encm += spch[pos]
        else:
            encm += pc
    clear()
    print(f"Encrypted message is >> {encm}")
    return encm

def decryption(msg, shift):
    orm = ""
    for i in range(len(msg)):
        pc = msg[i]
        pos = 0
        if pc in cap:
            while pc != cap[pos]:
                pos += 1
            pos = (pos - shift) % 26
            if pos < 0:
                pos += 26
            orm += cap[pos]
        elif pc in sm:
            while pc != sm[pos]:
                pos += 1
            pos = (pos - shift) % 26
            if pos < 0:
                pos += 26
            orm += sm[pos]
        elif pc in num:
            while pc != num[pos]:
                pos += 1
            pos = (pos - shift) % 10
            if pos < 0:
                pos += 10
            orm += num[pos]
        elif pc in spch:
            while pc != spch[pos]:
                pos += 1
            pos = (pos - shift) % 28
            if pos < 0:
                pos += 28
            orm += spch[pos]
        else:
            orm += pc
    clear()
    print(f"Decrypted message is >> {orm}")
    return orm


logo = """ 

                                      ######     ###    ########  ######     ###    ########  
                                     ##    ##   ## ##   ##       ##    ##   ## ##   ##     ## 
                                     ##        ##   ##  ##       ##        ##   ##  ##     ## 
                                     ##       ##     ## ######    ######  ##     ## ########  
                                     ##       ######### ##             ## ######### ##   ##   
                                     ##    ## ##     ## ##       ##    ## ##     ## ##    ##  
                                      ######  ##     ## ########  ######  ##     ## ##     ## 


                                      ######  #### ########  ##     ## ######## ########      
                                     ##    ##  ##  ##     ## ##     ## ##       ##     ##     
                                     ##        ##  ##     ## ##     ## ##       ##     ##     
                                     ##        ##  ########  ######### ######   ########      
                                     ##        ##  ##        ##     ## ##       ##   ##       
                                     ##    ##  ##  ##        ##     ## ##       ##    ##      
                                      ######  #### ##        ##     ## ######## ##     ##     

"""

from replit import clear
import string
sm = list(string.ascii_lowercase)
spch = ['!','@','#','$','^','&','*','(',')','_','','+','=','[',']','{','}','|',':',';',',','/','?','<','>','₹','%','"']
cap = list(string.ascii_uppercase)
num = ['1','2','3','4','5','6','7','8','9','0']
print(logo)#ASCII ART FROM : patorjk.com  STYLE : BANNER3
con = True
while con:
    ch = input("Choices are:\n 1. Encryption\n 2. Decryption\n Enter any other key to quit\nEnter your choice >> ")
    if ch == '1':
        pt = input("Enter the original message >> ")
        a = int(input("Enter the shift key >> "))
        ct = encryption(pt, a)
        con1 = True
        while con1:
            op = input(f"Do you want to continue with '{ct}' as Cipher text and decrypt it?\nType 'Y' for yes or\nType 'N' for giving other Cipher text to decrypt or\nType 'S' for encrypting '{ct}'\nType 'C' for giving another Plain text to encrypt\nType any other key to quit\nEnter your choice >> ").upper()
            if op == 'Y':
                in1 = input(f"Do yo want to continue with the same key ({a})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in1 == 'Y':
                    pt = decryption(ct, a)
                elif in1 == 'N':
                    a = int(input("Enter the shift key >> "))
                    pt = decryption(ct, a)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            elif op == 'N':
                ct = input("Enter the encrypted message >> ")
                a = int(input("Enter the shift key >> "))
                pt = decryption(ct, a)
            elif op == 'S':
                pt = ct
                in2 = input(f"Do yo want to continue with the same keys ({a})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in2 == 'Y':
                    ct = encryption(pt, a)
                elif in2 == 'N':
                    a = int(input("Enter the shift key >> "))
                    ct = encryption(pt, a)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            elif op == 'C':
                pt = input("Enter the original message >> ")
                in3 = input(f"Do yo want to continue with the same keys ({a})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in3 == 'Y':
                    ct = encryption(pt, a)
                elif in3 == 'N': 
                    a = int(input("Enter the shift key >> "))
                    ct = encryption(pt, a)
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
        a = int(input("Enter the shift key >> "))
        pt = encryption(ct, a)
        con1 = True
        while con1:
            op = input(f"Do you want to continue with '{pt}' as Plain text and encrypt it?\nType 'Y' for yes or\nType 'N' for giving other Plain text to encrypt or\nType 'S' for decrypting '{pt}'\nType 'C' for giving another Cipher text to decrypt\nType any other key to quit\nEnter your choice >> ").upper()
            if op == 'Y':
                in1 = input(f"Do yo want to continue with the same keys ({a})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in1 == 'Y':
                    ct = encryption(pt, a)
                elif in1 == 'N':
                    a = int(input("Enter the shift key >> "))
                    ct = encryption(pt, a)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            elif op == 'N':
                pt = input("Enter the decrypted message >> ")
                a = int(input("Enter the shift key >> "))
                ct = encryption(pt, a)
            elif op == 'S':
                ct = pt
                in2 = input(f"Do yo want to continue with the same keys ({a})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in2 == 'Y':
                    pt = decryption(ct, a)
                elif in2 == 'N':
                    a = int(input("Enter the shift key >> "))
                    pt = decryption(ct, a)
                else:
                    clear()
                    print("Thank you....")
                    con1 = False
                    con = False
            elif op == 'C':
                ct = input("Enter the encrypted message >> ")
                in3 = input(f"Do yo want to continue with the same keys ({a})?\nType 'Y' for yes or\nType 'N' for giving different keys\nType any other key to quit\nEnter your choice >>  ").upper()
                if in3 == 'Y':
                    pt = decryption(ct, a)
                elif in3 == 'N': 
                    a = int(input("Enter the shift key >> "))
                    pt = decryption(ct, a)
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
