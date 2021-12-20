#!/usr/bin/env python3

import pandas as pd
import os
import csv
import shutil
from icecream import ic
from config import CONFIG

data_dir = CONFIG['data_dir']
csv_dir = CONFIG['csv_dir']
processed_dir = CONFIG['processed_dir']


def get_list_from_csv(csv_name, skip_header=True):
    with open(csv_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)
        if skip_header:
            data = data[1:]
        return data


def make_dir_if_not_exists(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)


def get_filenames(dirname, ext='.json'):
    files = []
    for f in sorted(os.listdir(dirname)):
        if f.endswith(ext):
            files.append(f'{dirname}/{f}')

    return files


def move_to_archive(files, dirname, data_dir=data_dir):
    archive_folder = f'{data_dir}/{dirname}/{processed_dir}'

    make_dir_if_not_exists(archive_folder)

    for filename in files:
        shutil.move(filename, archive_folder)


def generate_csv_files(data_dir=data_dir, archive=False):
    try:
        sub_folders = sorted(os.listdir(data_dir))
        if not sub_folders:
            ic(f'no sub folders found in {data_dir}')
    except FileNotFoundError:
        ic(f'Data dir {data_dir} not found')
        return 0

    make_dir_if_not_exists(csv_dir)

    for dirname in sub_folders:
        files = get_filenames(f'{data_dir}/{dirname}')
        if files:
            df = pd.DataFrame()
            for filename in files:
                df1 = pd.read_json(filename, lines=True)
                df = pd.concat([df, df1], ignore_index=True)
                ic(f'added {filename}')
            ic(f'Shape of {dirname} is {df.shape}')
            df.to_csv(f'{csv_dir}/{dirname}.csv', index=False)
            if archive:
                ic('Archiving...')
                move_to_archive(files, dirname)
        else:
            ic(f'No files in sub-folder: {dirname}')
    return


if __name__ == '__main__':
    generate_csv_files(archive=True)
