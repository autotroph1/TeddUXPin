from rrb2 import *
import time

rr = RRB2()
try:
    while True:
        rr.forward(0.5,1)
        rr.reverse(0.5,1)
finally:
        rr.reverse(0.5,1)
        rr.stop()
