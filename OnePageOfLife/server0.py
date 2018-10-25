from socket import *


def readFile0():
    '''临时测试用，程序运行时插入信息'''
    f0=open('text0.txt','rt')
    theWorld=f0.readlines()
    f0.close()
    L0=list()
    for ite in theWorld:
        ite=eval(ite)
        L0.append(ite)
    return L0
def dataAdd(userID0,psd0):
    '''注册信息判断，用户信息存储'''
    for msgUser in L:
        if msgUser['UID']==userID0:#判断用户名重复
            return 'ECHO'
    else:
        #插入用户名，密码，预置的信息
        # [{UID:userID0,PSD:psd0,STR:[msg1,msg2]},{}]
        dict0=dict()
        list0=list()
        dict0['UID']=userID0
        dict0['PSD']=psd0
        list0.append('this just a page of life in my story')
        dict0['STR']=list0
        L.append(dict0)
        return 'RSUCCESS'
def dataVerification(userID0,psd0):
    '''验证登录信息'''
    for msgUser in L:
        if msgUser['UID']==userID0:
            if msgUser['PSD']==psd0:
                return 'LSUCCESS'
    else:
        return 'LERROR'

def readSTR():
    '''从列表中提取发布文本信息'''
    # [{UID:userID0,PSD:psd0,STR:[msg1,msg2]},{}]
    ListSTR=list()
    for msgUser in L:
        for msg0 in msgUser['STR']:
            msgFinal=msgUser['UID']+":"+msg0
            ListSTR.append(msgFinal)
    else:
        #将列表转成字符串
        return str(ListSTR)

def addSTR(msgAdd0):
    '''添加发布文本  '''
    # global L
    list0=msgAdd0.split('#!~')
    UID0=list0[0]
    msg0=list0[1]
    for msgUser in L:
        if msgUser['UID']==UID0:
            msgUser['STR'].append(msg0)
            return 'ASUCCESS'
    else:
        return 'AERROR'




def serverLogin():
    #服务端登录验证并根据用户请求返回消息
    sockfd=socket(AF_INET,SOCK_STREAM,0)
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    ADDR=('0.0.0.0',26669)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    while True:
        print('wating...')
        connfd,addr=sockfd.accept()
        print('正在连接到',addr)
        #[{UID:userID0,PSD:psd0,STR:[msg1,msg2]},{}]
        #接收信息
        userID=connfd.recv(1024).decode()
        psd=connfd.recv(1024).decode()
        LorR=connfd.recv(1024).decode()
        #确认登录或注册,调用登录注册函数
        if LorR=='L':
            #登录成功后返回消息并接收客户端信息
            msg=dataVerification(userID,psd)
            connfd.send(msg.encode())
            if msg=='LSUCCESS':
                while True:
                    userAction=connfd.recv(1024).decode()
                    print('用户请求的操作为',userAction)
                    if userAction=='exit':
                        connfd.send('服务器已安全断开'.encode())
                        break
                    elif userAction=='read':
                        msgSend=readSTR()#获取到主题内容列表
                    elif userAction=='add':
                        msgAdd=connfd.recv(2048).decode()
                        msgSend=addSTR(msgAdd)
                    else:
                        #未能识别用户的请求
                        msgSend='code4'
                    connfd.send(msgSend.encode())


        elif LorR=='R':
            msg = dataAdd(userID, psd)
            print(L)
        else:
            print('未识别的信息')
            msg='MSGERROR'
        #给客户端返回登录信息
        connfd.send(msg.encode())

        # connfd.recv(1024)#1022
    sockfd.close()
L=readFile0()
serverLogin()





