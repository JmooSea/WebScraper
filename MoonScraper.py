#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:14:41 2019

@author: moon
"""

import argparse
import os
from selenium import webdriver



URL = 'https://pracuj.pl/praca'



def PreprocessURL(keywords, location=None):
    global URL
    if len(keywords) > 1:
        keywords = "-x44-".join(keywords)
    else:
        keywords = keywords[0]
    URL += keywords + ';kw/'
    if location:
        URL += location + ';wp/'
    
    return URL


def SeleniumActions(URL):
    
    #define your own path to the driver
    driver = webdriver.Firefox(executable_path='/home/moon/Downloads/Projekty_prog/WebScraper/geckodriver')
    driver.get(URL)
    result_list = driver.find_elements_by_class_name("results__list-container-item")
    QueryResults = [] 
    for res in results:
        attributes = res.text.split(sep='\n')
        link = res.find_element_by_class_name('offer__click-area').get_property('href')
        
        storeAttributes = dict()
        storeAttributes['Title'] = attributes[0]
        storeAttributes['Company'] = attributes[2]
        storeAttributes['Location']
        storeAttributes['Info'] = attributes[4:-2]
        storeAttributes['DatePublished'] = attributes[-2]
        QueryResults.append(storeAttributes)          
        
    driver.quit()
    
    return QueryResults

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="MoonScraper", 
                                 description="Specify Location of job offer and Keywords")
    parser.add_argument('-l', '--loc', type=str, help='Location of work offer')
    parser.add_argument('-k', '--keywords', action='append', type=str, help='Main keywords')
    parser.add_argument('-sp' ,'--savepath', type=str, help='path to save directory')
    args = parser.parse_args()
    result = SeleniumActions(PreprocessURL(URL))
    if args.savepath:
        save_dir = os.path.dirname(args.save_path)
        if os.path.isfile(args.savepath):
            print("File with that name already exists!")
        
        elif not os.path.exists(save_dir):
                print(f"Save directory doesn't exist. Making {save_dir}")
                os.makedirs(save_dir)            
        with open(args.savepath, 'w') as file:
            file.write(result)
        
    print(result)

    