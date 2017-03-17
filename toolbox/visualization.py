import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


def plot_history(path):
    prefix = path.rsplit('.', maxsplit=1)[0]
    df = pd.read_csv(path)
    epoch = df['epoch']
    for metric in ['Loss', 'PSNR']:
        train = df[metric.lower()]
        val = df['val_' + metric.lower()]
        plt.figure()
        plt.plot(epoch, train, label='train')
        plt.plot(epoch, val, label='val')
        plt.legend(loc='best')
        plt.xlabel('Epoch')
        plt.ylabel(metric)
        plt.savefig('.'.join([prefix, metric.lower(), 'png']))
        plt.close()
