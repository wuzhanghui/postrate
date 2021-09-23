import os 
import argparse

from douzero.evaluation.offlinesimulation import evaluate

if __name__ == '__main__':



    #新
    parser = argparse.ArgumentParser(
        'Dou Dizhu Evaluation')
    parser.add_argument('--landlord', type=str,
                        default='baselines/resnet/landlord_9772187500.ckpt')
    parser.add_argument('--landlord_up', type=str,
                        default='baselines/resnet/resnet_landlord_up.ckpt')
    parser.add_argument('--landlord_down', type=str,
                        default='baselines/resnet/resnet_landlord_down.ckpt')


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
        if i ==0:
            with open("offlinetest.txt","a",encoding="utf-8") as f:
                #f.write("resnet test：-----------------\n")
                f.write("Resnet landlord VS Resnet Farmer:")



            evaluate(args.landlord,
                     args.landlord_up,
                     args.landlord_down,
                     args.eval_data,
                     args.num_workers,
                     args.output,
                     args.bid,
                     args.title)
        if i == 1:
            with open("offlinetest.txt", "a", encoding="utf-8") as f:
                # f.write("Resnet landlord ：ADP Farmer-----\n")
                f.write("Resnet landlord VS ADP    Farmer:")
            args.landlord = 'baselines/resnet/landlord_9772187500.ckpt'
            args.landlord_up = 'baselines/ADP/landlord_up.ckpt'
            args.landlord_down = 'baselines/ADP/landlord_down.ckpt'
            evaluate(args.landlord,
                     args.landlord_up,
                     args.landlord_down,
                     args.eval_data,
                     args.num_workers,
                     args.output,
                     args.bid,
                     args.title)

        if i == 2:
            with open("offlinetest.txt", "a", encoding="utf-8") as f:
                #f.write("ADP Test-----------\n")
                f.write("ADP    landlord VS ADP    Farmer:")
            args.landlord = 'baselines/ADP/landlord.ckpt'
            args.landlord_up = 'baselines/ADP/landlord_up.ckpt'
            args.landlord_down = 'baselines/ADP/landlord_down.ckpt'
            evaluate(args.landlord,
                     args.landlord_up,
                     args.landlord_down,
                     args.eval_data,
                     args.num_workers,
                     args.output,
                     args.bid,
                     args.title)
        if i == 3:
            with open("offlinetest.txt","a",encoding="utf-8") as f:
                #f.write("ADP landlord ：Resnet Farmer-----\n")
                f.write("ADP    landlord VS Resnet Farmer:")
            args.landlord = 'baselines/ADP/landlord.ckpt'
            args.landlord_up = 'baselines/resnet/resnet_landlord_up.ckpt'
            args.landlord_down = 'baselines/resnet/resnet_landlord_down.ckpt'
            evaluate(args.landlord,
                     args.landlord_up,
                     args.landlord_down,
                     args.eval_data,
                     args.num_workers,
                     args.output,
                     args.bid,
                     args.title)


