# import re
# str0='asda司机9856#!~666阿斯达····wda~~~'
# pattern="(.*)#!~"
# UID=re.findall(pattern,str0)
# print(UID[0])
#
# print(str0.split('#!~'))
# L=[{'UID': '666', 'PSD': '666', 'STR': ['this just a page of life in my story']}]


def dataAdd(userID0,psd0):

    for msgUser in L:
        if msgUser['UID']==userID0:
            return 'ECHO'
    else:

        # [{UID:userID0,PSD:psd0,STR:[msg1,msg2]},{}]
        dict0=dict()
        list0=list()
        dict0['UID']=userID0
        dict0['PSD']=psd0
        list0.append('this just a page of life in my story')
        dict0['STR']=list0
        strDict='\n'+str(dict0)
        f0=open('text0.txt','at')
        f0.write(strDict)


        return 'RSUCCESS'

def read0():
    f0=open('text0.txt','rt')
    theWorld=f0.readlines()
    f0.close()
    L0=[]
    for ite in theWorld:
        ite=eval(ite)
        L0.append(ite)
    return L0
L=read0()

dataAdd('11111111','000')







#
# {'UID': 'INDEXxiaoxia', 'PSD': '666', 'STR': ['this just a page of life in my story']}
# {'UID': 'Memorij', 'PSD': '666', 'STR': ['Oh my fucking god!']}
# {'UID': 'Xx1', 'PSD': '666', 'STR': ['hello world!']}