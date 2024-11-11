#Created by: Cleon Simpson
#Date: 10/11/2024
import math

#This follows the Euclidean algorithm
def gcd(a,b):
    while b:
        a,b=b,a%b #switches the bigger number with the smaller one continuously until one becomes 0
    return a

#The below finds the modular inverse of e%phi
def mod_inverse(e,phi):
# 1<e<(a-1)*(b_1)
    for d in range (1,phi):
        if (d*e)%phi ==1:
            return d
    return None

#The below finds the two prime factors a and b       
def factorize(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return i,n//i
    return None,None


#The below finds 
def rsa_decrypt(c,e,n):
    p,q=factorize(n)
    if not p or not q:
        return "Unable to factorize n"
    
    
    #We will need a function to calculate the phi of n
    phi=(p-1)*(q-1)
    #We will need a function to calculate the mod inverse
    d=mod_inverse(e,phi)
    if not d:
        return "Failed to find modular Inverse"
    
    message=pow(c,d,n)
    return message
ciphertext=1648
e=43
n=2117

decrypt_message=rsa_decrypt(ciphertext,e,n)
print("Decrypted Message: ", decrypt_message)

#Password 11264267153