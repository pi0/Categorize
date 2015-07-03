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
        name, ext = os.path.splitext(full_name)
        ext = ext[1:]
        name = os.path.basename(name)
        if ext == '':
            ext = 'unknown'

        dst = os.path.join(args.dst, ext, name + '.' + ext)
        suffix = 1
        while os.path.exists(dst):
            dst = os.path.join(args.dst, ext, name + '.' + str(suffix) + '.' + ext)
            suffix += 1

        os.makedirs(os.path.join(args.dst, ext), exist_ok=True)
        if args.verbosity:
            print(full_name + ' -> ' + dst)
        try:
            shutil.move(full_name, dst)
        except:
            print('unable to move ' + full_name + ' to ' + dst)

print('Done!')
