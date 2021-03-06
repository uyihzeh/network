import socket

# 1.监听本机IP端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind('127.0.0.1', 8001) # IP, 端口
sock.listen(5) #支持排队5人

while True:
    # 2.等待， 有人来连接
    conn, addr = sock.appept() # 等待客户端来连接

    # 3.等待， 连接者发送消息
    client_dada = conn.recv(1024) # 等待接受客户端发来数据
    print(client_dada.decode('utf-8')) # 字节

    # 4.给连接者回复消息
    conn.sendall("hello world".encode('utf-8'))

    # 5.关闭连接
    conn.close()

# 6.停止服务端程序
sock.close()

