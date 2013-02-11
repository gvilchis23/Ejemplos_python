'''
Created on 11/02/2013

@author: infest48
'''
# Example of a simple event-driven program

# CodeSkulptor GUI module
import threading

# Event handler
def tick():
    print "tick!"
    lanza()

# Register handler
def lanza():
    timer = threading.Timer(1,tick)
    # Start timer
    timer.start()
    
lanza()



