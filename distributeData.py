
#take all anno file text and mix it (all the lines randomly)
#create 3 new txt files, 70% train 20% valid 10% test train.txt val.txt  test.txt


import random


with open(r"mmaction2\DataSet\annotation.txt", 'r') as anno:
   lines = anno.readlines()  # Read all lines from the ano file


# Shuffle the lines randomly
random.shuffle(lines)


# Calculate the number of lines for each set
total_lines = len(lines)
test_lines = int(total_lines * 0.1)
val_lines = int(total_lines * 0.2)
train_lines = total_lines - test_lines - val_lines


# Open train, val, and test files for writing
with open(r"mmaction2\DataSet\train.txt", 'w') as train_file, \
       open(r"mmaction2\DataSet\val.txt", 'w') as val_file, \
       open(r"mmaction2\DataSet\test.txt", 'w') as test_file:
   # Write lines to each file based on the calculated number of lines
   for i, line in enumerate(lines):
       if i < test_lines:
           test_file.write(line)
       elif i < test_lines + val_lines:
           val_file.write(line)
       else:
           train_file.write(line)
