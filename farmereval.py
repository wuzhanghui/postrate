import os 
import argparse

from douzero.evaluation.offlinesimulation import evaluate

if __name__ == '__main__':



    #新
    # parser = argparse.ArgumentParser(
    #     'Dou Dizhu Evaluation')
    # parser.add_argument('--landlord', type=str,
    #                     default='baselines/12ADP/landlord.ckpt')
    # parser.add_argument('--landlord_up', type=str,
    #                     default='baselines/12ADP/landlord_up.ckpt')
    # parser.add_argument('--landlord_down', type=str,
    #                     default='baselines/12ADP/landlord_down.ckpt')
    parser = argparse.ArgumentParser(
        'Dou Dizhu Evaluation')
    parser.add_argument('--landlord', type=str,
                        default='baselines/douzero_ADP/landlord_strong.ckpt')
    parser.add_argument('--landlord_up', type=str,
                        default='baselines/resnet/resnet_landlord_up_11505825900.ckpt')
    parser.add_argument('--landlord_down', type=str,
                        default='baselines/resnet/resnet_landlord_down_11505825900.ckpt')



    parser.add_argument('--eval_data', type=str,
            default='eval_data_10000.pkl')
    # parser.add_argument('--eval_data', type=str,
    #                     default='eval_data.pkl')
    parser.add_argument('--num_workers', type=int, default=1)
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
    def writetext(a,b):
        with open("offlinetest.txt", "a", encoding="utf-8") as f:
            # s = ["\n", a.split('/')[-1], ":", b.split('/')[-1], "-"]
            s = ["\n", a, ":", b, "-"]
            f.writelines(s)

    for i in range(4):
        # if i ==0:
        #     with open("offlinetest.txt","a",encoding="utf-8") as f:
        #
        #         f.write("12ADP landlord VS 12ADP  Farmer:")
        #     evaluate(args.landlord,
        #              args.landlord_up,
        #              args.landlord_down,
        #              args.eval_data,
        #              args.num_workers,
        #              args.output,
        #              args.bid,
        #              args.title)
        # if i ==0:
        #     # with open("offlinetest.txt","a",encoding="utf-8") as f:
        #     #
        #     #     f.write("\nstrong landlord VS 11505825900  Farmer:")
        #     #s = ["\n",args.landlord.split('/')[-1],":",args.landlord_up.split('/')[-1],"-"]
        #     writetext(args.landlord,args.landlord_up)
        #     #os.system("pause")
        #     evaluate(args.landlord,
        #              args.landlord_up,
        #              args.landlord_down,
        #              args.eval_data,
        #              args.num_workers,
        #              args.output,
        #              args.bid,
        #              args.title)
        # if i == 2:
        #     # with open("offlinetest.txt", "a", encoding="utf-8") as f:
        #     #
        #     #     f.write("STRONG landlord VS Resnet Farmer:")
        #     args.landlord = 'baselines/douzero_ADP/landlord_strong.ckpt'
        #     args.landlord_up = 'baselines/resnet/resnet_landlord_up.ckpt'
        #     args.landlord_down = 'baselines/resnet/resnet_landlord_down.ckpt'
        #     writetext(args.landlord, args.landlord_up)
        #     evaluate(args.landlord,
        #              args.landlord_up,
        #              args.landlord_down,
        #              args.eval_data,
        #              args.num_workers,
        #              args.output,
        #              args.bid,
        #              args.title)
        if i == 1:
            # with open("offlinetest.txt", "a", encoding="utf-8") as f:
            #
            #     f.write("STRONG landlord VS Resnet Farmer:")
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






        # if i == 2:
        #     # with open("offlinetest.txt", "a", encoding="utf-8") as f:
        #     #
        #     #     f.write("STRONG landlord VS STRONG Farmer:")
        #     args.landlord = 'baselines/douzero_ADP/landlord.ckpt'
        #     args.landlord_up = 'baselines/douzero_ADP/landlord_up.ckpt'
        #     args.landlord_down = 'baselines/douzero_ADP/landlord_up.ckpt'
        #     writetext(args.landlord, args.landlord_up)
        #     evaluate(args.landlord,
        #              args.landlord_up,
        #              args.landlord_down,
        #              args.eval_data,
        #              args.num_workers,
        #              args.output,
        #              args.bid,
        #              args.title)
        # if i == 3:
        #     # with open("offlinetest.txt", "a", encoding="utf-8") as f:
        #     #
        #     #     f.write("12ADP landlord VS STRONG Farmer:")
        #     args.landlord = 'baselines/12ADP/landlord.ckpt'
        #     args.landlord_up = 'baselines/douzero_ADP/landlord_up.ckpt'
        #     args.landlord_down = 'baselines/douzero_ADP/landlord_up.ckpt'
        #     writetext(args.landlord, args.landlord_up)
        #     evaluate(args.landlord,
        #              args.landlord_up,
        #              args.landlord_down,
        #              args.eval_data,
        #              args.num_workers,
        #              args.output,
        #              args.bid,
        #              args.title)
        # if i == 4:
        #     # with open("offlinetest.txt", "a", encoding="utf-8") as f:
        #     #
        #     #     f.write("STRONG landlord VS 12ADP Farmer:")
        #     args.landlord = 'baselines/douzero_ADP/landlord.ckpt'
        #     args.landlord_up = 'baselines/12ADP/landlord_up.ckpt'
        #     args.landlord_down = 'baselines/12ADP/landlord_up.ckpt'
        #     writetext(args.landlord, args.landlord_up)
        #     evaluate(args.landlord,
        #              args.landlord_up,
        #              args.landlord_down,
        #              args.eval_data,
        #              args.num_workers,
        #              args.output,
        #              args.bid,
        #              args.title)




