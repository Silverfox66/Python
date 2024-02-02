#Crypto

#What is up
def encrypt(plaintext, offset, indexByChar, charByIndex):
    ciphertext = plaintext

    for x in range(len(ciphertext)):
        index = indexByChar[ciphertext[x]]
        index = (index + offset) % len(indexByChar)
        char = charByIndex[index]
        ciphertext = ciphertext[ : x] + char + ciphertext[x + 1 :]

    return ciphertext

def decrypt(ciphertext, offset, indexByChar, charByIndex):
    plaintext = ciphertext

    for x in range(len(plaintext)):
        index = indexByChar[plaintext[x]]
        index = (index - offset) % len(indexByChar)
        char = charByIndex[index]
        plaintext = plaintext[ : x] + char + plaintext[x + 1 :]

    return plaintext
# Make a dictionary from a-z a is 0, b is 1 and so on.
indexByChar = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,'A':26,'B':27,'C':28,'D':29,'E':30,'F':31,'G':32,'H':33,'I':34,'J':35,'K':36,'L':37,'M':38,'N':39,'O':40,'P':41,'Q':42,'R':43,'S':44,'T':45,'U':46,'V':47,'W':48,'X':49,'Y':50,'Z':51,' ':52,',':53,'.':54,'!':55,'?':56,'=':57,'+':58,'-':59,'*':60,'/':61,':':62,'<':63,'>':64}
#expand Alphabet
charByIndex = list(indexByChar.keys())

offset = 3

message = "Hello World!"

ciphertext = encrypt(message, offset, indexByChar, charByIndex)

plaintext = decrypt(ciphertext, offset, indexByChar, charByIndex)

print("message: ", message)
print("ciphertext: ", ciphertext)
print("plaintext: ", plaintext)

