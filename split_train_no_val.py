import os
import os.path
from shutil import copyfile
from math import floor
from random import shuffle

list_path = './'
train_list = 'newFood724_train_percent10_aug.txt'

src_dir = 'images'

class_names = []
for filename in os.listdir(src_dir):
    path = os.path.join(src_dir, filename)
    if os.path.isdir(path):
        class_names.append(filename)

lst = class_names
lst.sort()

f_train = open(os.path.join(list_path, train_list), 'w')

for ind in range(0,len(lst)):
    sblst=os.listdir(os.path.join(src_dir,lst[ind]))
    shuffle(sblst)
    print(len(sblst))
    for pic_name in sblst:
        filepath_src= src_dir + '/' + lst[ind] + '/' + pic_name
        if pic_name.endswith('.db') == True:
            continue
        else:
            f_train.writelines(filepath_src + " " + str(ind) + '\n')

f_train.close()
