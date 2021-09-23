from __future__ import division

import math
import sys
import requests
import os
import zipfile
import time

from werkzeug.sansio.multipart import MultipartEncoder


def progressbar(cur,total):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ( '=' * int(math.floor(cur * 50 /total)),percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')

def setwenjian():
    #上传文件到服务器
    filename = 'rate' + str(time.time()) + '.zip'
    zip_file = zipfile.ZipFile(filename, 'w')
    zip_file.write('./rate/',compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    file = {'file': open(filename ,'rb')}
    r = requests.post('http://[240b:250:280:cb00:8171:63df:dae6:187b]:5000/upload', files=file,data={'mima':'zheshiyigeshenqidemima'})
    print(r.text)


if __name__ == '__main__':

    setwenjian()
