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

style.use("ggplot")

# f = Figure(figsize=(7,3), dpi=78)
# a = f.add_subplot(111)

ANIM_INTVL = 1000        # Animation Interval in mS



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
            self.dataStruct.setSamples(self.sdr.read_samples(256*1024))
            # time.sleep(0.05)
            if self.dataStruct.getQuitState():
                break



def main():
    dataStruct = DataStructure()


    mythread = SensorThread(name = "SdrThread")
    mythread.setDataStruct(dataStruct)
    mythread.setSDR(3e6, 98.5e6, 10)
    mythread.start()

    app = BMeasureApp(dataStruct=dataStruct)

    # ani = animation.FuncAnimation(f, animate, interval=ANIM_INTVL)

    while True:
        winUpdate (app)
        time.sleep(0.05)

if __name__ == '__main__':
    main()
