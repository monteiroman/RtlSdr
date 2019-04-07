# Tkinter imports
import tkinter as tk
from tkinter import ttk, font
from tkinter import *
from PIL import ImageTk, Image

# Matplotlib imports
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import time

LARGE_FONT = ("Verdana", 24)
MEDIUM_FONT = ("Verdana", 18)
SMALL_FONT = ("Verdana", 14)
style.use("ggplot")

f = Figure(figsize=(7,3), dpi=78)
a = f.add_subplot(111)

BFIELDSCREEN = 1
ACCSCREEN = 2
SPLASHTIME = 1
GRAPHLENGTH = 50         # Quantity of points in the x axis of thee graph
ANIM_INTVL = 1000



class BMeasureApp(tk.Tk):

    def __init__(self, dataStruct):
        self.tk = tk.Tk()

        # self.tk.attributes("-fullscreen", True)
        self.tk.title("SDR Spectrum Analyzer")

        container = tk.Frame(self.tk)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        frame =  MeasurePage(container, self, dataStruct)
        self.frames[MeasurePage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        time.sleep(SPLASHTIME)
        self.show_frame(MeasurePage)

        self.ani = self.frames[MeasurePage].getAni()

        self.dataStruct = dataStruct



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quitProgram (self):
        self.tk.destroy()
        self.dataStruct.setQuitState()

    # def holdMeasure (self):
    #     if self.holdStatus:
    #         self.holdStatus = False
    #     else:
    #         self.holdStatus = True
    #
    # def getHoldStatus (self):
    #     return self.holdStatus
    #
    # def setLSMZeros (self):
    #     self.dataStruct.setZeros()
    #
    # def saveBtnClicked (self):
    #     self.dataStruct.setSaveDataStatus(True)



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        s = ttk.Style()
        s.configure('my.TButton', font=("Verdana", 16))

        label = tk.Label(self, text="Medidor de Campo B", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text=
            "Trabajo Practico realizado para la materia Medidas Electrónicas I",
             font=MEDIUM_FONT)
        label.pack(pady=10,padx=10)
        label = tk.Label(self, text=
            "de la facultad regional Buenos Aires de la UTN.", font=MEDIUM_FONT)
        label.pack(pady=10,padx=10)

        # If we want the start button
        #button = ttk.Button(self, text="Ir al medidor", style='my.TButton',
                            #command=lambda: controller.show_frame(MeasurePage))
        #button.pack()

        # self.img = ImageTk.PhotoImage(
        #         Image.open("/home/pi/BField_Accel_Meter/sources/pictures/logo1.png"))
        # self.panel = Label(self, image = self.img)
        # self.panel.pack()


# class SelectMeasurePage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#
#         s = ttk.Style()
#         s.configure('my.TButton', font=("Verdana", 16))
#
#         self.fooXSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooXSpacer.grid(row=0, column=0, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=0, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=1, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=2, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=3, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=5, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=6, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=8, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=9, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=10, column=1, sticky="nsew")
#         self.fooYSpacer = ttk.Label(self, text="                                ", font=MEDIUM_FONT)
#         self.fooYSpacer.grid(row=11, column=1, sticky="nsew")
#
#         self.buttonB = ttk.Button(self, text="Ir al medidor de campo B", style='my.TButton',
#                             command=lambda: controller.show_frame(MeasurePage, BFIELDSCREEN))
#         self.buttonB.grid(row=4, column=1, sticky="nsew")
#         self.buttonG = ttk.Button(self, text="Ir al medidor de aceleración", style='my.TButton',
#                             command=lambda: controller.show_frame(MeasurePage, ACCSCREEN))
#         self.buttonG.grid(row=7, column=1, sticky="nsew")
#         self.exitButton = ttk.Button(self, text="Salir", style='my.TButton',
#                             command=lambda: controller.quitProgram())
#         self.exitButton.grid(row=12, column=1, sticky="nsew")
#
#         # self.img = ImageTk.PhotoImage(Image.open("/home/pi/BField_Accel_Meter/sources/pictures/logo1.png"))
#         # self.panel = Label(self, image = self.img)
#         # self.panel.pack()
#



class MeasurePage(tk.Frame):

    def __init__(self, parent, controller, dataStruct):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.dataStruct = dataStruct

        s = ttk.Style()
        s.configure('my.TButton', font=("Verdana", 16))

        self.msg_Title = StringVar()
        self.msg_Title.set("Campo B")
        self.label = ttk.Label(self, textvariable=self.msg_Title, font=MEDIUM_FONT)
        self.label.grid(row=0, column=0, sticky="n")

        self.valuesFrame = tk.Frame(self)
        self.valuesFrame.grid(row=1, column=0, sticky="nsew")

        self.msg_x = StringVar()
        self.msg_x.set("---")
        self.msg_y = StringVar()
        self.msg_y.set("---")
        self.msg_z = StringVar()
        self.msg_z.set("---")
        self.msg_mod = StringVar()
        self.msg_mod.set("---")
        self.msg_xpp = StringVar()
        self.msg_xpp.set("---")
        self.msg_ypp = StringVar()
        self.msg_ypp.set("---")
        self.msg_zpp = StringVar()
        self.msg_zpp.set("---")
        self.msg_freq = StringVar()
        self.msg_freq.set("---")
        self.msg_saveStatus = StringVar()
        self.msg_saveStatus.set("---")

        self.separator = ttk.Label(self.valuesFrame,
                            text="_____________________", font=MEDIUM_FONT)
        self.separator.grid(row=1, column=0, sticky="nsew")
        self.labelX = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_x, font=MEDIUM_FONT)
        self.labelX.grid(row=2, column=0, sticky="nsew")
        self.labelY = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_y, font=MEDIUM_FONT)
        self.labelY.grid(row=3, column=0, sticky="nsew")
        self.labelZ = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_z, font=MEDIUM_FONT)
        self.labelZ.grid(row=4, column=0, sticky="nsew")
        self.labelMod = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_mod, font=MEDIUM_FONT)
        self.labelMod.grid(row=5, column=0, sticky="nsew")
        self.separator = ttk.Label(self.valuesFrame,
                            text="_____________________", font=MEDIUM_FONT)
        self.separator.grid(row=6, column=0, sticky="nsew")
        self.labelXPp = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_xpp, font=MEDIUM_FONT)
        self.labelXPp.grid(row=7, column=0, sticky="nsew")
        self.labelYPp = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_ypp, font=MEDIUM_FONT)
        self.labelYPp.grid(row=8, column=0, sticky="nsew")
        self.labelZPp = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_zpp, font=MEDIUM_FONT)
        self.labelZPp.grid(row=9, column=0, sticky="nsew")
        self.labelFreq = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_freq, font=MEDIUM_FONT)
        self.labelFreq.grid(row=10, column=0, sticky="nsew")
        self.holdButton = ttk.Button(self.valuesFrame, text="Hold",
                            padding=(5,5), style='my.TButton',
                            command=lambda: controller.holdMeasure())
        self.holdButton.grid(row=11, column=0, sticky="nsew")
        self.measureButton = ttk.Button(self.valuesFrame, text="Guardar mediciones",
                            padding=(5,5), style='my.TButton',
                            command=lambda: controller.saveBtnClicked())
        self.measureButton.grid(row=12, column=0, sticky="nsew")
        self.saveStatusLabel = ttk.Label(self.valuesFrame,
                            textvariable=self.msg_saveStatus, font=SMALL_FONT)
        self.saveStatusLabel.grid(row=13, column=0, sticky="nsew")
