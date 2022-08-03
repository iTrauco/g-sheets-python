#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gspread 

sa = gspread.service_account()
sh = sa.open("bq")

wks = sh.worksheet("Projects")

print('Rows ', wks.row_count)
print('Cols ', wks.col_count)

print(wks.acell('L13').value)

print(wks.get('L13:L'))
