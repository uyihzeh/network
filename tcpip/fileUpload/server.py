import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind('127.0.0.1', 8001) 
sock.listen(5)

coon, addr = sock.accept() # 阻塞

# 接收文件大小
data = conn.recv(1024)
total_file_size = int(data.decode('utf-8'))

# 接收文件内容
file_object = open('xxx.png', mode = 'wb')
recv_size = 0

while True:
    # 每次最多接受1024字节
    data = conn.recv(1024)
    file_object.write(data)
    file_object.flush()

    recv_size += len(data)
    # 上传完成
    if recv_size == total_file_size:
        break

# 接受完毕， 关闭连接
conn.close()
sock.close()


