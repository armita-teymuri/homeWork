from tkinter import *
import sys
# ---------------------------------------------------------
# Load words from file
lines = []
#file = open(filename, encoding="utf8")
with open(sys.path[0]+"/words.csv", encoding="utf8") as file:
    lines = file.readlines()
print(lines)
