import subprocess

# will read the output of this linux command
out_bytes = subprocess.check_output(['netstat','-a'])
out_text = out_bytes.decode('utf-8')

try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output # Output generated before error
    code = e.returncode # Return code

out_bytes = subprocess.check_output(['cmd','arg1','arg2'],
            stderr=subprocess.STDOUT)

try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'], timeout=5) # use timeout option
except subprocess.TimeoutExpired as e:
    pass

out_bytes = subprocess.check_output('grep python | wc > out', shell=True)

# Some text to send
text = b'''
hello world
this is a test
goodbye
'''

# Launch a command with pipes
p = subprocess.Popen(['wc'],
        stdout = subprocess.PIPE,
        stdin = subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
