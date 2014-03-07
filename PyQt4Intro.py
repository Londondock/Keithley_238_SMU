"""
PyQt4 sctrach example.
"""
import PyQt4
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

class HelloWindow(QtGui.QMainWindow):
    
    def __init__(self,win_parent=None,keithley):
        # Init the base class of the main window.
        QtGui.QMainWindow.__init__(self,win_parent)
        # Call the function that creates all the widgets.        
        self.create_widgets()
        
    def create_widgets(self):
        # Widgets such as buttons and labels created here.
        self.label=QtGui.QLabel('Say Hello:')        
        self.hello_edit=QtGui.QLineEdit()
        self.hello_button=QtGui.QPushButton('Push Me!')  
        
        # Create horizontal layout manager and add widgets to it.
        h_box=QtGui.QHBoxLayout()
        h_box.addWidget(self.label)
        h_box.addWidget(self.hello_edit)
        h_box.addWidget(self.hello_button)
               
        # Create the central widget, set layout based on horizontal layout
        # manager.
        central_widget=QtGui.QWidget()
        central_widget.setLayout(h_box)
        self.setCentralWidget(central_widget)
    
        # Connecting signals for event handling.
        QtCore.QObject.connect(self.hello_button,QtCore.SIGNAL('clicked()'),self.on_hello_clicked)
    
    # A message box pop-up to display the text in our Line Edit box.
    def on_hello_clicked(self):
        QtGui.QMessageBox.information(self
        , "Hello!"
        , "Hello %s" % self.hello_edit.displayText()
        , QtGui.QMessageBox.Ok)
    
if __name__ == "__main__":
    # Someone is launching this directly
    # Create the QApplication
    app=QtGui.QApplication(sys.argv)
    #The Main window
    main_window = HelloWindow()
    main_window.show()
    # Enter the main loop
    app.exec_()
    