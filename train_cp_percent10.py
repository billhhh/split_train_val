import os
import os.path
from shutil import copyfile
from math import floor
from random import shuffle
import shutil

list_path = './'
train_list = 'newFood724_train_percent10.txt'
cp_ratio = 0.1

src_dir = 'train'
des_dir = 'train_percent10'
os.mkdir(des_dir)

class_names = []
for filename in os.listdir(src_dir):
    path = os.path.join(src_dir, filename)
    if os.path.isdir(path):
        class_names.append(filename)

lst = class_names
lst.sort()
print(lst)

f_train = open(os.path.join(list_path, train_list), 'w')

for ind in range(0,len(lst)):
    os.mkdir(des_dir + '/' + lst[ind])
    sblst=os.listdir(os.path.join(src_dir,lst[ind]))
    shuffle(sblst)
    print(len(sblst))
    cnt=0
    for pic_name in sblst:
        filepath_src= src_dir + '/' + lst[ind] + '/' + pic_name
        des_path= des_dir + '/' + lst[ind] + '/' + pic_name
        if pic_name.endswith('.db') == True:
            continue
        else:
            cnt+=1
            if cnt <= floor(len(sblst) * cp_ratio):
                f_train.writelines(des_path + " " + str(ind) + '\n')
                # copy files
                shutil.copy(filepath_src, des_path)

f_train.close()
