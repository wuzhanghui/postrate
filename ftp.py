from ftplib import FTP
import time
import tarfile
import shutil
import os


def ftpconnect(host, username, password):
    ftp = FTP()
    ftp.set_pasv(0)
    ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    ftp.encoding = "utf-8"
    return ftp


def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR  ' + remotepath, fp.write, bufsize)
    # 接受服务器上文件并写入文本
    ftp.set_debuglevel(0)  # 关闭调试
    fp.close()  # 关闭文件


def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # 上传文件
    ftp.set_debuglevel(0)
    # fp.seek(0)
    fp.close()


if __name__ == "__main__":
    path = './rate/'
    f0, f1, f2, f3, f4, f5 = 0, 0, 0, 0, 0, 0
    print(f1)
    try:
        ftp0 = ftpconnect("[240b:250:280:cb00:8171:63df:dae6:187b]", "rate", "")
        uploadfile(ftp0, "./下赢用上模型局前预估/" + "下赢用上模型局前预估" + str(time.time()) + ".csv", path + "下赢用上模型局前预估.csv")
        ftp0.quit()
    except:
        f0 = 1
    try:
        ftp2 = ftpconnect("[240b:250:280:cb00:8171:63df:dae6:187b]", "rate", "")
        uploadfile(ftp2, "./地上赢时局前预估/" + "地上赢时局前预估" + str(time.time()) + ".csv", path + "地上赢时局前预估.csv")
        ftp2.quit()
    except:
        f2 = 1
    try:
        ftp1 = ftpconnect("[240b:250:280:cb00:8171:63df:dae6:187b]", "rate", "")
        uploadfile(ftp1, "./地主赢时叫牌胜率/" + "地主赢时叫牌胜率" + str(time.time()) + ".csv", path + "地主赢时叫牌胜率.csv")
        ftp1.quit()
    except:
        f1 = 1
    try:
        ftp3 = ftpconnect("[240b:250:280:cb00:8171:63df:dae6:187b]", "rate", "")
        uploadfile(ftp3, "./地主赢时局前预估/" + "地主赢时局前预估" + str(time.time()) + ".csv", path + "地主赢时局前预估.csv")
        ftp3.quit()
    except:
        f3 = 1
    try:
        ftp4 = ftpconnect("[240b:250:280:cb00:8171:63df:dae6:187b]", "rate", "")
        uploadfile(ftp4, "./地主输时叫牌胜率/" + "地主输时叫牌胜率" + str(time.time()) + ".csv", path + "地主输时叫牌胜率.csv")
        ftp4.quit()
    except:
        f4 = 1
    try:
        ftp5 = ftpconnect("[240b:250:280:cb00:8171:63df:dae6:187b]", "rate", "")
        uploadfile(ftp5, "./地主输时局前预估/" + "地主输时局前预估" + str(time.time()) + ".csv", path + "地主输时局前预估.csv")
        ftp5.quit()
    except:
        f5 = 1
    if f0 != 1 and f1 != 1 and f2 != 1 and f3 != 1 and f4 != 1 and f5 != 1:
        shutil.rmtree("./rate/")
        print(f0,f1,f2,f3,f4,f5)
        #os.system("pause")
        shutil.copytree("./sample", "./rate/")
