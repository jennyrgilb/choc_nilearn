# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:57:37 2017

@author: nibl
"""

#this imports all the commands needed for the script to work#
import os
import numpy as np
import nilearn
import matplotlib
import glob
import nibabel as nib
from nilearn.image import concat_imgs, index_img, smooth_img
from nilearn.image import resample_to_img

#set basepath
basepath=os.path.join('/projects','niblab','data','eric_data','W1','imagine')

#make a list of the files to concat
all_func = glob.glob(os.path.join(basepath,'level1_grace_edit','cs*++.feat','filtered_func_data.nii.gz'))
print(all_func)

#contat files via nilearn concatenate function
output= concat_imgs(all_func, memory_level=0, auto_resample=True, verbose=0)
outfile=os.path.join(basepath,'concatenated_imagine.nii.gz')
nib.save(output, outfile) 
