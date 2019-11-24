import socket
import threading


serverIp = input('input server ip:')
port = input('input server port:')
nickname = input('input nickname:')


s = socket.socket(AF_INET,SOCK_STREAM)
conn = s.connect((serverIp,port))
conn.send(nickname)


outData = ''
#socket接受
def threadRecv(conn):
    global outData
    while Ture:
        inData = conn.recv(1024)
        if not inData:
            break
        if outData == indata:
            break
        else:
            print(date)



#socket发送
def threadSend(conn):
    while True:
        outData = raw_input()
        outData = nickname + ':' + outData
        print(outData)
        conn.send(outData)


#接受发送线程
threadSen = threading.Thread(target=threadSend,args=(s,))
threadSen.start()
threadRec = threading.Thread(target=threadRecv,args=(s,))
threadRec.start()
