pyCountdownTimer
================

A count-down timer that periodically checks a flag (to terminate the timer) using a supplied callable.

There are some simple unit-tests that take 20 seconds to execute and leave no remaining threads or processes.

        from  pyCountdownTimer import Timer, InteruptedSleep
        
        #   Sleep/block for max: 'int_duration_seconds' checking boolean state of 'callable_func()' every 'resolution_seconds':
        try:
          boolean_slept = Timer(int_duration_seconds, callable_func, resolution_seconds)
        except ValueError:
          print "Error or inconsistant parameters passed to CountdownTimer"
        except InteruptedSleep, e:
          print "Sleep was interrupted prematurely by callable_func() at: %s"%e.when
          print "Remaining sleep time: %s"%e.remaining
          print "Slept for time: %s"%e.duration
          print "Expected to sleep for time: %s"%e.expected
        else:
          # FYI - timer may not sleep if 'int_duration_seconds'==0
          print "Did we sleep? "+boolean_slept
        
In case you're feeling generous:
LTC: LT636SrauWAz9XDz2EKxAXQ5jKqehyhR69
BTC: 13vS6cvzZXf1Yxrar2SYSPQrFLSEwLePV4
