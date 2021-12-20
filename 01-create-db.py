#!/usr/bin/env python3
# Usage: ./01-create-db.py
import my_db_utils
from config import CONFIG

db_name = f"{CONFIG['database_dir']}/{CONFIG['db_file']}"
table_name = CONFIG['table_name_1']
table_fields = CONFIG['table_fields_1']

my_db_utils.create_table(db_name, table_name, table_fields)
