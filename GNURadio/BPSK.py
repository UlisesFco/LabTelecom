#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BPSK simulation
# Generated: Mon Jan 21 12:10:57 2019
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

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import vocoder
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import epy_block_0
import sip
import sys


class BPSK(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BPSK simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BPSK simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "BPSK")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 630e-3
        self.samp_rate = samp_rate = 256e3

        ##################################################
        # Blocks
        ##################################################
        self.vocoder_alaw_encode_sb_0 = vocoder.alaw_encode_sb()
        self.vocoder_alaw_decode_bs_0 = vocoder.alaw_decode_bs()
        self._variable_qtgui_range_0_range = Range(0, 1, 1, 630e-3, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, "variable_qtgui_range_0", "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self.qtgui_sink_x_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Channel output", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_1_win)
        
        self.qtgui_sink_x_1.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_KAISER, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Modulator output", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(True)
        
        
          
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(8, (filter.firdes.root_raised_cosine(8,8,1.0,0.5,21)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.epy_block_0 = epy_block_0.blk(example_param=1.0)
        self.digital_simple_framer_0 = digital.simple_framer(20)
        self.digital_simple_correlator_0 = digital.simple_correlator(20)
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=2,
          mod_code="gray",
          differential=False,
          samples_per_symbol=4,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_psk_demod_0 = digital.psk.psk_demod(
          constellation_points=2,
          differential=False,
          samples_per_symbol=4,
          excess_bw=0.35,
          phase_bw=6.28/100.0,
          timing_bw=6.28/100.0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0,
        	frequency_offset=0,
        	epsilon=1,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/ettus/Música/bensound-photoalbum.wav", True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vff((30.5176e-6, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((2, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((630e-3, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((32.768e3, ))
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "BPSK_Channel.txt", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1, ))
        self.audio_sink_0 = audio.sink(44100, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.interp_fir_filter_xxx_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.vocoder_alaw_encode_sb_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_short_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_3, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.digital_psk_demod_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_sink_x_1, 0))    
        self.connect((self.digital_psk_demod_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.digital_simple_correlator_0, 0), (self.vocoder_alaw_decode_bs_0, 0))    
        self.connect((self.digital_simple_framer_0, 0), (self.epy_block_0, 0))    
        self.connect((self.epy_block_0, 0), (self.digital_psk_mod_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.digital_simple_correlator_0, 0))    
        self.connect((self.vocoder_alaw_decode_bs_0, 0), (self.blocks_short_to_float_0, 0))    
        self.connect((self.vocoder_alaw_encode_sb_0, 0), (self.digital_simple_framer_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BPSK")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_1.set_frequency_range(0, self.samp_rate)


def main(top_block_cls=BPSK, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
