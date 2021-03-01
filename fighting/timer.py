from util.colors import RESET, RED_BOLD
import signal
import time
import sys
from multiprocessing import Process

sys.path.append('../')
from util.variables import timerMode

#Battle
class TimeOut(Exception):  #Use this instead of a general Exception- Avoid accidentally catching other errors
  pass

def signalHandler(sign, frame):
  raise TimeOut("Sorry, time is out.")

#Variables
processArray = []
pause_timers = False

#Clears/stops all existing timers
def clearTimers():
  global processArray
  signal.alarm(0)
  for i in range(len(processArray)):
    processArray[i].kill()
    processArray.pop(i)

def pauseTimers(is_set, pause=False):
  global pause_timers
  if not is_set:
    pause_timers = pause
  return pause_timers

#Stops old timers and creates a new one
def resetTimer(timeEnd):
  global processArray
  global timerMode

  #Clear existing timers
  clearTimers()

  if (timerMode == "on"):
    #Starting a new signal
    signal.signal(signal.SIGALRM, signalHandler)
    signal.alarm(timeEnd)

    #Starting another process too
    p2 = Process(target=timer, args=(timeEnd, ))
    p2.start()
    processArray.append(p2)

timer_res = 1
def timer(t):
  org = t
  while (t > 0):
    if pause_timers:
      continue
    comp_t = int(timer_res * (t // timer_res))
    if (comp_t == int(org / 2)):
      print(RED_BOLD + "\nHalf Time Left!" + RESET)
    if (comp_t == int(org / 4)):
      print(RED_BOLD + "\nAlmost up!" + RESET)

    time.sleep(timer_res)
    t -= timer_res