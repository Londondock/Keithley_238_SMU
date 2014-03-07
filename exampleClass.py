# -*- coding: utf-8 -*-
"""
Just a test to see if I can make a class work properly.
"""

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        """
        Prints 'hello world' to stout
        """        
        return 'hello world'
        
    def __init__(self):
        self.data = []

class Complex:
    """A class for giving real and imaginary parts to an object"""
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class smu:
    """A class to see if I can write to the SMU after loading the serial port
    connection properly."""
    def __init__(self, serialconnection):
        self.conn = serialconnection
    
    def setSource(self, Source):
        if Source == 'dcvoltage':
            self.conn.write('F0,1X\r\n')
        elif Source == 'dccurrent':
            self.conn.write('F1,0X\r\n')
        else:
            pass
