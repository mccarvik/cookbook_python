import sys
# error
# sys.stdout.write(b'Hello\n')
# simply write the byte data to the files underlying buffer
sys.stdout.buffer.write(b'Hello\n')