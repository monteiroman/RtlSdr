#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: AM_Demod
# Generated: Sun Jul 21 20:08:57 2019
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


class AM_Demod(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "AM_Demod")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("AM_Demod")
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

        self.settings = Qt.QSettings("GNU Radio", "AM_Demod")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.seek = seek = 0
        self.freq = freq = 415
        self.vol = vol = 1
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ((freq*1e6)+(seek*1e3))
        self.samp_rate = samp_rate = 2e6
        self.rf_gain = rf_gain = 60
        self.passband = passband = 10
        self.decimate = decimate = 10
        self.audio_low_cutoff = audio_low_cutoff = 250
        self.audio_high_cutoff = audio_high_cutoff = 1500

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
        self._vol_range = Range(0, 100, 1, 1, 100)
        self._vol_win = RangeWidget(self._vol_range, self.set_vol, 'volume', "counter_slider", float)
        self.top_layout.addWidget(self._vol_win)
        self._seek_range = Range(-100, 500, 0.5, 0, 100)
        self._seek_win = RangeWidget(self._seek_range, self.set_seek, 'Seek in kHz', "counter_slider", float)
        self.Tabs_grid_layout_0.addWidget(self._seek_win, 2, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(2,3)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self._rf_gain_range = Range(10, 70, 1, 60, 100)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, 'RF Gain dB', "counter_slider", int)
        self.Tabs_grid_layout_0.addWidget(self._rf_gain_win, 0, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(0,1)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self._passband_range = Range(3, 30, 1, 10, 100)
        self._passband_win = RangeWidget(self._passband_range, self.set_passband, 'Filter kHz', "counter_slider", int)
        self.Tabs_grid_layout_0.addWidget(self._passband_win, 4, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(4,5)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self._freq_range = Range(24, 1766, 0.5, 415, 100)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency in MHz', "counter_slider", float)
        self.Tabs_grid_layout_0.addWidget(self._freq_win, 1, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(1,2)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self._audio_low_cutoff_range = Range(20, 400, 1, 250, 200)
        self._audio_low_cutoff_win = RangeWidget(self._audio_low_cutoff_range, self.set_audio_low_cutoff, 'Audio low Cutoff Hz', "counter_slider", float)
        self.Tabs_grid_layout_1.addWidget(self._audio_low_cutoff_win, 2, 1, 1, 1)
        [self.Tabs_grid_layout_1.setRowStretch(r,1) for r in range(2,3)]
        [self.Tabs_grid_layout_1.setColumnStretch(c,1) for c in range(1,2)]
        self._audio_high_cutoff_range = Range(500, 20000, 1, 1500, 200)
        self._audio_high_cutoff_win = RangeWidget(self._audio_high_cutoff_range, self.set_audio_high_cutoff, 'Audio high Cutoff Hz', "counter_slider", float)
        self.Tabs_grid_layout_1.addWidget(self._audio_high_cutoff_win, 1, 1, 1, 1)
        [self.Tabs_grid_layout_1.setRowStretch(r,1) for r in range(1,2)]
        [self.Tabs_grid_layout_1.setColumnStretch(c,1) for c in range(1,2)]
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: eng_notation.num_to_str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel("Frequency"+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.Tabs_grid_layout_0.addWidget(self._variable_qtgui_label_0_tool_bar, 3, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(3,4)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(((freq*1e6)+(seek*1e3)), 0)
        self.rtlsdr_source_0.set_freq_corr(80, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(rf_gain, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(2e6, 0)

        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=200,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimate,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Tabs_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_win, 0, 1, 1, 1)
        [self.Tabs_grid_layout_1.setRowStretch(r,1) for r in range(0,1)]
        [self.Tabs_grid_layout_1.setColumnStretch(c,1) for c in range(1,2)]
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq + (seek*1e-3), #fc
        	50000, #bw
        	"Filter", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 5, 2, 1, 1)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(5,6)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(2,3)]
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decimate, passband*1000, 200, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff(((vol/100)*100, ))
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, 48e3, audio_low_cutoff, audio_high_cutoff, 10, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=samp_rate/decimate,
        	audio_decim=1,
        	audio_pass=20000,
        	audio_stop=21000,
        )
        self.Output_Frequency_graph = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	48e3, #bw
        	"Output Frequency Graph", #name
        	1 #number of inputs
        )
        self.Output_Frequency_graph.set_update_time(0.10)
        self.Output_Frequency_graph.set_y_axis(-100, -20)
        self.Output_Frequency_graph.set_y_label('Relative Gain', 'dB')
        self.Output_Frequency_graph.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.Output_Frequency_graph.enable_autoscale(False)
        self.Output_Frequency_graph.enable_grid(False)
        self.Output_Frequency_graph.set_fft_average(0.2)
        self.Output_Frequency_graph.enable_axis_labels(True)
        self.Output_Frequency_graph.enable_control_panel(True)

        if not True:
          self.Output_Frequency_graph.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.Output_Frequency_graph.set_plot_pos_half(not True)

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
                self.Output_Frequency_graph.set_line_label(i, "Data {0}".format(i))
            else:
                self.Output_Frequency_graph.set_line_label(i, labels[i])
            self.Output_Frequency_graph.set_line_width(i, widths[i])
            self.Output_Frequency_graph.set_line_color(i, colors[i])
            self.Output_Frequency_graph.set_line_alpha(i, alphas[i])

        self._Output_Frequency_graph_win = sip.wrapinstance(self.Output_Frequency_graph.pyqwidget(), Qt.QWidget)
        self.Tabs_grid_layout_1.addWidget(self._Output_Frequency_graph_win, 0, 0, 3, 1)
        [self.Tabs_grid_layout_1.setRowStretch(r,1) for r in range(0,3)]
        [self.Tabs_grid_layout_1.setColumnStretch(c,1) for c in range(0,1)]
        self.Input_Waterfall = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	((freq*1e6)+(seek*1e3)), #fc
        	samp_rate/decimate, #bw
        	"", #name
                1 #number of inputs
        )
        self.Input_Waterfall.set_update_time(0.10)
        self.Input_Waterfall.enable_grid(False)
        self.Input_Waterfall.enable_axis_labels(True)

        if not True:
          self.Input_Waterfall.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.Input_Waterfall.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Input_Waterfall.set_line_label(i, "Data {0}".format(i))
            else:
                self.Input_Waterfall.set_line_label(i, labels[i])
            self.Input_Waterfall.set_color_map(i, colors[i])
            self.Input_Waterfall.set_line_alpha(i, alphas[i])

        self.Input_Waterfall.set_intensity_range(-140, 10)

        self._Input_Waterfall_win = sip.wrapinstance(self.Input_Waterfall.pyqwidget(), Qt.QWidget)
        self.Tabs_grid_layout_0.addWidget(self._Input_Waterfall_win, 5, 0, 1, 2)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(5,6)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,2)]
        self.Input = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	((freq*1e6)+(seek*1e3)), #fc
        	samp_rate/decimate, #bw
        	"Input Frequency Graph", #name
        	1 #number of inputs
        )
        self.Input.set_update_time(0.05)
        self.Input.set_y_axis(-140, 10)
        self.Input.set_y_label('Relative Gain', 'dB')
        self.Input.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.Input.enable_autoscale(False)
        self.Input.enable_grid(True)
        self.Input.set_fft_average(0.2)
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
        self.Tabs_grid_layout_0.addWidget(self._Input_win, 0, 0, 4, 2)
        [self.Tabs_grid_layout_0.setRowStretch(r,1) for r in range(0,4)]
        [self.Tabs_grid_layout_0.setColumnStretch(c,1) for c in range(0,2)]

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_am_demod_cf_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.band_pass_filter_0, 0), (self.Output_Frequency_graph, 0))
        self.connect((self.band_pass_filter_0, 0), (self.audio_sink_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.Input, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.Input_Waterfall, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rational_resampler_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "AM_Demod")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_seek(self):
        return self.seek

    def set_seek(self, seek):
        self.seek = seek
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(((self.freq*1e6)+(self.seek*1e3))))
        self.rtlsdr_source_0.set_center_freq(((self.freq*1e6)+(self.seek*1e3)), 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq + (self.seek*1e-3), 50000)
        self.Input_Waterfall.set_frequency_range(((self.freq*1e6)+(self.seek*1e3)), self.samp_rate/self.decimate)
        self.Input.set_frequency_range(((self.freq*1e6)+(self.seek*1e3)), self.samp_rate/self.decimate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(((self.freq*1e6)+(self.seek*1e3))))
        self.rtlsdr_source_0.set_center_freq(((self.freq*1e6)+(self.seek*1e3)), 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq + (self.seek*1e-3), 50000)
        self.Input_Waterfall.set_frequency_range(((self.freq*1e6)+(self.seek*1e3)), self.samp_rate/self.decimate)
        self.Input.set_frequency_range(((self.freq*1e6)+(self.seek*1e3)), self.samp_rate/self.decimate)

    def get_vol(self):
        return self.vol

    def set_vol(self, vol):
        self.vol = vol
        self.blocks_multiply_const_vxx_0.set_k(((self.vol/100)*100, ))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decimate, self.passband*1000, 200, firdes.WIN_HAMMING, 6.76))
        self.Input_Waterfall.set_frequency_range(((self.freq*1e6)+(self.seek*1e3)), self.samp_rate/self.decimate)
        self.Input.set_frequency_range(((self.freq*1e6)+(self.seek*1e3)), self.samp_rate/self.decimate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.rtlsdr_source_0.set_gain(self.rf_gain, 0)

    def get_passband(self):
        return self.passband

    def set_passband(self, passband):
        self.passband = passband
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decimate, self.passband*1000, 200, firdes.WIN_HAMMING, 6.76))

    def get_decimate(self):
        return self.decimate

    def set_decimate(self, decimate):
        self.decimate = decimate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decimate, self.passband*1000, 200, firdes.WIN_HAMMING, 6.76))
        self.Input_Waterfall.set_frequency_range(((self.freq*1e6)+(self.seek*1e3)), self.samp_rate/self.decimate)
        self.Input.set_frequency_range(((self.freq*1e6)+(self.seek*1e3)), self.samp_rate/self.decimate)

    def get_audio_low_cutoff(self):
        return self.audio_low_cutoff

    def set_audio_low_cutoff(self, audio_low_cutoff):
        self.audio_low_cutoff = audio_low_cutoff
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, 48e3, self.audio_low_cutoff, self.audio_high_cutoff, 10, firdes.WIN_HAMMING, 6.76))

    def get_audio_high_cutoff(self):
        return self.audio_high_cutoff

    def set_audio_high_cutoff(self, audio_high_cutoff):
        self.audio_high_cutoff = audio_high_cutoff
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, 48e3, self.audio_low_cutoff, self.audio_high_cutoff, 10, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=AM_Demod, options=None):

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
