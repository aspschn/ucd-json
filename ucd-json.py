#!/usr/bin/env python3
'''
ucd-json.py

Author:     Yujeonja <hardboiled65@gmail.com>
Created:    2019. 11. 02. 15:30
Copyright (c) 2019-2021 Yujeonja. All rights reserved.
'''
import os
import shutil
import argparse
from argparse import ArgumentParser
import zipfile
import json

import parsers
from ucd_files import ucd_files

UNICODE_VERSION = '14.0.0'
EMOJI_VERSION = '14.0'

UCD_URL = "http://www.unicode.org/Public/{}/ucd/"
EMOJI_URL = "http://www.unicode.org/Public/emoji/{}/"

UCD_DATA_BASEDIR = 'data/'
EMOJI_DATA_BASEDIR = 'data/emoji/'


def has_data(version):
    '''Check if UCD data has been downloaded.'''
    base_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(base_dir, UCD_DATA_BASEDIR)
    data_path = os.path.join(data_dir, version, 'UCD.zip')
    return os.path.isfile(data_path)

def has_emoji_data(version):
    '''Check if Emoji data has been downloaded.'''
    base_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(base_dir, EMOJI_DATA_BASEDIR)
    data_path = os.path.join(data_dir, version, 'emoji-data.txt')
    return os.path.isfile(data_path)

def download_data(unicode_version, emoji_version):
    # Get the data dirs.
    base_dir = os.path.dirname(os.path.realpath(__file__))
    ucd_data_base_dir = os.path.join(base_dir, UCD_DATA_BASEDIR)
    emoji_data_base_dir = os.path.join(base_dir, EMOJI_DATA_BASEDIR)

    # Download UCD data.
    os.system('mkdir -p ' + os.path.join(ucd_data_base_dir, unicode_version))
    cmd = 'wget https://www.unicode.org/Public/{}/ucd/UCD.zip'.format(
        unicode_version)
    cmd += ' -O ' + os.path.join(ucd_data_base_dir, unicode_version, 'UCD.zip')
    os.system(cmd)

    # Download emoji data.
    emoji_dir = os.path.join(emoji_data_base_dir, emoji_version)
    os.system('mkdir -p ' + emoji_dir)

    url = EMOJI_URL.format(emoji_version) + 'emoji-data.txt'
    cmd = 'wget ' + url + ' -O ' + os.path.join(emoji_dir, 'emoji-data.txt')
    os.system(cmd)

    url = EMOJI_URL.format(emoji_version) + 'emoji-sequences.txt'
    cmd = 'wget ' + url + ' -O ' + os.path.join(emoji_dir, 'emoji-sequences.txt')
    os.system(cmd)

    url = EMOJI_URL.format(emoji_version) + 'emoji-test.txt'
    cmd = 'wget ' + url + ' -O ' + os.path.join(emoji_dir, 'emoji-test.txt')
    os.system(cmd)

    url = EMOJI_URL.format(emoji_version) + 'emoji-variation-sequences.txt'
    cmd = 'wget ' + url + ' -O ' + os.path.join(emoji_dir, 'emoji-variation-sequences.txt')
    os.system(cmd)

    url = EMOJI_URL.format(emoji_version) + 'emoji-zwj-sequences.txt'
    cmd = 'wget ' + url + ' -O ' + os.path.join(emoji_dir, 'emoji-zwj-sequences.txt')
    os.system(cmd)

def unzip_data(unicode_version, emoji_version):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    # Unzip UCD.
    ucd_zip_path = os.path.join(base_dir, UCD_DATA_BASEDIR, unicode_version,
        'UCD.zip')
    ucd_zip = zipfile.ZipFile(ucd_zip_path)
    ucd_zip.extractall(path=os.path.dirname(ucd_zip_path))

def read_data(data_type, file_name, unicode_version, emoji_version):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = ''
    if data_type == 'ucd':
        file_path = os.path.join(base_dir, UCD_DATA_BASEDIR, unicode_version,
            file_name)
    elif data_type == 'emoji':
        file_path = os.path.join(base_dir, EMOJI_DATA_BASEDIR, emoji_version,
            file_name)
    f = open(file_path, 'r')
    d = f.read()
    f.close()
    return d


if __name__ == '__main__':
    argp = ArgumentParser(
        prog='./ucd-json',
        description='Convert UCD text format to JSON.'
    )
    argp.add_argument('file', type=str, nargs='?', default=None,
        help='One of file inside data directory.')
    argp.add_argument('--unicode-version', metavar='VERSION', type=str,
        default=UNICODE_VERSION)
    argp.add_argument('--emoji-version', metavar='VERSION', type=str,
        default=EMOJI_VERSION)
    argp.add_argument('-l', '--list', action='store_true',
        help='List all UCD files. Regardless specified version.')

    args = argp.parse_args()

    # print(args.file)
    # print(args.list)

    # -l, --list
    if args.list == True:
        print('\n'.join(ucd_files.keys()))
        exit(0)

    # Main

    if not (has_data(args.unicode_version) and has_emoji_data(args.emoji_version)):
        download_data(args.unicode_version, args.emoji_version)
        unzip_data(args.unicode_version, args.emoji_version)
    if args.file != None:
        ucd_file = ucd_files[args.file]
        data = read_data(ucd_file['type'],
            args.file,
            args.unicode_version,
            args.emoji_version)
        parser_cls = ucd_files[args.file]['parser']
        if parser_cls is None:
            print('Parser for "' + args.file + '" is not implemented.')
            exit(1)
        parser = parser_cls()
        py_dict = parser.parse(data)
        json_string = json.dumps(py_dict, indent=2)
        print(json_string)
