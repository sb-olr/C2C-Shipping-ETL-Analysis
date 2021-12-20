#!/usr/bin/env python3
# Usage: ./04-database-view.py
from icecream import ic
import my_db_utils
from config import CONFIG

db_name = f"{CONFIG['database_dir']}/{CONFIG['db_file']}"
table_name = CONFIG['table_name_1']

data = my_db_utils.get_100_records(db_name, table_name)
ic(data)
