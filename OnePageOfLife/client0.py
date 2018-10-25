from socket import *
from time import *


def clientLogin(userID0,psd0,loginRegister):
    '''
        1.创建套接字并建立连接
        2.将用户名密码以及初始消息发送给服务端
        3.向服务端发送不同的请求
    '''
    sockfd=socket()
    sockfd.connect(('127.0.0.1',26669))
    sockfd.send(userID0.encode())#发送账号
    sleep(0.1)
    sockfd.send(psd0.encode())#发送密码
    sleep(0.1)
    sockfd.send(loginRegister.encode())#发送登录or注册
    msgSever=sockfd.recv(1024).decode()
    if msgSever=='ECHO':
        print('用户名重复')
    elif msgSever=='RSUCCESS':
        print('注册成功')
    elif msgSever=='LSUCCESS':
        print('登录成功')
        while True:
            #登录成功后循环发送请求
            msgRequest=input('read||add||exit>>')
            sockfd.send(msgRequest.encode())#发送请求
            # print(readRead)
            if msgRequest=='exit':
                msgRecv=sockfd.recv(1024).decode()
                print(msgRecv+'\nBye~')
                break
            elif msgRequest=='read':
                readRead = sockfd.recv(1024).decode()#接收返回的信息
                #处理服务端返回的主题列表并整理输出
                msgReadClean(readRead)
            elif msgRequest=='add':
                #进行主题发布操作
                msgadd=input('内容>>')
                msgSend=userID0+'#!~'+msgadd
                sockfd.send(msgSend.encode())#发送发布的内容和用户id到服务器
                msgRecv=sockfd.recv(1024).decode()#等待接收服务端的消息
                print(msgRecv)
            else:
                msgRecv=sockfd.recv(1024).decode()
                print(msgRecv)



    elif msgSever=='LERROR':
        print('登录失败')
    else:
        print('code3')
    sockfd.close()
    # return msgSever

def msgReadClean(msg0):
    '''将字符串转回列表遍历输出'''
    msg0=eval(msg0)
    for msgClean in msg0:
        print(msgClean)




userID=input('账号：')
psd=input('密码：')
loginRegister=input('L||R>>')
clientLogin(userID,psd,loginRegister)
# print(clientLogin(userID,psd,loginRegister))