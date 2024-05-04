# This is about file I/O in Python.
#
# File I/O:
#
# File I/O (input/output) is a way of reading and writing data to and from files. Python provides built-in functions for reading and writing files. You can open a file using the open() function, read data from a file using the read() method, write data to a file using the write() method, and close a file using the close() method. For example:

# Open a file
file = open('example.txt', 'w')

# Write data to the file
file.write('Hello, World!')

# Close the file
file.close()
# In the above example, we open a file named example.txt in write mode ('w'). We write the string 'Hello, World!' to the file using the write() method. Finally, we close the file using the close() method.

# You can also open a file in read mode ('r') to read data from a file. For example:

# Open a file
file = open('example.txt', 'r')

# Read data from the file
data = file.read()

# Close the file
file.close()
# In the above example, we open a file named example.txt in read mode ('r'). We read the data from the file using the read() method and store it in the variable data. Finally, we close the file using the close() method.

# You can also open a file in append mode ('a') to append data to the end of a file. For example:

# Open a file
file = open('example.txt', 'a')

# Append data to the file
file.write('\nHello, Python!')

# Close the file
file.close()

# In the above example, we open a file named example.txt in append mode ('a'). We append the string 'Hello, Python!' to the end of the file using the write() method. Finally, we close the file using the close() method.

# You can also open a file in binary mode ('b') to read or write binary data to a file. For example:

# Open a file in binary mode
file = open('example.bin', 'wb')

# Write binary data to the file
file.write(b'\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21') 

# Close the file
file.close()

# In the above example, we open a file named example.bin in binary write mode ('wb'). We write the binary data b'\x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21' to the file using the write() method. Finally, we close the file using the close() method.

# You can also use the with statement to open a file. The with statement automatically closes the file when the block of code is exited. For example:

# Open a file using the with statement
with open('example.txt', 'r') as file:
    # Read data from the file
    data = file.read()

# The file is automatically closed when the block of code is exited
# In the above example, we open a file named example.txt in read mode ('r') using the with statement. We read the data from the file using the read() method and store it in the variable data. The file is automatically closed when the block of code is exited.

# You can also read data from a file line by line using the readlines() method. For example:

# Open a file
file = open('example.txt', 'r')

# Read data from the file line by line
for line in file.readlines():
    print(line)

# Close the file
file.close()
# In the above example, we open a file named example.txt in read mode ('r'). We read the data from the file line by line using the readlines() method and print each line to the console. Finally, we close the file using the close() method.

# You can also use the readline() method to read data from a file line by line. For example:

# Open a file
file = open('example.txt', 'r')

# Read data from the file line by line

while True:
    line = file.readline()
    if not line:
        break
    print(line)
    
# Close the file
file.close()

# In the above example, we open a file named example.txt in read mode ('r'). We read the data from the file line by line using the readline() method and print each line to the console. We use a while loop to read the file line by line until there are no more lines to read. Finally, we close the file using the close() method.

# You can also use the writelines() method to write a list of lines to a file. For example:

# Open a file
file = open('example.txt', 'w')

# Write a list of lines to the file
lines = ['Hello, World!\n', 'Hello, Python!\n']
file.writelines(lines)

# Close the file
file.close()

# In the above example, we open a file named example.txt in write mode ('w'). We write a list of lines ['Hello, World!\n', 'Hello, Python!\n'] to the file using the writelines() method. Finally, we close the file using the close() method.

# You can also use the seek() method to change the current file position. For example:

# Open a file
file = open('example.txt', 'r')

# Read the first 5 characters from the file
data = file.read(5)
print(data)

# Change the current file position to the beginning of the file
file.seek(0)

# Read the entire file
data = file.read()
print(data)

# Close the file
file.close()

# In the above example, we open a file named example.txt in read mode ('r'). We read the first 5 characters from the file using the read() method and store it in the variable data. We change the current file position to the beginning of the file using the seek() method. We read the entire file using the read() method and print it to the console. Finally, we close the file using the close() method.

# You can also use the tell() method to get the current file position. For example:             

# Open a file
file = open('example.txt', 'r')

# Read the first 5 characters from the file
data = file.read(5)
print(data)


# Get the current file position
position = file.tell()
print(position)

# Close the file
file.close()

# In the above example, we open a file named example.txt in read mode ('r'). We read the first 5 characters from the file using the read() method and store it in the variable data. We get the current file position using the tell() method and store it in the variable position. Finally, we close the file using the close() method.

# You can also use the truncate() method to truncate the file to a specified size. For example:

# Open a file
file = open('example.txt', 'r+')

# Truncate the file to 10 bytes
file.truncate(10)

# Close the file
file.close()

# In the above example, we open a file named example.txt in read/write mode ('r+'). We truncate the file to 10 bytes using the truncate() method. Finally, we close the file using the close() method.

# You can also use the flush() method to flush the internal buffer to the file. For example:

# Open a file   
file = open('example.txt', 'w')

# Write data to the file
file.write('Hello, World!')

# Flush the internal buffer to the file
file.flush()

# Close the file
file.close()

# In the above example, we open a file named example.txt in write mode ('w'). We write the string 'Hello, World!' to the file using the write() method. We flush the internal buffer to the file using the flush() method. Finally, we close the file using the close() method.

# You can also use the readable() method to check if a file is readable. For example:

# Open a file
file = open('example.txt', 'r')

# Check if the file is readable
result = file.readable()
print(result)

# Close the file
file.close()

# In the above example, we open a file named example.txt in read mode ('r'). We check if the file is readable using the readable() method and store the result in the variable result. Finally, we close the file using the close() method.

# You can also use the writable() method to check if a file is writable. For example:

# Open a file
file = open('example.txt', 'w')

# Check if the file is writable
result = file.writable()
print(result)

# Close the file
file.close()

# In the above example, we open a file named example.txt in write mode ('w'). We check if the file is writable using the writable() method and store the result in the variable result. Finally, we close the file using the close() method.

# You can also use the seekable() method to check if a file is seekable. For example:

# Open a file
file = open('example.txt', 'r')

# Check if the file is seekable
result = file.seekable()
print(result)

# Close the file
file.close()

# In the above example, we open a file named example.txt in read mode ('r'). We check if the file is seekable using the seekable() method and store the result in the variable result. Finally, we close the file using the close() method.

