import os
import os.path
from shutil import copyfile
from math import floor
from random import shuffle

list_path = './'
evaluation_list = 'evaluate-2018-02-halfway.txt';
src_dir = 'evaluate-2018-02-halfway';
all_food_dir = 'D:/share/FoodAI_756_20180422/val';

class_names = []
for filename in os.listdir(src_dir):
    path = os.path.join(src_dir, filename)
    if os.path.isdir(path):
        class_names.append(filename)

lst = class_names
lst.sort()

all_food_class_names = []
for filename in os.listdir(all_food_dir):
    path = os.path.join(all_food_dir, filename)
    if os.path.isdir(path):
        all_food_class_names.append(filename)

all_food_lst = all_food_class_names
all_food_lst.sort()

f_evaluation = open(os.path.join(list_path, evaluation_list), 'w')

for ind in range(0,len(lst)):
    sblst=os.listdir(os.path.join(src_dir,lst[ind]))
    shuffle(sblst)
    print(len(sblst))
    for pic_name in sblst:
        filepath_src= src_dir + '/' + lst[ind] + '/' + pic_name
        if pic_name.endswith('.db') == True:
            continue
        else:
            label_id = all_food_lst.index(lst[ind]);
            f_evaluation.writelines(filepath_src + " " + str(label_id) + '\n')

f_evaluation.close()
