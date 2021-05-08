# in this we will look at how to convert the text into the hand written

# for this the method text_to_handwriting is used which is in pywhatkit module

# let us first import the module

import pywhatkit

# text_to_handwriting takes the three arguments

# 1.text (that we want to convert into handwritten,we can also read from the file )

# 2.destination (path where we want to save the handwritten notes)

# 3.color (color of the handwritten ,we must provide it in rgb format)

# we should pass a tuple or list as third argument which contains the three numerical values denoting the ratio of rgb colors

#  -------------converting the text into handwritten------------

pywhatkit.text_to_handwriting("this is github repository",
                              "C:\\Users\\angaj\\OneDrive\\Desktop\\handwritten.jpeg", (10, 10, 10))

# in the second argument this is the path "C:\\Users\\angaj\\OneDrive\\Desktop" where the file saves ,and handwritten.png is the file name

# Note that the file extension should be either png or jpeg do not use other extension it does not yield desired results

# (10,10,10) tuple denotes the rgb colours


# -------------let us convert the text in file to handwritten------------

# let us read a file

file = open("C:\\Users\\angaj\\OneDrive\\Desktop\\saisri.txt", "r")

# open the file in the read mode

# let us read the contents of the file and store in a variable

text = file.read()

file.close()  # let us close the file

# now let us convert to handwritten

pywhatkit.text_to_handwriting(text,
                              "C:\\Users\\angaj\\OneDrive\\Desktop\\file_handwritten.jpeg", (10, 10, 10))
