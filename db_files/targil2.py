import os
import hashlib
pw_hash = "a7312e17ba07ab09dacfebc4cdc2fe516043c1c2fd71078abcebb1e2a017f6c8"
password_dir='../pythonProject7/db_files/Q2'
for filename in os.listdir(password_dir):
    current_file = os.path.join(password_dir,filename)
    #print(f"current file is: {current_file}")
    with open(current_file,'r') as file:
        filename = os.path.basename(current_file)
        # print(f"filename is {filename}")
        for line in file:
            try:
                message = line.replace('\n','') + filename
                times,pw=message.split("_",1)
                test = hashlib.sha256(message.encode()).hexdigest()
            except:
                pass
            try:
                for i in range(int(times)):
                    test=hashlib.sha256(pw.encode()).hexdigest()
                    pw=test
                    #print(test)
                    if pw_hash == test:
                        print(f"password: {line}")
                        break
            except:
                print("not found")




"""
message="10_testme"
# remove leading and trailing whitespaces
first,last=message.split('_',1)
# Output: Message: Learn Python
print(first)
print(last)
"""