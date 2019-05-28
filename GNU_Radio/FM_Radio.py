#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM Radio
# Generated: Tue May 28 09:19:07 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class FM_Radio(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FM Radio")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FM Radio")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "FM_Radio")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.width = width = 1e6
        self.volume = volume = 1
        self.seek = seek = 0
        self.sample = sample = 500e3
        self.samp_rate = samp_rate = 2e6
        self.freq = freq = 90.2e6
        self.cutoff = cutoff = 1e3

        ##################################################
        # Blocks
        ##################################################
        self.Tabs = Qt.QTabWidget()
        self.Tabs_widget_0 = Qt.QWidget()
        self.Tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tabs_widget_0)
        self.Tabs_grid_layout_0 = Qt.QGridLayout()
        self.Tabs_layout_0.addLayout(self.Tabs_grid_layout_0)
        self.Tabs.addTab(self.Tabs_widget_0, 'input')
        self.Tabs_widget_1 = Qt.QWidget()
        self.Tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tabs_widget_1)
        self.Tabs_grid_layout_1 = Qt.QGridLayout()
        self.Tabs_layout_1.addLayout(self.Tabs_grid_layout_1)
        self.Tabs.addTab(self.Tabs_widget_1, 'output')
        self.top_layout.addWidget(self.Tabs)
        self._width_range = Range(1e3, 4e6, 1, 1e6, 200)
        self._width_win = RangeWidget(self._width_range, self.set_width, 'Transition', "counter_slider", float)
        self.Tabs_grid_layout_0.addWidget(self._width_win, 2, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(2,3)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self._volume_range = Range(0.001, 10, 1, 1, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'volume', "counter_slider", float)
        self.Tabs_grid_layout_0.addWidget(self._volume_win, 4, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(4,5)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self._seek_range = Range(-20e6, 20e6, 1, 0, 200)
        self._seek_win = RangeWidget(self._seek_range, self.set_seek, 'Seek', "counter_slider", float)
        self.Tabs_grid_layout_0.addWidget(self._seek_win, 1, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(1,2)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self._freq_range = Range(24e6, 1.766e9, 1, 90.2e6, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency', "counter_slider", float)
        self.Tabs_grid_layout_0.addWidget(self._freq_win, 0, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(0,1)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self._cutoff_range = Range(1e3, 1e6, 1, 1e3, 200)
        self._cutoff_win = RangeWidget(self._cutoff_range, self.set_cutoff, 'Cutoff', "counter_slider", float)
        self.Tabs_grid_layout_0.addWidget(self._cutoff_win, 3, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(3,4)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq + seek, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=int(sample/10e3),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(sample),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq + seek, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(True)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Tabs_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 3, 0, 2, 2)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(3,5)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,2)]
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (firdes.low_pass(1,samp_rate,cutoff,width)), 0, sample)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=sample,
        	audio_decimation=10,
        )
        self.Input = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq + seek, #fc
        	samp_rate, #bw
        	"Input", #name
        	1 #number of inputs
        )
        self.Input.set_update_time(0.05)
        self.Input.set_y_axis(-140, 10)
        self.Input.set_y_label('Relative Gain', 'dB')
        self.Input.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.Input.enable_autoscale(False)
        self.Input.enable_grid(True)
        self.Input.set_fft_average(1.0)
        self.Input.enable_axis_labels(True)
        self.Input.enable_control_panel(True)

        if not True:
          self.Input.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.Input.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Input.set_line_label(i, "Data {0}".format(i))
            else:
                self.Input.set_line_label(i, labels[i])
            self.Input.set_line_width(i, widths[i])
            self.Input.set_line_color(i, colors[i])
            self.Input.set_line_alpha(i, alphas[i])

        self._Input_win = sip.wrapinstance(self.Input.pyqwidget(), Qt.QWidget)
        self.Tabs_grid_layout_0.addWidget(self._Input_win, 0, 0, 3, 2)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(0,3)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,2)]

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.Input, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rational_resampler_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "FM_Radio")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,self.cutoff,self.width)))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_seek(self):
        return self.seek

    def set_seek(self, seek):
        self.seek = seek
        self.rtlsdr_source_0.set_center_freq(self.freq + self.seek, 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq + self.seek, self.samp_rate)
        self.Input.set_frequency_range(self.freq + self.seek, self.samp_rate)

    def get_sample(self):
        return self.sample

    def set_sample(self, sample):
        self.sample = sample

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq + self.seek, self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,self.cutoff,self.width)))
        self.Input.set_frequency_range(self.freq + self.seek, self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.rtlsdr_source_0.set_center_freq(self.freq + self.seek, 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq + self.seek, self.samp_rate)
        self.Input.set_frequency_range(self.freq + self.seek, self.samp_rate)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,self.cutoff,self.width)))


def main(top_block_cls=FM_Radio, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
