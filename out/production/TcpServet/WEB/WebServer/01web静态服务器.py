import socket
def main():
    # 1、创建服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用，程序退出，端口立即释放-----socket.SOL_SOCKET对当前套接字
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 2、绑定地址
    tcp_server_socket.bind(("", 8888))
    # 3、设置监听
    tcp_server_socket.listen(128)
    while True:
        # 接收客户端连接-----有客户端连接时，通信套接字，和客户端ip,port
        new_socket, ip_port = tcp_server_socket.accept()

        # 接收数据
        rece_data = new_socket.recv(4096)
        #判断接收的数据是否为0
        if len(rece_data)==0:
            new_socket.close()
            return
        rece_content=rece_data.decode("utf-8")


        #对数据按照空格进行分割
        request_list = rece_content.split(" ",maxsplit=2)
        #获取请求资源路径
        requset_path = request_list[1]
        #判断请求是否根目录，如果是根目录，则设置返回信息
        if requset_path == "/":
            requset_path = "/index.html"
        #os.path.exists("static/" + requset_path)
        try:
            #打开文件读取文件中的数据，用rb模式是为了兼容打开图片
            with open("./static"+requset_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            # 返回404状态信息
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Server: PWS/1.0\r\n"
            #读取404页面信息
            with open("./static/error.html", "rb") as file:
                file_data = file.read()
            response_body = file_data
            # 把数据封装成http响应报文格式数据
            response = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            # 发送给浏览器的数据必须为二进制
            new_socket.send(response)

        else:
            # 响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Server: PWS/1.0\r\n"
            # 响应体
            response_body = file_data
            # 把数据封装成http响应报文格式数据
            response = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            # 发送给浏览器的数据必须为二进制
            new_socket.send(response)
        finally:
            # 关闭服务于客户端的套接字
            new_socket.close()

if __name__ == '__main__':
    main()