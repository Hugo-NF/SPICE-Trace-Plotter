import numpy as np
import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot(data, options=None):
        fig, ax1 = plt.subplots()

        ax1.set_xlabel('Tempo (s)')
        ax1.set_ylabel('Tensão (V)')
        ax1.plot(data['time'], data['V(vin)'], marker='', color='blue', linewidth=1, alpha=0.9, label='Vin')
        ax1.plot(data['time'], data['V(vout)'], marker='', color='green', linewidth=1, alpha=0.9, label='Vout')
        ax1.tick_params(axis='y')
        ax1.legend(loc=1)
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        ax2.set_ylabel('Corrente (A)')  # we already handled the x-label with ax1
        ax2.plot(data['time'], data['I(R1)'], marker='', color='red', linewidth=1, alpha=0.9, label='I(R1)')
        ax2.tick_params(axis='y')

        fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # otherwise the right y-label is slightly clipped
        ax2.legend(loc=2)
        plt.title('Conversor Boost')
        fig.savefig('boost.png')
        plt.show()
