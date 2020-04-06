#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:14:41 2019

@author: moon
"""

import argparse
import os
from selenium import webdriver


URL = 'https://pracuj.pl/praca/'


def PreprocessURL(keywords, location=None):
    global URL
    
    if URL[-1] != "/":
        URL += "/"
        
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
    driver = webdriver.Firefox(executable_path='path/to/geckodriver')
    driver.get(URL)
    result_list = driver.find_elements_by_class_name("results__list-container-item")
    QueryResults = [] 
    for res in result_list:
        attributes = res.text.split(sep='\n')
        attributes = list(filter(lambda x: x not in ['Zobacz profil', 'Super oferta'], attributes))
        link = res.find_element_by_class_name('offer__click-area').get_property('href')
        
        storeAttributes = dict()
        storeAttributes['Title'] = attributes[0]
        storeAttributes['Company'] = attributes[1]
        storeAttributes['Info'] = attributes[2:-2]
        storeAttributes['DatePublished'] = attributes[-2].split(sep=":")[1].strip()
        storeAttributes['Link'] = link
        QueryResults.append(storeAttributes)          
        
    driver.quit()
    
    return QueryResults
def PrettyPrint(results):
    for res in results:
        for key in res:
            print(key, '\n', res[key])
        print(2*'\n')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="MoonScraper", 
                                 description="Specify Location of job offer and Keywords")
    parser.add_argument('-l', '--loc', type=str, help='Location of work offer')
    parser.add_argument('-k', '--keywords', action='append', type=str, help='Main keywords')
    parser.add_argument('-sp' ,'--savepath', type=str, help='path to save directory')
    args = parser.parse_args()
    result = SeleniumActions(PreprocessURL(args.keywords, location=args.loc))
    if args.savepath:
        save_dir = os.path.dirname(args.save_path)
        if os.path.isfile(args.savepath):
            print("File with that name already exists!")
        
        elif not os.path.exists(save_dir):
                print(f"Save directory doesn't exist. Making {save_dir}")
                os.makedirs(save_dir)            
        with open(args.savepath, 'w') as file:
            file.write(result)
        
    PrettyPrint(result)

    
