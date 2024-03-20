print("Loading modules, please wait...")
import random
import time
from tqdm import tqdm
rec_pass = input(str("DictionaryGenerator>>>Strict Recording of passwords or No:")).lower()
amount_pass = input("DictionaryGenerator>>>Amount of Passwords:")
if rec_pass == "yes":
    line_pass = input("DictionaryGenerator>>>Passwords in line:")
else:
    dupl_pass = input(str("DictionaryGenerator>>>Do you need to track duplicate passwords?|ATTENTION:Requires a lot of RAM:")).lower()
    long_pass = input("DictionaryGenerator>>>Long of Passwords:")
    elem_pass = input(str("DictionaryGenerator>>>Elements of Password:"))
    line_pass = input("DictionaryGenerator>>>Passwords in line:")
    long_pass = int(long_pass)
dict_preview = ""
password = ""
rec_password = 0
rec_password_str = ""
counter = 0
pass_count = 0
amount_pass = int(amount_pass)
line_pass = int(line_pass)
if line_pass > 0:
    line_pass -= 1
else:
    line_pass = line_pass
file = open("file.txt","w")
write_count = 0
progress = tqdm(total=amount_pass)
while counter < amount_pass:
    if rec_pass == "yes":
        rec_password += 1
        rec_password_str = str(rec_password)
        if line_pass == 0:
            file.write(rec_password_str)
            file.write("\n")
            progress.update(1)
        elif line_pass > 0:
            if write_count < line_pass:
                file.write(rec_password_str)
                file.write("-")
                progress.update(1)
                write_count += 1
            else:
                file.write(rec_password_str)
                file.write("\n")
                progress.update(1)
                write_count = 0
        else:
            print("DictionaryGenerator>>>You made a mistake")
            time.sleep(3)
            quit()
        rec_password_str = ""
        counter += 1
    elif rec_pass == "no":
        for x in range(long_pass):
           password = password + random.choice(list(elem_pass))
        if line_pass == 0:
            if dupl_pass == "yes":
                if password in dict_preview:
                    password = ""
                    pass
                else:
                    file.write(password)
                    file.write("\n")
                    progress.update(1)
                    if dupl_pass == "yes":
                        dict_preview = dict_preview + password + "\n"
            else:
                file.write(password)
                file.write("\n")
                progress.update(1)
        elif line_pass > 0:
            if write_count < line_pass:
                if dupl_pass == "yes":
                    if password in dict_preview:
                        password = ""
                        pass
                    else:
                        file.write(password)
                        file.write(" - ")
                        progress.update(1)
                        write_count += 1
                        if dupl_pass == "yes":
                            dict_preview = dict_preview + password + "\n"
                else:
                    file.write(password)
                    file.write(" - ")
                    progress.update(1)
                    write_count += 1
            else:
                if dupl_pass == "yes":
                    if password in dict_preview:
                        password = ""
                        pass
                    else:
                        file.write(password)
                        file.write(" - ")
                        progress.update(1)
                        write_count += 1
                        if dupl_pass == "yes":
                            dict_preview = dict_preview + password + "\n"
                else:
                    file.write(password)
                    file.write(" - ")
                    progress.update(1)
                    write_count += 1
        else:
            print("DictionaryGenerator>>>You made a mistake")
            time.sleep(3)
            quit()
        password = ""
        counter += 1
    else:
        print("DictionaryGenerator>>>You made a mistake")
