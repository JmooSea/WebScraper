#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:14:41 2019

@author: moon
"""

import requests
from bs4 import BeautifulSoup
import argparse
import os


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


def SoupActions(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    offers = soup.find_all(name="offer-details__text")
    
    return offers
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="MoonScraper", 
                                 description="Specify Location and Keywords to get info")
    parser.add_argument('-l', '--loc', type=str, help='Location of work offer')
    parser.add_argument('-k', '--keywords', action='append', type=str, help='Main keywords')
    parser.add_argument('-sp' ,'--savepath', type=str, help='path to save directory')
    args = parser.parse_args()
    print(args)
    if args.savepath:
        save_dir = os.path.dirname(args.save_path)
        if not os.path.exists(save_dir):
                print(f"Save directory doesn't exist. Making {save_dir}")
                os.makedirs(save_dir)
    print(SoupActions(PreprocessURL(URL)))

    