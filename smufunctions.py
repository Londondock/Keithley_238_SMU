# -*- coding: utf-8 -*-
"""
smufunctions - A Python module for controlling the Keithley 238 SMU in
the Preston lab. This module instantiates a class for the SMU, and provides
various methods for setting and getting instrument configuration and data from
sweeps.
"""

class smu:
    """A class to see if I can write to the SMU after loading the serial port
    connection properly."""
    def __init__(self, serialconnection):
        self.conn = serialconnection
    
    def setSource(self, source):
        if source == 'dcvoltage':
            self.conn.write('F0,0X\r\n')
        elif source == 'sweepvoltage':
            self.conn.write('F0,1X\r\n')
        elif source == 'dccurrent':
            self.conn.write('F1,0X\r\n')
        elif source == 'sweepcurrent':
            self.conn.write('F1,1X\r\n')
        else:
            pass
    
    def setTrigger(self,value):
        if value == True:
            self.conn.write('R1X\r\n')
            print 'Triggering is on.'
        else:
            self.conn.write('R0X\r\n')
            print 'Triggering is off.'
        
    def setTriggerNow(self):        
        self.conn.write('H0X\r\n')
        
    def setOperateOnOff(self,value):
        if value == True:
            self.conn.write('N1X\r\n')
        else:
            self.conn.write('N0X\r\n')
        
    def setCompliance(self,level,compliancerange):
        outputComp = 'L'+str(level)+','+str(compliancerange)+'X\r\n'
        self.conn.write(outputComp)
        print 'Compliance level set.'
    
    def setBias(self,level,sourcerange,delay):
        if (
            level < -0.100 or level > 0.100 or
            sourcerange < 0 or sourcerange > 9 or
            delay < 0 or delay > 65000   
            ):
            print 'Out of parameter range.'
        else:
            outputBias = 'B'+str(level)+','+str(sourcerange)+','+str(delay)+'X\r\n'
            self.conn.write(outputBias)
            print 'Bias level set.'
    
    def setConstantSweep(self,level,sourcerange,delay,count):
        if (
            level < -0.100 or level > 0.100 or
            sourcerange < 0 or sourcerange > 9 or
            delay < 0 or delay > 65000 or
            count < 1 or count > 1000
            ):
            print 'Out of parameter range.'
        else:
            outputConstSweep = 'Q0'+','+str(level)+','+str(sourcerange)+','+str(delay)+','+str(count)+'X\r\n'
            self.conn.write(outputConstSweep)
            print 'Constant sweep is set.'
    
    def setLinearSweep(self,start,stop,step,sourcerange,delay):
        if (
            start < -0.100 or start > 0.100 or
            stop < -0.100 or stop > 0.100 or
            step < -0.100 or step > 0.100 or
            sourcerange < 0 or sourcerange > 9 or
            delay < 0 or delay > 65000
            ):
            print 'Out of parameter range.'
        else:
            outputLinearSweep = 'Q1'+','+str(start)+','+str(stop)+','+str(step)+','+str(sourcerange)+','+str(delay)+'X\r\n'
            self.conn.write(outputLinearSweep)
            print 'Linear sweep is set.'    
    
    def setDataFormat(self,items,dataformat,lines):
        if (
            items not in [0,1,2,4,8,15] or
            dataformat not in [0,1,2,3,4] or
            lines not in [0,1,2]
            ):
            print 'Out of parameter range.'
        else:
            outputDataFormat = 'G'+str(items)+','+str(dataformat)+','+str(lines)+'X\r\n'
            self.conn.write(outputDataFormat)
