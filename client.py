import socket
import time
host = '127.0.0.1'
port = 0

server = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)


#prepare for run
#at the beggining of method it is known server is currently free
#method run until server return state ready
#client sends PFR (preapre for run) request to server
#in response client expects RDY (ready)
def prepare_for_run():
    print("[INF] Server is available")
    while 1:
        print("[INF] Sending prepare for run request to server!")
        s.sendto(b'PFR', server)
        msg = get_state()
        if msg == b'RDY':
            print("[SUCCESS] Server status changed to 'RDY' as expected!")
            break
        else:
            print("[WARNING] Actual server status is not 'RDY'")
    return True


#execute run
#execute tests (?) (?) (?) ..
def execute_run():
    s.sendto(b'TEST', server)
    print("[INF] Executing...")
    test0()
    cleanup()


#cleanup
#method running until cleanup is complete
#client sends CLEAN request to server
#client get actual server status
#if it is FREE then break while-loop
def cleanup():
    print("[INF] Test cleanup is running...")
    while 1:
        s.sendto(b'CLEAN', server)
        msg = get_state()
        if msg == b'FREE':
            print("[SUCCESS] Serves status changed to 'FREE' as expected!")
            break
        else:
            print("[WARNING] Actual server status is not 'FREE'")


#get state
#client sends STATE request to server to get server actual state
#time sleep is set to 0.2 because of tcp freeze (ad. can be found in python documantion)
def get_state():
    print("[INF] Sending get state request to server")
    s.sendto(b'STATE', server)
    time.sleep(0.2)
    try:
        return s.recv(1024)
    except:
        pass


#close socket
#method close connection with server in case of error
def close_socket():
    print("[WARNING] Socket is going to be closed...")
    s.close()


#main
#running all the time due to need of listening connected port constantly
#method gets return message from another method and compares it with known responses
#free - server does not run any tests and is not affected by error
#rdy (ready) - server was informed by client that tests will be run and waiting for them
#busy - server is running tests
#err (error) - server is affected by error
#else - any other unknown message appered
def main():
    while 1:
        msg = get_state()
        if msg == b'FREE':
            prepare_for_run()
        elif msg == b'RDY':
            execute_run()
        elif msg == b'BUSY':
            print("[WARNING] Server is currently busy!")
        elif msg == b'ERR':
            print("[WARNING] Server returned ERR Code!")
        else:
            print("[WARNING] Unknown response from server!")
        time.sleep(3)

#TESTS
def test0():
    time.sleep(5)
    print("PASSED")


main()
