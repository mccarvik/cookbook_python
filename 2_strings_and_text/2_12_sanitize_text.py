import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# create translation table
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}

a = s.translate(remap)
print(a)

# removes all combining characters
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

# maps unicode to equivalent ascii
digitmap = { c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
# arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# can use encode + decode functions
print(a)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))

# fast simple way yo clean up whitespace
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s