import string
#string.ascii_lowercase
sm = list(string.ascii_lowercase)
lg = list(string.ascii_uppercase)
sym = ['~','!','@','#','$','%','^','&','*','(',')','-','_','+','=',' ',':',';','""','<','>',',','.','?','/']
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
    print(f"ct = {ct}")
    return ct

def decryption(ct, a, b):
    for i in range (1,27):
        if (a * i) % 26 == 1:
            A = i
            break
    pt = ""
    x = 0
    for i in ct:
        x = sm.index(i)
        pt += sm[(A * (x - b)) % 26]
    print(f"pt = {pt}")
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
    elif ch == '2':
        op = input(f"Do you want to continue with {ct} as Cipher text?\nType 'Y' for yes or\nType 'N' for giving other Cipher text or\nType any other key to quit\nEnter your choice >> ").upper()
        if op == 'Y':
            pt = decryption(ct, a, b)
        elif op == 'N':
            ct = input("Enter the encrypted message >> ")
            a = int(input("Enter first key >> "))
            b = int(input("Enter second key >> "))
            pt = decryption(ct, a, b)
        else:
            print("Thank you...")
            con = False
    else:
        print("Thank you...")
        con = False
