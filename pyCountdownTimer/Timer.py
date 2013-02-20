'''
Created on 20 Feb 2013

@author: Francis
'''

from pyCountdownTimer import InteruptedSleep
import time

class Timer(object):
    r"""
    @summary: A timer to count-down and periodically check a flag using a supplied callable.
    @param: callable_ A callable which takes no params, returns False=Stop sleep, True=continue sleep.
    @raise ValueException - error or inconsistent parameters.
    @raise InteruptedSleep: callable triggered the sleep to be interupted.
    """
    @staticmethod
    def __new__(cls, time_s, callable_=lambda: False, resolution_s=1):
        #    Check the time_s
        if time_s is None:
            raise ValueError("time_s parameter is None!")
        if isinstance(time_s, int):
            if time_s<0:
                raise ValueError("time_s parameter is negative: <%(T)s>."%{"T":time_s})
            elif time_s==0:
                return False
        else:
            raise ValueError("time_s parameter is invalid: <%(T)s>."%{"T":time_s})
        #    Check the resolution_s:
        if resolution_s is None:
            raise ValueError("resolution_s parameter is None!")
        if isinstance(resolution_s, int):
            if resolution_s<=0:
                raise ValueError("resolution_s parameter is invalid: <%(R)s>."%{"R":resolution_s})
            if resolution_s>time_s:
                raise ValueError("resolution_s parameter %(R)s is greater than the parameter time_s: %(T)s."%{"T":time_s, "R":resolution_s})
            Timer._sleep(time_s, resolution_s, callable_=callable_)
            return True
        else:
            raise ValueError("time_s parameter is invalid: <%(T)s>."%{"T":time_s})
    @staticmethod
    def _sleep(time_s, resolution_s, callable_=None):
        timeStart = time.time()
        endTime = timeStart + time_s
        while time.time()<endTime:
            if callable_() is True:
                print "Countdown timer expired due to supplied callable result!"
                raise InteruptedSleep(time_s, timeStart, endTime, resolution_s)
            timeNow = time.time()
            timeRemaining = endTime - timeNow
            period = max(min(timeRemaining, resolution_s), 0)
            if period>0:
                time.sleep(period)
