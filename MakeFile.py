import os
import time
num = input()
new_dir_path = "./過去問/ABC"+num
# try:
#     os.mkdir(new_dir_path)
# except:
#     print("既にフォルダが作られています")
os.mkdir(new_dir_path)
for i in range(97,97+6):
    file_path = new_dir_path + "/ABC" + num + chr(i) + ".py"
    f = open(file_path, 'a')
    f.close()
    os.startfile(os.path.normpath(file_path))
    time.sleep(0.5)
os.startfile(os.path.normpath(new_dir_path + "/ABC" + num + "a.py"))