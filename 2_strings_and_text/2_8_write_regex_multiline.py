import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
              multiline comment */
'''

# re wont find new lines
print(comment.findall(text1))
print(comment.findall(text2))

# add new line capabilities
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# DOTALL flag make "." match all characters including newlines
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment.findall(text2))