#---------------

        mCanvas = FigureCanvasTkAgg(f, self)
        mCanvas.draw()
        mCanvas.get_tk_widget().grid(row=1, column=1, sticky="nsew")

        self.ani = animation.FuncAnimation(f, animate, interval=ANIM_INTVL, fargs=(dataStruct,))

        self.exitButton = ttk.Button(self, text="Salir", padding=(5,5),
                            style='my.TButton',
                            command=lambda: controller.quitProgram())
        self.exitButton.grid(row=2, column=0, sticky="nsew")
        # self.setZeroButton = ttk.Button(self, text="Setear ceros", padding=(5,5),
        #                     style='my.TButton',
        #                     command=lambda: controller.setLSMZeros())
        # self.setZeroButton.grid(row=2, column=1, sticky="nsew")

    def refreshLabel (self, type):
        axis = self.controller.dataStruct.getAxis()
        pp = self.controller.dataStruct.getPpValues()

        if type == BFIELDSCREEN:
            self.msg_Title.set("Campo B")
            self.msg_x.set(" X: {:.2f}".format(axis[0]) + " uT")
            self.msg_y.set(" Y: {:.2f}".format(axis[1]) + " uT")
            self.msg_z.set(" Z: {:.2f}".format(axis[2]) + " uT")
            self.msg_mod.set(" Mod: {:.2f}".format(axis[3]) + " uT")
            self.msg_xpp.set(" Xpp: {:.2f}".format(pp[0]) + " uT")
            self.msg_ypp.set(" Ypp: {:.2f}".format(pp[1]) + " uT")
            self.msg_zpp.set(" Zpp: {:.2f}".format(pp[2]) + " uT")

        if type == ACCSCREEN:
            self.msg_Title.set("Aceleracion")
            self.msg_x.set(" X: {:.3f}".format(axis[4]) + " G")
            self.msg_y.set(" Y: {:.3f}".format(axis[5]) + " G")
            self.msg_z.set(" Z: {:.3f}".format(axis[6]) + " G")
            self.msg_mod.set(" Mod: {:.3f}".format(axis[7]) + " G")
            self.msg_xpp.set(" Xpp: {:.3f}".format(pp[3]) + " G")
            self.msg_ypp.set(" Ypp: {:.3f}".format(pp[4]) + " G")
            self.msg_zpp.set(" Zpp: {:.3f}".format(pp[5]) + " G")

        self.msg_freq.set(" Frec: {:.0f}".format(self.controller.dataStruct.getSamplingRate()) + " HZ")

        if self.controller.dataStruct.getSaveDataStatus():
            self.msg_saveStatus.set("   Guardando...")
        else:
            self.msg_saveStatus.set("   Listo para guardar")

    def getAni (self):
        return self.ani                                                         #have to return ani in order to mantain her and not be collected by the garbage collector

    def setDataStruct (data):
        self.dataStruct = data

