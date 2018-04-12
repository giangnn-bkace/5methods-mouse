# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:24:15 2018

@author: NGN
"""

"""
Seperate dataset into Training set and Test set
Input a folder name as the folder of Test samples, other folders is Training
Run in folders' parent directory
"""

import os
import os.path
import numpy as np

class_name_alias = {"drink": "drink", "d": "drink", 
                    "eat": "eat", "e": "eat",
                    "groomback": "groom", "groom": "groom", "gb": "groom", "g": "groom",
                    "hang": "hang", "ha": "hang",
                    "head": "micromovement", "he": "micromovement",
                    "rear": "rear", "r": "rear",
                    "rest": "rest", "rs": "rest",
                    "walk": "walk", "w": "walk"}

def get_train_test_lists(test_folder_name=''):
    # Get list of all folders
    list_folders = os.listdir()
    not_folders = []
    for item in list_folders:
        if not(os.path.isdir(item)):
            not_folders.append(item)
    for item in not_folders:
        list_folders.remove(item)
    
    # If no test folder is specified, the first fold will be chosen as test folder
    if test_folder_name=='' or not(test_folder_name in list_folders):
        print("Test folder is set as the first folder by default")
        test_folder_name = list_folders[0]
    
    test_list = []
    train_list = []
    
    test_file = os.listdir(test_folder_name)
    for file in test_file:
        test_list.append(os.path.join(test_folder_name, file))
    
    for folder in list_folders:
        if folder != test_folder_name:
            train_file = os.listdir(folder)
            for file in train_file:
                train_list.append(os.path.join(folder, file))
                
    file_groups = {
            'train_'+test_folder_name: train_list,
            'test_'+test_folder_name: test_list
    }
    
    return file_groups

def move_files(file_groups):
    """This assumes all of our files are currently in _this_ directory.
    So move them to the appropriate spot. Only needs to happen once.
    """
    for group, videos in file_groups.items():
        for video in videos:
            parts = video.split(os.path.sep)
            filename = parts[1]
            name_parts = filename.split('_')
            classname = class_name_alias[name_parts[1]]
            
            
            # check if this class exists
            if not os.path.exists(os.path.join(group, classname)):
                print("Creating folder for %s%s" % (group, classname))
                os.makedirs(os.path.join(group, classname))
                
            # check if we have already move this file, or exists to move
            if not os.path.exists(video):
                print("Can't find %s to move. Skipping." % (video))
                continue
            
            # move file
            dest = os.path.join(group, classname, filename)
            print("Moving %s to %s" % (video, dest))
            os.rename(video, dest)
    
    print("Done.")
    
def main():
    group_lists = get_train_test_lists("agoutivideo320080229")
    move_files(group_lists)
    
if __name__ == '__main__':
    main()


        
    