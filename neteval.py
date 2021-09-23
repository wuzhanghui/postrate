import os 
import argparse
from douzero.evaluation.simulation import evaluate
import os
import time
import random
import client_helper
import shutil
import hashlib
import torch
from douzero.dmc.models import Model
start = 1
if __name__ == '__main__':
    #while(1):
        updating = False
        global models
        models = {}
        model = Model(device="cpu")
        models["cpu"] = model
        def update_model(ver, urls, force):
            global model_version, models, updating
            if updating:
                return
            updating = True
            if model_version != ver or force:
                print("检测到模型更新")
                if len(urls) > 0:
                    url = urls[random.randint(0, len(urls) - 1)]
                else:
                    print("模型更新失败：没有有效的模型地址")
                    updating = False
                    return
                print("更新中，请耐心等待")
                st = time.time()
                weights = client_helper.download_pkl(url)
                if weights is not None:
                    model_version = ver
                    for position in ["landlord", "landlord_up", "landlord_down"]:
                        models["cpu"].get_model(position).load_state_dict(weights[position])
                        torch.save(weights[position], "./models/" + position + ".ckpt")
                    with open("./model_version.txt", "w") as f:
                        f.write(str(model_version))
                    print("更新模型成功！耗时: %.1f s" % (time.time() - st))
                else:
                    print("更新模型失败！")
            updating = False


        def load_actor_models():
            global model_version, models
            if os.path.exists("./model_version.txt"):
                with open("./model_version.txt", "r") as f:
                    model_version = int(f.read())
            print("初始化，正在获取服务器版本")
            model_info = client_helper.get_model_info()
            if model_info is not None:
                print("版本获取完成，服务器版本:", model_info["version"])
                update_model(model_info["version"], model_info["urls"], False)
            else:
                print("服务器版本获取失败，更新模型失败")
                return
            if not (os.path.exists("./models/landlord.ckpt") and os.path.exists(
                    "./models/landlord_up.ckpt") and os.path.exists("./models/landlord_down.ckpt") and os.path.exists(
                "./models/bidding.ckpt")):
                update_model(model_info["version"], model_info["urls"], True)


        load_actor_models()
        file_name = "./models/landlord.ckpt"
        with open(file_name, 'rb') as fp:
            data = fp.read()
        file_md5 = hashlib.md5(data).hexdigest()
        print("新md5:"+file_md5)
        with open("md5.txt") as fd:
            md = fd.readline()
            print("旧md5:"+md)
        # if file_md5 != md:
        #     with open("md5.txt", "w", encoding="utf-8") as f:
        #         f.write(file_md5)
            #print("done")
        #os.system("pause")
        if file_md5 != md:
        #if file_md5 == md:
            if os.path.exists("./model_version.txt"):
                    with open("./model_version.txt", "r") as f:
                        frames = int(f.read())
            shutil.copy('./models/landlord.ckpt','./baselines/resnet/resnet_landlord_'+ str(frames) + '.ckpt')
            shutil.copy('./models/landlord_down.ckpt', './baselines/resnet/resnet_landlord_down_' + str(frames) + '.ckpt')
            shutil.copy('./models/landlord_up.ckpt', './baselines/resnet/resnet_landlord_up_' + str(frames) + '.ckpt')
            resnetlandlord = 'baselines/resnet/resnet_landlord_'+ str(frames) + '.ckpt'
            resnetlandlord_up ='baselines/resnet/resnet_landlord_up_' + str(frames) + '.ckpt'
            resnetlandlord_down ='baselines/resnet/resnet_landlord_down_' + str(frames) + '.ckpt'
            #os.system("pause")
            #新
            parser = argparse.ArgumentParser(
                'Dou Dizhu Evaluation')
            parser.add_argument('--landlord', type=str,
                                default=resnetlandlord)
            parser.add_argument('--landlord_up', type=str,
                                default=resnetlandlord_up)
            parser.add_argument('--landlord_down', type=str,
                                default=resnetlandlord_down)


            parser.add_argument('--eval_data', type=str,
                    default='eval_data.pkl')
            parser.add_argument('--num_workers', type=int, default=2)
            parser.add_argument('--gpu_device', type=str, default='0')
            parser.add_argument('--output', type=bool, default=True)
            parser.add_argument('--bid', type=bool, default=True)
            parser.add_argument('--title', type=str, default='New')
            args = parser.parse_args()
            #args.output = True
            args.output = False
            args.bid = False

            os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
            os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu_device
            for i in range(4):
                # if i ==0:
                #     with open("test.txt","a",encoding="utf-8") as f:
                #         #f.write("resnet test：-----------------\n")
                #         s=[str(frames),"\n","Resnet landlord VS Resnet Farmer:"]
                #         # f.write("Resnet landlord VS Resnet Farmer:")
                #         f.writelines(s)
                #     print(str(frames))
                #     print("Resnet landlord VS Resnet Farmer:",end='')
                #     id = "Resnet landlord VS Resnet Farmer.csv"
                #
                #     evaluate(args.landlord,
                #              args.landlord_up,
                #              args.landlord_down,
                #              args.eval_data,
                #              args.num_workers,
                #              args.output,
                #              args.bid,
                #              args.title,id,frames)
                #     #os.system('cls')
                if start == 1:
                    with open("test.txt", "a", encoding="utf-8") as f:
                        f.write("ADP Test-----------\n")
                        f.write("ADP    landlord VS ADP    Farmer:")
                    print("ADP    landlord VS ADP    Farmer:", end='')
                    id = "ADP"
                    args.landlord = 'baselines/douzero_ADP/landlord.ckpt'
                    args.landlord_up = 'baselines/douzero_ADP/landlord_up.ckpt'
                    args.landlord_down = 'baselines/douzero_ADP/landlord_down.ckpt'
                    starttime = time.time()
                    evaluate(args.landlord,
                             args.landlord_up,
                             args.landlord_down,
                             args.eval_data,
                             args.num_workers,
                             args.output,
                             args.bid,
                             args.title, id, frames)
                    start = 0
                    end = time.time()
                    print(end - starttime)
                    #os.system('pause')

                if i == 0:
                    with open("test.txt", "a", encoding="utf-8") as f:
                        # f.write("Resnet landlord ：ADP Farmer-----\n")
                        s=["\n",str(frames),"\n","Resnetlandlord : ADPFarmer - "]
                        f.writelines(s)
                        #f.write("Resnetlandlord : ADPFarmer -- ")
                    print("Resnetlandlord : ADPFarmer - ",end='')
                    id = "Resnet landlord VS ADP    Farmer.csv"
                    args.landlord = resnetlandlord
                    args.landlord_up = 'baselines/douzero_ADP/landlord_up.ckpt'
                    args.landlord_down = 'baselines/douzero_ADP/landlord_down.ckpt'
                    starttime = time.time()
                    evaluate(args.landlord,
                             args.landlord_up,
                             args.landlord_down,
                             args.eval_data,
                             args.num_workers,
                             args.output,
                             args.bid,
                             args.title,id,frames)
                    #os.system('cls')
                    end = time.time()
                    print(end - starttime)

                if i == 1:
                    with open("test.txt","a",encoding="utf-8") as f:
                        #f.write("ADP landlord ：Resnet Farmer-----\n")
                        f.write("ADPlandlord : "+str(frames)+"farmer")
                    print("ADPlandlord : ResnetFarmer - ",end='')
                    id = "ADP    landlord VS Resnet Farmer.csv"
                    args.landlord = 'baselines/douzero_ADP/landlord.ckpt'
                    args.landlord_up = resnetlandlord_up
                    args.landlord_down = resnetlandlord_down
                    starttime = time.time()
                    evaluate(args.landlord,
                             args.landlord_up,
                             args.landlord_down,
                             args.eval_data,
                             args.num_workers,
                             args.output,
                             args.bid,
                             args.title,id,frames)
                if i == 2:
                    with open("test.txt", "a", encoding="utf-8") as f:
                        f.write("STRONG landlord VS Resnet Farmer:")
                    id = 0
                    args.landlord = 'baselines/douzero_ADP/landlord.ckpt'
                    args.landlord_up = 'baselines/resnet/resnet_landlord_up.ckpt'
                    args.landlord_down = 'baselines/resnet/resnet_landlord_down.ckpt'
                    evaluate(args.landlord,
                             args.landlord_up,
                             args.landlord_down,
                             args.eval_data,
                             args.num_workers,
                             args.output,
                             args.bid,
                             args.title,id,frames)
                if i == 3:
                    with open("test.txt", "a", encoding="utf-8") as f:
                        f.write("STRONG landlord VS STRONG Farmer:")
                    id = 0
                    args.landlord = 'baselines/douzero_ADP/landlord.ckpt'
                    args.landlord_up = 'baselines/douzero_ADP/landlord_up.ckpt'
                    args.landlord_down = 'baselines/douzero_ADP/landlord_up.ckpt'
                    evaluate(args.landlord,
                             args.landlord_up,
                             args.landlord_down,
                             args.eval_data,
                             args.num_workers,
                             args.output,
                             args.bid,
                             args.title,id,frames)

                    #os.system('cls')
                    end = time.time()
                    print(end-starttime)
            with open("md5.txt", "w", encoding="utf-8") as f:
                f.write(file_md5)
            #os.system("pause")
        else:
            print("权重相同，等待5分钟")
            time.sleep(300)


