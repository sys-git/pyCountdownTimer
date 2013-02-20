'''
Created on 20 Feb 2013

@author: francis
'''

from  pyCountdownTimer import Timer, InteruptedSleep
import time
import unittest

class TestCountdownTimer(unittest.TestCase):
    def setUp(self):
        self._count = 0
        self._interuptionTimeout = 5
        self._timeStart = None
    def _flagChecker(self):
        if time.time()>=(self._timeStart+self._interuptionTimeout):
            return True
        return False
    def _timeEquals(self, t1, t2, resolution=1):
        duration = abs(t1-t2)
        assert (duration<=resolution), "Duration %(D)s is greater than allowed uncertainty: %(U)s"%{"D":duration, "U":resolution}
    def testTimeIsNone(self):
        try:
            Timer(None)
        except:
            assert True
        else:
            assert False, "Exception should have been raised!"
    def testTimeOfWrongType(self):
        try:
            Timer("123")
        except:
            assert True
        else:
            assert False, "Exception should have been raised!"
    def testTimeIsZero(self):
        try:
            slept = Timer(0)
        except:
            assert False, "Exception should have been raised!"
        else:
            assert slept is False, "Should have not slept!"
    def testTimeIsNegative(self):
        try:
            Timer(-1)
        except:
            assert True
        else:
            assert False, "Exception should have been raised!"
    def testResolutionIsNone(self):
        try:
            Timer(1, resolution_s=None)
        except:
            assert True
        else:
            assert False, "Exception should have been raised!"
    def testResolutionOfWrongType(self):
        try:
            Timer(10, resolution_s="123")
        except:
            assert True
        else:
            assert False, "Exception should have been raised!"
    def testResolutionIsZero(self):
        try:
            Timer(10, resolution_s=0)
        except:
            assert True
        else:
            assert False, "Exception should have been raised!"
    def testResolutionIsNegative(self):
        try:
            Timer(10, resolution_s=-1)
        except:
            assert True
        else:
            assert False, "Exception should have been raised!"
    def testResolutionIsTooBig(self):
        try:
            Timer(10, resolution_s=11)
        except:
            assert True
        else:
            assert False, "Exception should have been raised!"
    def testMidwayInteruption(self):
        self._timeStart = time.time()
        self._interuptionTimeout = 5
        duration = 10
        resolution = 1
        try:
            Timer(duration, callable_=self._flagChecker, resolution_s=resolution)
        except InteruptedSleep, e:
            print "Sleep was interrupted prematurely by callable_func() at: %s"%e.when
            print "Remaining sleep time: %s"%e.remaining
            print "Slept for time: %s"%e.duration
            print "Expected to sleep for time: %s"%e.expected
            assert int(e.start)==int(self._timeStart)
            timeEnd = time.time()
            assert int(timeEnd-self._timeStart)>(self._interuptionTimeout-1)
            assert e.resolutionSeconds==resolution
    def testNormalExpiry(self):
        self._timeStart = time.time()
        duration = 5
        resolution = 1
        slept = Timer(duration, resolution_s=resolution)
        assert slept is True, "Should have slept!"
        timeEnd = time.time()
        self._timeEquals(timeEnd-self._timeStart, duration)
    def testNormalExpiry2SecondResolution(self):
        self._timeStart = time.time()
        duration = 5
        resolution = 2
        slept = Timer(duration, resolution_s=resolution)
        assert slept is True, "Should have slept!"
        timeEnd = time.time()
        self._timeEquals(timeEnd-self._timeStart, duration)
    def testNormalExpiryMaxResolution(self):
        self._timeStart = time.time()
        duration = 5
        resolution = 5
        slept = Timer(duration, resolution_s=resolution)
        assert slept is True, "Should have slept!"
        timeEnd = time.time()
        self._timeEquals(timeEnd-self._timeStart, duration)

if __name__=="__main__":
    unittest.main()
