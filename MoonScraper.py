#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:14:41 2019

@author: moon
"""

import requests
from bs4 import BeautifulSoup
import argparse


URL = 'https://pracuj.pl/praca'

soup = BeautifulSoup(page.content, 'html.parser')

def PreprocessURL(location=None, keywords):
    global URL
    if len(keywords) > 1:
        keywords = "-x44-".join(keywords)
    else:
        keywords = keywords[0]
    URL += kwywords + ';kw/'
    if location:
        URL += location + ';wp/'
    
    return URL

def 
    
        
    
    
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="MoonScraper", 
                                 description="Specify Location and Keywords to get info")
parser.add_argument('-l', '--loc', type=str, help='Location of work offer')
parser.add_argument('-k', '--keyword', action='append' type=str, help='Main keywords')
parser.add_argument('-sp' ,'--savepath', type=str, help='path to save directory')
args = parser.parse_args()
