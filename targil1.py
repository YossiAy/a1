import os
import hashlib
pw_hash = "3752b8cc4f4fa147ce2fdd33689743c2a835900f41b5cfc33ec4cbcab6b33cb5"
password_dir='../pythonProject7/db_files/Q1'
for filename in os.listdir(password_dir):
    current_file = os.path.join(password_dir,filename)
    #print(f"current file is: {current_file}")
    #print(type(current_file))
    with open(current_file, 'r') as file:
        filename = os.path.basename(current_file)
        for line in file:
            message= line.replace('\n','') + filename
            #print(message)
            hasing=hashlib.sha256(message.encode()).hexdigest()
            if pw_hash == hasing:
                print(f"password is: {line} in file:{filename}")
                break
            else:
                pass