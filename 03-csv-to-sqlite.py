#!/usr/bin/env python3
#Usage: ./03-csv-to-sqlite.py
from icecream import ic
import my_db_utils
from config import CONFIG

db_name = f"{CONFIG['database_dir']}/{CONFIG['db_file']}"
table_name = CONFIG['table_name_1']
csv_dir = CONFIG['csv_dir']
csv_file = f'{csv_dir}/{table_name}.csv'

my_db_utils.csv_to_sqlite(db_name, table_name, csv_file)
