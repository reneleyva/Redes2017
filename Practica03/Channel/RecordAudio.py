#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pyaudio
from threading import Thread

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

class RecordAudio(Thread):

    def __init__(self):
        self.thread = Thread.__init__(self)

    def run(self):
        self.p = pyaudio.PyAudio()
        CHUNK = 1024
        WIDTH = 2
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        self.stream = self.p.open(format=self.p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

        print("* recording")
        while True:
            data = self.stream.read(CHUNK)
            self.stream.write(data, CHUNK)

        print("* done")

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
