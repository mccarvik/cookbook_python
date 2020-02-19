import re

# Need to find the shortest possible match
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
# ".*" will be greedy and find the longest possible string
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# Use "?" symbol in the regex
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))