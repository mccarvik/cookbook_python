import os
import textwrap


s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

# textwrap decides where the text wraps on a print
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
# indents first line
print (textwrap.fill(s, 40, initial_indent='     '))
# indents all subsequent lines 
print (textwrap.fill(s, 40, subsequent_indent='     '))

# gets the default column length
print(os.get_terminal_size().columns)