import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    @staticmethod
    def plot(data, options):
        fig, ax1 = plt.subplots()
        plots = []
        ax1.set_xlabel(options['x_axis']['label'])
        ax1.set_ylabel(options['y_axis']['left']['label'])

        scaler = lambda m: m * options['x_axis']['transform']
        np_scaler = np.vectorize(scaler)
        data['time'] = np_scaler(data['time'])

        for trace in options['traces']['left'].keys():
            scaler = lambda m: m * options['y_axis']['left']['transform']
            np_scaler = np.vectorize(scaler)
            data[trace] = np_scaler(data[trace])

            plots.append(ax1.plot(data['time'],
                                  data[trace],
                                  marker=options['traces']['left'][trace]['marker'],
                                  color=options['traces']['left'][trace]['color'],
                                  linewidth=1,
                                  alpha=0.9,
                                  label=options['traces']['left'][trace]['label']))
        ax1.tick_params(axis='y')

        if options['two_scales']:
            ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
            ax2.set_ylabel(options['y_axis']['right']['label'])  # we already handled the x-label with ax1
            for trace in options['traces']['right'].keys():
                scaler = lambda m: m * options['y_axis']['right']['transform']
                np_scaler = np.vectorize(scaler)
                data[trace] = np_scaler(data[trace])

                plots.append(ax2.plot(data['time'],
                                      data[trace],
                                      marker=options['traces']['right'][trace]['marker'],
                                      color=options['traces']['right'][trace]['color'],
                                      linewidth=1,
                                      alpha=0.9,
                                      label=options['traces']['right'][trace]['label']))
            ax2.tick_params(axis='y')

            fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # otherwise the right y-label is slightly clipped

        plt.title(options['title'])
        fig.savefig(options['output'])
        plt_sum = []
        for plot in plots:
            plt_sum += plot
        labels = [label.get_label() for label in plt_sum]
        ax1.legend(plt_sum, labels, loc=0)
        plt.show()
