#!/usr/bin/env python3

import argparse
import shutil
import os

parser = argparse.ArgumentParser()
parser.add_argument("src", help="source directory of files")
parser.add_argument("dst", help="destination directory to move files")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()


for root, dirs, files in os.walk(args.src):
    for file in files:
        full_name = os.path.join(root, file)
        ext = os.path.splitext(full_name)[1][1:]
        if ext == '':
            ext = 'unknown'
        dst = os.path.join(args.dst, ext)
        os.makedirs(dst, exist_ok=True)
        if args.verbosity:
            print(full_name + ' -> ' + dst)
       	try: 
            shutil.move(full_name, dst)
				except:
            print('Unable to move '+full_name+' to '+dst);

print('Done!')
