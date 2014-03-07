# -*- coding: utf-8 -*-
"""
smufunctions - A Python module for controlling the Keithley 238 SMU in
the Preston lab. This module instantiates a class for the SMU, and provides
various methods for setting and getting instrument configuration and data from
sweeps.
"""
import time

class smu:
    """A class to read and write to the SMU after loading the serial port
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
    
    def setTrigger(self,value):
        if value == True:
            self.conn.write('R1X\r\n')
        else:
            self.conn.write('R0X\r\n')
        
    def setCompliance(self,level,compliancerange):
        outputComp = 'L'+str(level)+','+str(compliancerange)+'X\r\n'
        self.conn.write(outputComp)
            
    def setBias(self,level,sourcerange,delay):
        outputBias = 'B'+str(level)+','+str(sourcerange)+','+str(delay)+'X\r\n'
        self.conn.write(outputBias)
            
    def setConstantSweep(self,level,sourcerange,delay,count):
        outputConstSweep = 'Q0'+','+str(level)+','+str(sourcerange)+','+str(delay)+','+str(count)+'X\r\n'
        self.conn.write(outputConstSweep)
            
    def setLinearSweep(self,start,stop,step,sourcerange,delay):
        outputLinearSweep = 'Q1'+','+str(start)+','+str(stop)+','+str(step)+','+str(sourcerange)+','+str(delay)+'X\r\n'
        self.conn.write(outputLinearSweep)        
    
    def setLogSweep(self,start,stop,points,sourcerange,delay):
        outputLogSweep = 'Q2'+','+str(start)+','+str(stop)+','+str(points)+','+str(sourcerange)+','+str(delay)+'X\r\n'
        self.conn.write(outputLogSweep)    
        
    def setDataFormat(self,items,dataformat,lines):
        outputDataFormat = 'G'+str(items)+','+str(dataformat)+','+str(lines)+'X\r\n'
        self.conn.write(outputDataFormat)
                  
    def setTriggerNow(self):        
        self.conn.write('H0X\r\n')
        
    def setOperateOnOff(self,value):
        if value == True:
            self.conn.write('N1X\r\n')
        else:
            self.conn.write('N0X\r\n')
        
    def getDataLine(self):
        self.conn.write('++read \r')
        time.sleep(0.1)
        dataline = self.conn.readline()
        return dataline

    def setRemoteSense(self,value):
        if value == True:
            self.conn.write('O1X\r\n')
        elif value == False:
            self.conn.write('O0X\r\n')
    
    def parseDataLine(self,dataline):
        sourcePrefix=dataline[0:5]
#        print sourcePrefix
        sourceValue=dataline[5:16]
#        print sourceValue
        delayPrefix=dataline[17]
#        print delayPrefix
        delayValue=dataline[18:29]
#        print delayValue
        measurePrefix=dataline[30:35]
#        print measurePrefix
        measureValue=dataline[35:47]
#        print measureValue
        timePrefix=dataline[48]
#        print timePrefix
        timeValue=dataline[49:61]
#        print timeValue
        bufferPrefix=dataline[62]
#        print bufferPrefix
        bufferValue=dataline[63:67]
#        print bufferValue
        parsedData = [sourcePrefix,sourceValue,delayPrefix,delayValue,measurePrefix,measureValue,timePrefix,timeValue,bufferPrefix,bufferValue]
        tabbedData = parsedData[0]+'\t'+parsedData[1]+'\t'+parsedData[2]+'\t'+parsedData[3]+'\t'+parsedData[4]+'\t'+parsedData[5]+'\t'+parsedData[6]+'\t'+parsedData[7]+'\t'+parsedData[8]+'\t'+parsedData[9]+'\n'
        return (parsedData,tabbedData)