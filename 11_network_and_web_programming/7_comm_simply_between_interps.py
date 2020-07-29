from multiprocessing.connection import Listener
import traceback

# writing an echo server
def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
    try:
        client = serv.accept()
        echo_client(client)
 
    except Exception:
        traceback.print_exc()

echo_server(('', 25000), authkey=b'peekaboo')


# connecting to server and sending various messages
from multiprocessing.connection import Client
c = Client(('localhost', 25000), authkey=b'peekaboo')
c.send('hello')
print(c.recv())
c.send(42)
print(c.recv())
c.send([1, 2, 3, 4, 5])
print(c.recv())

# ex to use a unix domain socket
s = Listener('/tmp/myconn', authkey=b'peekaboo')
# Windows named Pipe
s = Listener(r'\\.\pipe\myconn', authkey=b'peekaboo')
