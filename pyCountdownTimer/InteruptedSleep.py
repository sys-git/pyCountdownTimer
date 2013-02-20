'''
Created on 20 Feb 2013

@author: francis
'''

import time

class InteruptedSleep(Exception):
    def __init__(self, expected, start, end, resolutionSeconds):
        self.when = time.time()
        self.start = start
        self.end = end
        self.resolutionSeconds = resolutionSeconds
        self.remaining = self.end-self.when
        self.duration = self.when-self.start
        self.expected = expected