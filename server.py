import socket


host='127.0.0.1'
port=5000


def get_free_port():
    while 1:
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.bind(('', 0))
            a, p = tcp.getsockname()
            tcp.close()
            print("Server found free port to run on: ", port)
            break
        except:
            print("[WARNING] ")


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

server_status = "FREE"

print("[INF] Server started on port", port)
print("[INF] Current server status " + server_status)

while 1:
    try:
        if server_status != "BUSY":
            data, addr = s.recvfrom(1024)
            print(str(addr) + ": :" + str(data))
            if data == b'STATE':
                s.sendto(server_status.encode(), addr)
            elif data == b'PFR':
                server_status = "RDY"
            elif data == b'TEST':
                server_status = "BUSY"
                print("[INF] Executing tests...")
            else:
                print("[WARNING] Unknown response from client!")
        else:
            data, addr = s.recvfrom(1024)
            print(str(addr) + ": :" + str(data))
            if data == b'STATE':
                print("[INF] Sending BUSY status to client!")
                s.sendto(b'BUSY', addr)
            elif data == b'CLEAN':
                server_status = "FREE"
                print(">CLEAN SUCCESSFULL")
        print("[SERVER STATUS] " + server_status)
    except:
        pass
s.close()