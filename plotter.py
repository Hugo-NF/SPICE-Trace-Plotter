import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot(data, options=None):
        fig, ax1 = plt.subplots()
        color = 'tab:blue'
        ax1.set_xlabel('Tempo (s)')
        ax1.set_ylabel('Tensão (V)')
        ax1.plot(data['time'], data['V(vin)'])
        ax1.plot(data['time'], data['V(vout)'])
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        color = 'tab:red'
        ax2.set_ylabel('Corrente (A)', color=color)  # we already handled the x-label with ax1
        ax2.plot(data['time'], data['I(R1)'], color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        plt.show()
