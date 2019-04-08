#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM Radio
# Generated: Mon Apr  8 18:08:27 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FM Radio")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.width = width = 1e6
        self.volume = volume = 1
        self.seek = seek = 0
        self.sample = sample = 500e3
        self.samp_rate = samp_rate = 2e6
        self.freq = freq = 90.2e6
        self.cutoff = cutoff = 100e3

        ##################################################
        # Blocks
        ##################################################
        self.notebook = self.notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Input")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Output")
        self.Add(self.notebook)
        _width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._width_text_box = forms.text_box(
        	parent=self.notebook.GetPage(0).GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	label='Transition',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._width_slider = forms.slider(
        	parent=self.notebook.GetPage(0).GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	minimum=1e3,
        	maximum=4e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.notebook.GetPage(0).Add(_width_sizer)
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label='Volume',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=1e-3,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_volume_sizer)
        _seek_sizer = wx.BoxSizer(wx.VERTICAL)
        self._seek_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_seek_sizer,
        	value=self.seek,
        	callback=self.set_seek,
        	label='Seek',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._seek_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_seek_sizer,
        	value=self.seek,
        	callback=self.set_seek,
        	minimum=-20e6,
        	maximum=20e6,
        	num_steps=400,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_seek_sizer)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=24e6,
        	maximum=1766e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        _cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cutoff_text_box = forms.text_box(
        	parent=self.notebook.GetPage(0).GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	label='Cutoff',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cutoff_slider = forms.slider(
        	parent=self.notebook.GetPage(0).GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	minimum=1e3,
        	maximum=1e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.notebook.GetPage(0).Add(_cutoff_sizer)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Output',
        	peak_hold=False,
        )
        self.notebook.GetPage(1).Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook.GetPage(0).GetWin(),
        	baseband_freq=freq + seek,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Input',
        	peak_hold=False,
        )
        self.notebook.GetPage(0).Add(self.wxgui_fftsink2_0.win)
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
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (firdes.low_pass(1,samp_rate,cutoff,width)), 0, sample)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=sample,
        	audio_decimation=10,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_fftsink2_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_fftsink2_0, 0))

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self._width_slider.set_value(self.width)
        self._width_text_box.set_value(self.width)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,self.cutoff,self.width)))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_seek(self):
        return self.seek

    def set_seek(self, seek):
        self.seek = seek
        self._seek_slider.set_value(self.seek)
        self._seek_text_box.set_value(self.seek)
        self.wxgui_fftsink2_0.set_baseband_freq(self.freq + self.seek)
        self.rtlsdr_source_0.set_center_freq(self.freq + self.seek, 0)

    def get_sample(self):
        return self.sample

    def set_sample(self, sample):
        self.sample = sample

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,self.cutoff,self.width)))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.wxgui_fftsink2_0.set_baseband_freq(self.freq + self.seek)
        self.rtlsdr_source_0.set_center_freq(self.freq + self.seek, 0)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self._cutoff_slider.set_value(self.cutoff)
        self._cutoff_text_box.set_value(self.cutoff)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1,self.samp_rate,self.cutoff,self.width)))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
