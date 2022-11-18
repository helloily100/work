# %% [markdown]
# # CECS 229 Coded HW #3
# 
# #### Due Date: 
# 
# Sunday, 3/6 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit the following by the due date:
# 
# 1. **To the BB Dropbox Folder:** this completed .ipynb file
# 
# 2. **To CodePost:** this file converted to a Python script named `ca3.py`
# 
# #### Objectives:
# 
# 1. Find the inverse of a given integer under a given modulo m.
# 2. Encrypt and decrypt text using an affine transformation.
# 3. Encrypt and decrypt text using the RSA cryptosystem.
# 
# 
# 
# 
# ### Programming Tasks
# 
# You may use the utility functions at the end of this notebook to aid you in the implementation of the following tasks:

# %% [markdown]
# ------------------------------------------
# ##### Utility functions (NO EDITS NECESSARY)
# %%
def bezout_coeffs(a, b):
    s = 0
    s0 = 1
    t = 1
    t0 = 0
    b = b
    a = a
    dict = {'a':a,'b':b}
    if b < 0:
        while b != 0:
            quotient = a//b 
            a, b = b, a - quotient*b
            s0, s = s, s0 - quotient*s
            t0, t = t, t0 - quotient*t
        return {dict.get('a'):(s0*-1),dict.get('b'):(t0*-1)}

    else:
        while b != 0:
            quotient = a//b 
            a, b = b, a - quotient*b
            s0, s = s, s0 - quotient*s
            t0, t = t, t0 - quotient*t
        return {dict.get('a'):s0,dict.get('b'):t0}

def gcd(a,b):
    dict = bezout_coeffs(a, b)
    return abs((a * dict.get(a) + b * dict.get(b)))

# %%
def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

# %%
def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

# %%
def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
# %% [markdown]
# -------------------------------------------
# 
# #### Problem 1: 
# Create a function `modinv(a,m)` that returns the smallest, positive inverse of `a` modulo `m`.  If the gcd of `a` and `m` is not 1, then you must raise a `ValueError` with message `"The given values are not relatively prime"`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# %%
def modinv(a,m):
    if gcd(a,m) != 1:
        raise ValueError("The given values are not relatively prime")
    for x in range(1,m):
        if (((a%m)*(x%m))%m == 1):
            return x

# %% [markdown]
# ------------------------------------
# 
# #### Problem 2: 
# Create a function `affineEncrypt(text, a,b)` that returns the cipher text encrypted using key  (`a`, `b`).  You must verify that the gcd(a, 26) = 1 before making the encryption.  If this is not the case, the function must raise a `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# %%
def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
    if gcd(a,26) != 1:
      raise ValueError('The given key is invalid. The gcd(a,26) must be 1')
    text = text.replace(' ','')
    num = []

    for i in text:
        num.append(int(letters2digits(i)))
    for i in range(len(num)):
        num[i] = ((a*num[i])+b)%26
        if num[i] < 10:
            num[i] = "0" + str(num[i])
        else:
            num[i] = str(num[i])
    text = ''.join(num)
    return (digits2letters(text))

# %% [markdown]
# #### Problem 3: 
# Create a function `affineDecrypt(ciphertext, a,b)` that returns the cipher text encrypted using key  (`a`, `b`). You must verify that the gcd(a, 26) = 1.  If this is not the case, the function must raise `ValueError` with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented in previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# %%
def affineDecrypt(ciphertext, a, b):
    """decrypts the string 'ciphertext', which was encrypted using an affine transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
    if gcd(a,26) != 1:
        raise ValueError('The given key is invalid. The gcd(a,26) must be 1')
    text = ciphertext
    num=[]
    a = modinv(a,26)
    for i in text:
        num.append(int(letters2digits(i)))
    for i in range(len(num)):
        num[i] = (a*(num[i]-b))%26
        if num[i] < 10:
            num[i] = "0" + str(num[i])
        else:
            num[i] = str(num[i])
    text = ''.join(num)
    return (digits2letters(text))

# %% [markdown]
# -----------------------------------
# 
# #### Problem 4:
# 
# Implement the function `encryptRSA(m, n, e)` which encrypts a string `m` using RSA key `(n = p * q, e)`.  You may NOT use any built-in functions as part of your implementation, but you may use any functions you implemented for previous coding assignments.  Please make sure to copy and paste them into this file, so that they are uploaded to CodePost when you submit your `ca3.py` file.

# %%
def encryptRSA(m, n, e):
    """encrypts the plaintext m, using RSA and the key (n = p * q, e)
    INPUT:  m - plaintext as a string of letters
            n - a positive integer
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    text = m
    if n > 300:
        n = n
    l = blocksize(n)
    g = l//2
    num = []
    for i in text:
        num.append(letters2digits(i))
    if len(num) % 2 != 0:
        num.append('23')
    for i in range(g,len(num)):
        num[i-2 : i] = [''.join(num[i-2 : i])]
    num = list(filter(None,num))
    for i in range(len(num)):
        num[i] = (int(num[i]) ** e) % n
    for i in range(len(num)):
        num[i] = str(num[i])
    for i in range(len(num)):
        if len((num[i])) < l:
            for j in range(l - len((num[i]))):
                num[i] = '0'+num[i]
    text = ' '.join(num)
    return text


# %%
"""--------------------- ENCRYPTION TESTER CELL ---------------------------"""
encrypted1 = encryptRSA("STOP", 2537, 13)
encrypted2 = encryptRSA("HELP", 2537, 13)
encrypted3 = encryptRSA("STOPS", 2537, 13)
print("Encrypted Message:", encrypted1)
print("Expected: 2081 2182")
print("Encrypted Message:", encrypted2)
print("Expected: 0981 0461")
print("Encrypted Message:", encrypted3)
print("Expected: 2081 2182 1346")


"""--------------------- TEST 2 ---------------------------"""
encrypted = encryptRSA("UPLOAD", 3233, 17)
print("Encrypted Message:", encrypted)
print("Expected: 2545 2757 1211")

# %% [markdown]
# -------------------------------------------------------
# 
# #### Problem 5:
# 
# Complete the implementation of the function `decryptRSA(c, p, q, m)` which depends on `modinv(a,m)` and the given functions `digits2letters(digits)` and `blockSize(n)`.  When you are done, you can test your function against the given examples.

# %%
def decryptRSA(c, p, q, e):
    """decrypts the cipher c, which was encrypted using the key (p * q, e)
    INPUT:  c - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    text = c
    n = p * q
    l = blocksize(n)
    e = modinv(e,(p-1)*(q-1))
    num = text.split()
    for i in range(len(num)):
        num[i] = int(num[i])
    for i in range(len(num)):
        num[i] = (num[i] ** e) % n
    for i in range(len(num)):
        num[i] = str(num[i])
    for i in range(len(num)):
        if len((num[i])) < l:
            num[i] = '0'+num[i]
    text = ''.join(num)
    return digits2letters(text)

# %%
"""--------------------- TESTER CELL ---------------------------"""
decrypted1 = decryptRSA("2081 2182", 43, 59, 13)
decrypted2 = decryptRSA("0981 0461", 43, 59, 13)
decrypted3 = decryptRSA("2081 2182 1346", 43, 59, 13)
print("Decrypted Message:", decrypted1)
print("Expected: STOP")
print("Decrypted Message:", decrypted2)
print("Expected: HELP")
print("Decrypted Message:", decrypted3)
print("Expected: STOPSX")

"""--------------------- TEST 2---------------------------"""
decrypted = decryptRSA("0667 1947 0671", 43, 59, 13)
print("Decrypted Message:", decrypted)
print("Expected: SILVER")




