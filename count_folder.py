import os
import os.path
from shutil import copyfile
from math import floor
from random import shuffle

list_path = './'
train_list = 'count_folder.txt'

src_dir = '2018-02-halfway'

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

    f_train.writelines(lst[ind] + "," + str(len(sblst)) + '\n')

f_train.close()
