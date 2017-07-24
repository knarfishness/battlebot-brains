#!/usr/bin/env python

# handle imports
import time
from libraries import ps3

test = None

while test is None:
    try:
        print("Do the thing")
        p = ps3.ps3()
        raise(GenericError)
    except:
        print("Got the error")
        time.sleep(1);

