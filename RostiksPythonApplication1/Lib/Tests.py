import time
import ctypes

def click() :
    ctypes.windll.user32.SetCursorPos(777, 415)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up


def clicks() :
    N = 3600
    for i in range(N) :
        print 'Step number', i, ' Out of', N, time.asctime()
        click()
        time.sleep(10)  # Delay for 10 seconds)

clicks()