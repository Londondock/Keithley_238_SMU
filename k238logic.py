# -*- coding: utf-8 -*- k238logic.py
"""
k238logic - This is the implementation logic for k238.py, the GUI generated by 
    running the PyQt4 UI code generator on the 'keithleyMainWindow.ui' file.
"""
from PyQt4 import QtGui
import sys
import math
import k238

class k238l(QtGui.QMainWindow,k238.Ui_keithleyOnlyWindow):
    # k238l is inherited from both QtGui.QDialog and hw.Ui_Dialog
    def __init__(self,parent=None):
        # Initialization of the class. Call the __init__ for the super classes
        super(k238l,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        
        """
        This is a variable to signal to the "read_sweepdata_linebyline()"
        method that the stop button has been pushed and we want to stop reading 
        data from the SMU.
        """
        self.keepreading = True
    
    def main(self):
        self.show()
    
    def connectActions(self):
        """Connect the GUI controls to the logic"""
        # Connect the radio buttons for function select.
        self.rdoDCSourceCurr.clicked.connect(self.on_function_select)        
        self.rdoDCSourceVolt.clicked.connect(self.on_function_select)                
        self.rdoSWSourceCurr.clicked.connect(self.on_function_select)        
        self.rdoSWSourceVolt.clicked.connect(self.on_function_select)        
        
        # Connect compliance group box to set compliance.        
        self.btnComp.clicked.connect(self.on_setcompliance_click)
        
        # Connect DC bias group box to set bias.
        self.btnDCBias.clicked.connect(self.on_setbias_click)
        
        # Connect sweep type and parameters to set sweep.
        self.btnSweep.clicked.connect(self.on_setsweep_click)
        
        # Connect the local/remote sense radio buttons to set sense.
        self.rdoLocalSense.clicked.connect(self.on_setlocalremote_click)
        self.rdoRemoteSense.clicked.connect(self.on_setlocalremote_click)
        
        # Connect operate, trigger, stop buttons.
        self.btnOperate.clicked.connect(self.on_operate_click)
        self.btnTrigger.clicked.connect(self.on_trigger_click)
        self.btnStop.clicked.connect(self.on_stop_click)
        
        # Connect file group box actions to open file for saving data.
        self.btnFileDialog.clicked.connect(self.on_file_click)
        
    def on_function_select(self):
        if self.rdoDCSourceCurr.isChecked()==True:
            keithley.setSource('dccurrent')
            keithley.setDataFormat(15,0,0)            
            keithley.setTriggerNow()
        elif self.rdoDCSourceVolt.isChecked()==True:
            keithley.setSource('dcvoltage')
            keithley.setDataFormat(15,0,0)            
            keithley.setTriggerNow()
        elif self.rdoSWSourceCurr.isChecked()==True:
            keithley.setSource('sweepcurrent')
            keithley.setDataFormat(15,0,1)            
        elif self.rdoSWSourceVolt.isChecked()==True:
            keithley.setSource('sweepvoltage')
            keithley.setDataFormat(15,0,1)            
        
    def on_setcompliance_click(self):
        keithley.setCompliance(self.ledtComp.text(),self.cboxCompRange.currentIndex())

    def on_setbias_click(self):
        keithley.setBias(self.ledtDCBias.text(),self.cboxDCBiasRange.currentIndex(),self.ledtDCDelay.text())

    def on_setsweep_click(self):
        if self.rdoLinear.isChecked()==True:
            keithley.setLinearSweep(self.ledtStart.text(),self.ledtStop.text(),self.ledtStep.text(),self.cboxSWBiasRange.currentIndex(),self.ledtDelay.text())
        elif self.rdoLog.isChecked()==True:
            keithley.setLogSweep(self.ledtStart.text(),self.ledtStop.text(),self.cboxSWLogPPD.currentIndex(),self.cboxSWBiasRange.currentIndex(),self.ledtDelay.text())
        elif self.rdoDC.isChecked()==True:
            keithley.setConstantSweep(self.ledtBias.text(),self.cboxSWBiasRange.currentIndex(),self.ledtDelay.text(),self.ledtCounts.text())
            
    def on_operate_click(self):
            keithley.setOperateOnOff(True)
            
    def on_setlocalremote_click(self):
        if self.rdoLocalSense.isChecked()==True:
            keithley.setRemoteSense(False)
        elif self.rdoRemoteSense.isChecked()==True:
            keithley.setRemoteSense(True)
    
    def on_trigger_click(self):
            self.keepreading = True
            if self.rdoSWSourceCurr.isChecked()==True:
                self.on_setsweep_click()
                time.sleep(5)
                keithley.setTriggerNow()
                self.read_sweepdata_linebyline()
            elif self.rdoSWSourceVolt.isChecked()==True:
                self.on_setsweep_click()
                time.sleep(5)
                keithley.setTriggerNow()
                self.read_sweepdata_linebyline()
            else:
                keithley.setTriggerNow()
            
    def on_stop_click(self):
            self.keepreading = False
            keithley.setOperateOnOff(False)
            
    def on_file_click(self):
            filename = QtGui.QFileDialog.getSaveFileName(self,'Save File','.')
            self.ledtFile.setText(filename)
    
    def read_sweepdata_linebyline(self):
            """ Read the sweep data from the SMU, parse it, save it to file."""
            # Set the data format to read out all items, ASCII, point by point.
            keithley.setDataFormat(15,0,1)
                        
            # Calculate how many points are going to be in the sweep length,
            # mainly because asking 'U8X' to SMU is too slow for large sweeps.
            swstart = float(self.ledtStart.text())
            swstop = float(self.ledtStop.text())
            swstep = float(self.ledtStep.text())
            swcounts = int(self.ledtCounts.text())
            swppd = int(self.cboxSWLogPPD.currentText())
                        
            if self.rdoLinear.isChecked()==True:
                numpoints=int(math.ceil(abs(swstart-swstop)/abs(swstep))+1)
            elif self.rdoLog.isChecked()==True:
                numpointsLog1=int(math.ceil(swppd*(math.log(swstart/swstop,10))+1))
                numpointsLog2=int(math.ceil(swppd*(math.log(swstop/swstart,10))+1))
                numpoints=max(numpointsLog1,numpointsLog2)
            elif self.rdoDC.isChecked()==True:
                numpoints=swcounts
            
            # Open file for saving data via appending new lines.
            if self.chboxSaveOnOff.isChecked() == True:
                fname = open(self.ledtFile.text(), 'w+')
                      
            # Read the data in line by line.
            count=0
            xdata=[]
            ydata=[]
            
            # Clear the plot from previous runs and set up the labels.
            self.mplwidget.axes.cla()
            self.mplwidget.axes.hold(True)
            self.mplwidget.axes.set_title('Live Data')
            self.mplwidget.axes.set_xlabel('Source')
            self.mplwidget.axes.set_ylabel('Measure')     
            
            # Read data in from sweep, line by line. Plot to mplwidget.
            while count < numpoints:
                if self.keepreading == True:
                    # Write to the GPIB converter box to read till EOI                  
                    ser.write('++read eoi \r')
                    s = ser.readline()
                    parsedData, tabbedData = keithley.parseDataLine(s)
                    if self.chboxSaveOnOff.isChecked() == True:
                        fname.write(tabbedData)
                        
                    # Append new data to graph arrays
                    xdata.append(parsedData[1])
                    ydata.append(parsedData[5]) 
                    
                    # Plot new graph arrays
                    self.mplwidget.axes.plot(xdata,ydata,'b.')
                    self.mplwidget.draw()
                    
                    # Update the main window and graph widget
                    app.processEvents()
                    count += 1
                    
                elif self.keepreading == False:
                    break
            
            # Save the data if selected to.            
            if self.chboxSaveOnOff.isChecked() == True:
                fname.close()        
           
if __name__=='__main__':
    import time
    import serial
    import smufunctions2
    ser = serial.Serial(port='COM3',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=3)  
    keithley = smufunctions2.smu(ser)
        
    app = QtGui.QApplication(sys.argv)
    k238l1 = k238l()
    k238l1.main()
    sys.exit(app.exec_())