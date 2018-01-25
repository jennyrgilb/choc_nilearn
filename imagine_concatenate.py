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

#load in all the files from the glob above, then convert them from nifti1 to nifti2
ni2_funcs = (nib.Nifti2Image.from_image(nib.load(func)) for func in all_func)
#concat, this is with nibabel, but should work with nilearn too
ni2_concat = nib.concat_images(ni2_funcs, check_affines=False, axis=3)
#set the output file name
outfile=os.path.join(basepath,'concatenated_imagine_gtest.nii')
#write the file
ni2_concat.to_filename(outfile)
