import cryptography
from Crypto.Cipher import AES
with open("./keysomewhere.dat", 'rb') as key:
    key = key.read()
with open("./msg.dat", 'rb') as message:
    message = message.read()
for i in range(len(key) - 16):
    new_key = key[i:i+16]
    cipher = AES.new(new_key,AES.MODE_ECB)
    dycrypt_msg_text = cipher.decrypt(message)
    try:
        if dycrypt_msg_text.isascii():
            print("The Message is:\t",dycrypt_msg_text,f"\nThe Key is:{new_key}".format(new_key))
    except:
        print("No luck this time")

