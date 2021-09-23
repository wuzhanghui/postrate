from __future__ import division
import os
import argparse
import socket
import time

import urllib3
from douzero.evaluation.winratemulation import evaluate
import shutil
import os.path

import math
import sys
import requests
import os
import requests.packages.urllib3.util.connection as urllib3_cn
import time

def allowed_gai_family():
    """
     https://github.com/shazow/urllib3/blob/master/urllib3/util/connection.py
    """
    family = socket.AF_INET
    if urllib3_cn.HAS_IPV6:
        family = socket.AF_INET6 # force ipv6 only if it is available
    return family





def progressbar(cur,total):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ( '=' * int(math.floor(cur * 50 /total)),percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')

def setwenjian(filename):
    #上传文件到服务器
    # filename = 'rate' + str(time.time()) + '.zip'
    # zip_file = zipfile.ZipFile(filename, 'w')
    # zip_file.write('./rate/', compress_type=zipfile.ZIP_DEFLATED)
    # zip_file.close()
    file = {'file': open(filename, 'rb')}
    r = requests.post('http://[240b:250:280:cb00:6cc0:e71d:668a:cd4e]:9006//upload', files=file,data={'mima':'zheshiyigeshenqidemima'})
    print(r.text)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Dou Dizhu Evaluation')
    parser.add_argument('--landlord', type=str,
                        default='baselines/douzero_ADP/landlord_strong.ckpt')
    parser.add_argument('--landlord_up', type=str,
                        default='baselines/resnet/resnet_landlord_up_11505825900.ckpt')
    parser.add_argument('--landlord_down', type=str,
                        default='baselines/resnet/resnet_landlord_down_11505825900.ckpt')

    # parser.add_argument('--eval_data', type=str,
    #         default='eval_data_10000.pkl')
    parser.add_argument('--eval_data', type=str,
                        default='eval_data.pkl')
    parser.add_argument('--num_workers', type=int, default=1)
    parser.add_argument('--gpu_device', type=str, default='0')
    parser.add_argument('--output', type=bool, default=True)
    parser.add_argument('--bid', type=bool, default=True)
    parser.add_argument('--title', type=str, default='New')
    args = parser.parse_args()
    # args.output = True
    args.output = False
    args.bid = False

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu_device


    def writetext(a, b):
        with open("winratetest.txt", "a", encoding="utf-8") as f:
            # s = ["\n", a.split('/')[-1], ":", b.split('/')[-1], "-"]
            s = ["\n", a, ":", b, "-"]
            f.writelines(s)


    while 1:
        urllib3_cn.allowed_gai_family = allowed_gai_family
        #print(os.path.getmtime('/content/gdrive/MyDrive/data/'))
        #print(os.path.getctime('/content/gdrive/MyDrive/data/'))
        # if os.path.exists("./rate/"):
        #     shutil.rmtree("./rate/")
        # if not os.path.exists("/content/gdrive/MyDrive/data/"):
        #     os.mkdir("/content/gdrive/MyDrive/data/")
        #     os.mkdir('/content/gdrive/MyDrive/data/地上赢时局前预估/')
        #     os.mkdir('/content/gdrive/MyDrive/data/地下赢时局前预估/')
        #     os.mkdir('/content/gdrive/MyDrive/data/地主输时叫牌胜率/')
        #     os.mkdir('/content/gdrive/MyDrive/data/地主输时局前预估/')
        #     os.mkdir('/content/gdrive/MyDrive/data/地主输时三家/')
        #     os.mkdir('/content/gdrive/MyDrive/data/地主赢时叫牌胜率/')
        #     os.mkdir('/content/gdrive/MyDrive/data/地主赢时局前预估/')
        #     os.mkdir('/content/gdrive/MyDrive/data/地主赢时三家/')
        #
        # if time.time()- os.path.getmtime('/content/gdrive/MyDrive/data/') > 36000:
        #     a = input("超过10小时是否删除旧数据Y/N")
        #     if a == "Y":
        #         shutil.rmtree('/content/gdrive/MyDrive/data/')
        #         os.mkdir('/content/gdrive/MyDrive/data/地上赢时局前预估/')
        #         os.mkdir('/content/gdrive/MyDrive/data/地下赢时局前预估/')
        #         os.mkdir('/content/gdrive/MyDrive/data/地主输时叫牌胜率/')
        #         os.mkdir('/content/gdrive/MyDrive/data/地主输时局前预估/')
        #         os.mkdir('/content/gdrive/MyDrive/data/地主输时三家/')
        #         os.mkdir('/content/gdrive/MyDrive/data/地主赢时叫牌胜率/')
        #         os.mkdir('/content/gdrive/MyDrive/data/地主赢时局前预估/')
        #         os.mkdir('/content/gdrive/MyDrive/data/地主赢时三家/')
        if os.path.exists("./rate/"):
            shutil.rmtree("./rate/")
        if not os.path.exists("./zip/"):
            os.mkdir("./zip/")
        if not os.path.exists("./data/"):
            os.mkdir("./data/")
            os.mkdir('./data/地上赢时局前预估/')
            os.mkdir('./data/地下赢时局前预估/')
            os.mkdir('./data/地主输时叫牌胜率/')
            os.mkdir('./data/地主输时局前预估/')
            os.mkdir('./data/地主输时三家/')
            os.mkdir('./data/地主赢时叫牌胜率/')
            os.mkdir('./data/地主赢时局前预估/')
            os.mkdir('./data/地主赢时三家/')



        os.system("python generate_eval_data.py")
        args.landlord = 'baselines/douzero_ADP/landlord_8_12.ckpt'
        args.landlord_up = 'baselines/resnet/resnet_landlord_up.ckpt'
        args.landlord_down = 'baselines/resnet/resnet_landlord_down.ckpt'
        writetext(args.landlord, args.landlord_up)
        evaluate(args.landlord,
                 args.landlord_up,
                 args.landlord_down,
                 args.eval_data,
                 args.num_workers,
                 args.output,
                 args.bid,
                 args.title)
        # shutil.copy('./winrate.csv', './data/winrate' + str(time.time()) + '.csv')
        # shutil.copy('./farmer.csv', './data/farmer' + str(time.time()) + '.csv')

#         if not os.path.exists("./content/gdrive/data/"):
#             os.mkdir("./content/gdrive/data/")
        files = os.listdir("./rate/")
        for file in files:
            print(file)
            shutil.copy("./rate/" + file, './data/'+ file[:-4]+'/' + file[:-4] + str(time.time()) + '.csv')
        #os.system("python post.py")
        zipfile = './zip/'+str(time.time())
        shutil.make_archive(zipfile, 'zip', "./data/")
        if os.path.exists(zipfile+'.zip'):
#             try:
                setwenjian(zipfile+'.zip')
                #os.remove(zipfile+'.zip')
#             except:
#                 print("error")
#                 continue
        #os.system("pause")
        shutil.rmtree("./rate/")
        shutil.rmtree("./data/")
