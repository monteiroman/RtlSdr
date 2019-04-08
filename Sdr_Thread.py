#
#
# program with Thread
#
#

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

from DataStructure.Data import DataStructure
from GUI.SdrGui import *

from pylab import *
from rtlsdr import *

import threading
import numpy as np


style.use("ggplot")

# f = Figure(figsize=(7,3), dpi=78)
# a = f.add_subplot(111)

ANIM_INTVL = 50        # Animation Interval in mS



class SensorThread(threading.Thread):
    def setSDR (self, sample_rate, center_freq, gain):
        self.sdr = RtlSdr()
        self.sdr.sample_rate = sample_rate
        self.sdr.center_freq = center_freq
        self.sdr.gain = gain

        self.dataStruct.setParameters(sample_rate, center_freq, gain)

    def setDataStruct(self, dataStruct):
        self.dataStruct = dataStruct

    def run(self):
        while True:
            aux = fix_iq_imbalance(self.sdr.read_samples(256*1024))
            self.dataStruct.setSamples(aux)
            time.sleep(0.1)
            if self.dataStruct.getQuitState():
                break





def fix_iq_imbalance(x):
    # remove DC and save input power
    z = x - np.mean(x)
    p_in = np.var(z)

    # scale Q to have unit amplitude (remember we're assuming a single input tone)
    Q_amp = np.sqrt(2 * np.mean(x.imag**2))
    z /= Q_amp

    I, Q = z.real, z.imag

    alpha_est = np.sqrt(2 * np.mean(I**2))
    sin_phi_est = (2 / alpha_est) * np.mean(I * Q)
    cos_phi_est = np.sqrt(1 - sin_phi_est**2)

    I_new_p = (1 / alpha_est) * I
    Q_new_p = (-sin_phi_est / alpha_est) * I + Q

    y = (I_new_p + 1j * Q_new_p) / cos_phi_est

    print('phase error:', np.arccos(cos_phi_est) * 360 / 2 / np.pi, 'degrees')
    print('amplitude error:', 20 * np.log10(alpha_est), 'dB')

    return y * np.sqrt(p_in / np.var(y))





def main():
    dataStruct = DataStructure()


    mythread = SensorThread(name = "SdrThread")
    mythread.setDataStruct(dataStruct)
    mythread.setSDR(3e6, 300e6, 20)
    mythread.start()

    app = BMeasureApp(dataStruct=dataStruct)

    # ani = animation.FuncAnimation(f, animate, interval=ANIM_INTVL)

    while True:
        winUpdate (app)
        # time.sleep(0.05)

if __name__ == '__main__':
    main()
