"""
By Kami Bigdely
Remove control flag
Reference: https://stackoverflow.com/a/10140333/81306
This code snippet reads up to the end of the file
"""

n = 16
with open('foobar.file', 'rb') as fp:
    chunk = fp.read(n)
    while chunk != '':
        print(chunk) # process(chunk)
        chunk = fp.read(n)