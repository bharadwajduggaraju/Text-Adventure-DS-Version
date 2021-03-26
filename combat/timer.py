from util.colors import RESET, RED_BOLD
import signal
import time
from multiprocessing import Process

class Timer:
  timerMode = "on"
  pause_timers = False
  def settings(name, value=None):
    """timerMode, pause_timers"""
    is_set = value != None
    if name == "timerMode":
      if is_set:
        if type(value) == type(Timer.timerMode):
          Timer.timerMode = value
        else:
          raise TypeError
      return Timer.timerMode
    elif name == "pause_timers":
      if is_set:
        if type(value) == type(Timer.pause_timers):
          Timer.pause_timers = value
        else:
          raise TypeError
      return Timer.pause_timers
    else:
      raise ValueError

class TimeOut(Exception):  #Use this instead of a general Exception- Avoid accidentally catching other errors
  pass

def signalHandler(sign, frame):
  raise TimeOut("Sorry, time is out.")

processArray = [] #No one else needs to access this- For this file only.

#Clears/stops all existing timers
def clearTimers():
  global processArray
  signal.alarm(0)
  for i in range(len(processArray)):
    processArray[i].kill()
    processArray.pop(i)

def pauseTimers(is_set, pause=True):
  if is_set:
    pause = None
  Timer.settings("pause_timers", pause)

#Stops old timers and creates a new one
def resetTimer(timeEnd):
  global processArray

  #Clear existing timers
  clearTimers()

  if (Timer.timerMode == "on"):
    #Starting a new signal
    signal.signal(signal.SIGALRM, signalHandler)
    signal.alarm(timeEnd)

    #Starting another process too
    p2 = Process(target=timer, args=(timeEnd, ))
    p2.start()
    processArray.append(p2)

def timer(t, timer_res=1):
  org = t
  while (t > 0):
    if Timer.pause_timers:
      continue
    comp_t = int(timer_res * (t // timer_res))
    if (comp_t == int(org / 2)):
      print(RED_BOLD + "\nHalf Time Left!" + RESET)
    if (comp_t == int(org / 4)):
      print(RED_BOLD + "\nAlmost up!" + RESET)

    time.sleep(timer_res)
    t -= timer_res