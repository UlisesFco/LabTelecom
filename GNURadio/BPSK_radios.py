#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BPSK_radios
# Generated: Fri Nov 23 09:37:56 2018
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
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio import vocoder
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time


class BPSK_radios(gr.top_block, Qt.QWidget):

    def __init__(self, parameter_0="addr=192.168.10.2", parameter_1="addr=192.168.10.3"):
        gr.top_block.__init__(self, "BPSK_radios")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BPSK_radios")
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

        self.settings = Qt.QSettings("GNU Radio", "BPSK_radios")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.parameter_0 = parameter_0
        self.parameter_1 = parameter_1

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 630e-3
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 45*nfilts)
        self.freq = freq = 2e9
        self.bw = bw = 5e6
        self.Tx_Gain = Tx_Gain = 3
        self.Rx_Gain = Rx_Gain = 30

        ##################################################
        # Blocks
        ##################################################
        self.vocoder_alaw_encode_sb_0 = vocoder.alaw_encode_sb()
        self.vocoder_alaw_decode_bs_0 = vocoder.alaw_decode_bs()
        self._variable_qtgui_range_0_range = Range(0, 1, 1, 630e-3, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, "variable_qtgui_range_0", "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.10.3", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate*10)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(Rx_Gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_bandwidth(bw/5, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate*10)
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(Tx_Gain, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_bandwidth(bw/5, 0)
        self.qtgui_sink_x_1 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate, #bw
        	"Recieved signal", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/5)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_1_win)
        
        self.qtgui_sink_x_1.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_KAISER, #wintype
        	freq, #fc
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
        
        
          
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("BER")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(8, (filter.firdes.root_raised_cosine(8,8,1.0,0.5,22)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fec_ber_bf_0 = fec.ber_bf(False, 100, -7.0)
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
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/ettus/Música/bensound-photoalbum.wav", True)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("testBPSK_sonido.wav", 1, 44100, 16)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_4 = blocks.multiply_const_vcc((2, ))
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vff((30.5176e-6, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((2, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((630e-3, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((32.768e3, ))
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-1, ))
        self.audio_sink_0 = audio.sink(44100, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.interp_fir_filter_xxx_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_sink_x_1, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.vocoder_alaw_encode_sb_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_short_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_4, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_4, 0), (self.digital_psk_demod_0, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_3, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.digital_psk_demod_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.digital_psk_demod_0, 0), (self.fec_ber_bf_0, 1))    
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.digital_simple_correlator_0, 0), (self.vocoder_alaw_decode_bs_0, 0))    
        self.connect((self.digital_simple_framer_0, 0), (self.digital_psk_mod_0, 0))    
        self.connect((self.digital_simple_framer_0, 0), (self.fec_ber_bf_0, 0))    
        self.connect((self.fec_ber_bf_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.digital_simple_correlator_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_const_vxx_4, 0))    
        self.connect((self.vocoder_alaw_decode_bs_0, 0), (self.blocks_short_to_float_0, 0))    
        self.connect((self.vocoder_alaw_encode_sb_0, 0), (self.digital_simple_framer_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BPSK_radios")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_parameter_0(self):
        return self.parameter_0

    def set_parameter_0(self, parameter_0):
        self.parameter_0 = parameter_0

    def get_parameter_1(self):
        return self.parameter_1

    def set_parameter_1(self, parameter_1):
        self.parameter_1 = parameter_1

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 45*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 45*self.nfilts))

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.qtgui_sink_x_1.set_frequency_range(self.freq, self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate*10)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate*10)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.qtgui_sink_x_1.set_frequency_range(self.freq, self.samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.uhd_usrp_sink_0.set_bandwidth(self.bw/5, 0)
        self.uhd_usrp_source_0.set_bandwidth(self.bw/5, 0)

    def get_Tx_Gain(self):
        return self.Tx_Gain

    def set_Tx_Gain(self, Tx_Gain):
        self.Tx_Gain = Tx_Gain
        self.uhd_usrp_sink_0.set_gain(self.Tx_Gain, 0)
        	

    def get_Rx_Gain(self):
        return self.Rx_Gain

    def set_Rx_Gain(self, Rx_Gain):
        self.Rx_Gain = Rx_Gain
        self.uhd_usrp_source_0.set_gain(self.Rx_Gain, 0)
        	


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "-a", "--parameter-0", dest="parameter_0", type="string", default="addr=192.168.10.2",
        help="Set addr1 [default=%default]")
    parser.add_option(
        "-b", "--parameter-1", dest="parameter_1", type="string", default="addr=192.168.10.3",
        help="Set addr2 [default=%default]")
    return parser


def main(top_block_cls=BPSK_radios, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(parameter_0=options.parameter_0, parameter_1=options.parameter_1)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
