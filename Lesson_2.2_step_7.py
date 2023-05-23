import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname("C:\\Stepik_test\\"))
file_path = os.path.join(current_dir, 'File.txt')

i = 0
f = open(file_path, 'r', encoding='utf-8').read()
s = "используется"
if s in f:
    i = i + 1

print(i)
print(f)
print(file_path)

