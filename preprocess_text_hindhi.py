# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:05:26 2020

@author: chandar
"""

import numpy as np
import pandas as pd
import cv2
import os
import tqdm
from scipy.io import loadmat
import matplotlib.pyplot as plt

image_path = r'D:\Dl course\Deep learning\capstone project\Synthetic Train Set (100k) - Detection & Recognition.tar\Synthetic Train Set - Detection & Recognition\Image\1'
gt_path = r'D:\Dl course\Deep learning\capstone project\Synthetic Train Set (100k) - Detection & Recognition.tar\Synthetic Train Set - Detection & Recognition\Annotation\1'
gt_path_new = r'D:\Dl course\Deep learning\capstone project\Synthetic Train Set (100k) - Detection & Recognition.tar\Synthetic Train Set - Detection & Recognition\Annotation_yolo_tetxt\1'
train_image_paths = []
train_gt_paths = []

dumy = os.listdir(gt_path)
hindi_words=[]
my_word_list_new=[]

for txt_name in dumy:
    with open(gt_path+'\\'+txt_name,mode='r',encoding='utf-8') as f:
        mylist = [line.rstrip('\n') for line in f]
        
    for lines in mylist:
        my_word_list=lines.split()
        hindi_words.append(my_word_list[8])
        my_word_list=[float(i) for i in my_word_list[0:8]]
        my_word_list_new=[]
        my_word_list_new.append(0)
        my_word_list_new.append(round((my_word_list[1]-my_word_list[0])/(2*600),3)) #centre_X scaled by the width 600
        my_word_list_new.append(round((my_word_list[6]-my_word_list[5])/(2*450),3)) #centre_Y
        my_word_list_new.append(round((my_word_list[1]-my_word_list[0])/600,3)) #Widht of the image
        my_word_list_new.append(round((my_word_list[6]-my_word_list[5])/450,3)) #Height of the image
        
        my_word_list_new=[str(i) for i in my_word_list_new]
        
        with open(gt_path_new+'\\'+txt_name,mode='a+') as f1:
           for yolo_annot in my_word_list_new:
               f1.write(yolo_annot+' ')
           f1.write('\n')
       
    
    




 










# for new_file in tqdm.tqdm(os.listdir(gt_path)):
    
#     name_split = new_file.split('.')
#     image_name = name_split[0]
#     image_name = image_name + '.jpg'
    
#     if 'gt' in new_file:
#         image_name = name_split[0][3:]
#         image_name = image_name + '.jpg'
    
#     path_img = os.path.join(image_path , image_name)
#     train_image_paths.append(path_img)
#     train_gt_paths.append(os.path.join(gt_path , new_file))