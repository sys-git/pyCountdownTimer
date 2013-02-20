pyCountdownTimer
================

A count-down timer that periodically checks a flag (to terminate the timer) using a supplied callable.

        from pyCountdownTimer import COuntdownTimer as timer
        
        #   Sleep/block for max: 'int_duration_seconds' checking boolean state of 'callable_func()' every 'resolution_seconds':
        try:
          boolean_slept = timer(int_duration_seconds, callable_func, resolution_seconds)
        except ValueError:
          print "Error or inconsistant parameters passed to CountdownTimer"
        except InterruptedSleep, e:
          print "Sleep was interrupted prematurely by callable_func()."
          print "Remaining sleep time: "+e.remaining
          print "Slept for time: "+e.duration
        else:
          # FYI - timer may not sleep if 'int_duration_seconds'==0
          print "Did we sleep? "+boolean_slept
        
