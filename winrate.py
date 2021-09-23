from __future__ import division
import os
import argparse
import time
from douzero.evaluation.winratemulation import evaluate
import shutil
import os.path



import math
import sys
import requests
import os
import zipfile
import time




def progressbar(cur,total):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ( '=' * int(math.floor(cur * 50 /total)),percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')

def setwenjian():
    #上传文件到服务器
    filename = 'data'+str(time.time())+'.zip'
    zip_file = zipfile.ZipFile(filename, 'w')
    zip_file.write('app.py',compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    file = {'file': open(filename,'rb')}
    r = requests.post('http://[240b:250:280:cb00:8171:63df:dae6:187b]/upload', files=file,data={'mima':'zheshiyigeshenqidemima'})
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
#         files = os.listdir("./rate/")
#         for file in files:
#             print(file)
#             shutil.copy("./rate/" + file, '/content/gdrive/MyDrive/data/'+ file[:-4]+'/' + file[:-4] + str(time.time()) + '.csv')
        #os.system("python post.py")
        setwenjian()
        shutil.rmtree("./rate/")
