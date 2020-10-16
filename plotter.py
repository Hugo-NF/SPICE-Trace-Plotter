import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot(data, options):
        fig, ax1 = plt.subplots()
        plots = []
        ax1.set_xlabel(options['x_label'])
        ax1.set_ylabel(options['y_label'])
        for trace in options['traces'].keys():
            if options['traces'][trace]['scale'] == 'n':
                plots.append(ax1.plot(data['time'],
                                      data[trace],
                                      marker=options['traces'][trace]['marker'],
                                      color=options['traces'][trace]['color'],
                                      linewidth=1,
                                      alpha=0.9,
                                      label=options['traces'][trace]['label']))
        ax1.tick_params(axis='y')

        if options['scales'] == 'y':
            ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
            ax2.set_ylabel(options['right_y_label'])  # we already handled the x-label with ax1
            for trace in options['traces'].keys():
                if options['traces'][trace]['scale'] == 'y':
                    plots.append(ax2.plot(data['time'],
                                          data[trace],
                                          marker=options['traces'][trace]['marker'],
                                          color=options['traces'][trace]['color'],
                                          linewidth=1,
                                          alpha=0.9,
                                          label=options['traces'][trace]['label']))
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
