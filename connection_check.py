import socket

def main():
    s = socket.socket()
    address = '127.0.0.1'
    port = 1313 
    try:
        s.connect((address, port))  
        print("Success")
    except Exception as e: 
        print("something's wrong with %s:%d. Exception is %s" % (address, port, e))
    finally:
        s.close()