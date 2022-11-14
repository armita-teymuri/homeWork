from tkinter import *
import sys

# ---------------------------------------------------------
# Load words from file
lines = []
with open(sys.path[0]+"/words.csv", encoding="utf8") as file:
    lines = file.readlines()
print(lines)

# ---------------------------------------------------------
# Make a cleaner dict (IS LIKE a JSON) from our list of lines
words = {}
for line in lines:
    line = line.replace("\n", "")
    key, value = line.split(",")
    words[key] = value
print(words)

# ---------------------------------------------------------
# Function to translate


def translate():
    word = text_box.get()  # Get the text from text_box like "input.value"
    word = word.strip()  # This is to clean spaces around the word just like ".trim()"
    if word in words.keys():  # Check if word exists in our dictionary
        trans_label.config(text=words[word])
    else:
        trans_label.config(text="")


# ---------------------------------------------------------
# Make a window and set the dimensions
win = Tk()
win.geometry("300x100")
win.title("Dictionary")

# ---------------------------------------------------------
# Make a label
label = Label(text="Enter word")
label.pack()

# ---------------------------------------------------------
# Make a place to enter a text
text_box = Entry()
text_box.pack()

# ---------------------------------------------------------
# Make a button to translate a file
button = Button(text="Translate", command=translate)
button.pack()

# ---------------------------------------------------------
# Make a label to show the translation
trans_label = Label(text="")
trans_label.pack()

# ---------------------------------------------------------
# Show the window of our application
win.mainloop()