def winUpdate (app):
    app.update_idletasks()
    app.update()


def animate(i, data):
    a.clear()
    sample_rate, center_freq, gain = data.getParameters()
    a.psd(data.getSamples(), NFFT=256, Fs=sample_rate/1e6, Fc=center_freq/1e6)
    # a.xlabel('Frequency (MHz)')
    # a.ylabel('Relative power (dB)')


    # a.plot(dataStruct.getSamples)



    # a.plot(dataStruct.timeGraphList, dataStruct.xGraphList,
    #     dataStruct.timeGraphList, dataStruct.yGraphList,
    #     dataStruct.timeGraphList, dataStruct.zGraphList)
    # a.legend(("Eje X", "Eje Y", "Eje Z"), loc="upper right")
    # a.set_title("Campo B en eje Z")
    # a.set(xlabel='Tiempo [S]', ylabel='[uT]')
    # a.axis(ymin=0, ymax=53)




def dataGraph (axis, timeStamp):

    x_axis = axis[0]
    y_axis = axis[1]
    z_axis = axis[2]
    tmp = float(timeStamp.seconds + (timeStamp.microseconds / 1000000))

    if len(dataStruct.timeGraphList) <= GRAPHLENGTH:
        dataStruct.timeAppend(tmp)
        #z_axis_g=float('%.1f'%z_axis)									#set decimals to a requested value for graph
        #dataStruct.zAppend(z_axis_g)
        dataStruct.xAppend(abs(x_axis))
        dataStruct.yAppend(abs(y_axis))
        dataStruct.zAppend(abs(z_axis))


    else:
        dataStruct.popTimeList()
        dataStruct.timeAppend(tmp)
        dataStruct.popXList()
        dataStruct.popYList()
        dataStruct.popZList()
        #z_axis_g=float('%.1f'%z_axis)                                  #set decimals to a requested value for graph
        #dataStruct.zAppend(z_axis_g)
        dataStruct.xAppend(abs(x_axis))
        dataStruct.yAppend(abs(y_axis))
        dataStruct.zAppend(abs(z_axis))
