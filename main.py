import time
import xlrd
import os, json
import pandas as pd


def read(f):
    with open(f, 'r', encoding="utf-8") as f:
        return json.load(f)


def get_files(path):
    arr = os.listdir(path)
    return [path + p for p in arr]


'''******************************************************************************************************************'''

total = 0
for file in get_files('./native/'):
    words = read(file)
    total += len(words)

print(total)

