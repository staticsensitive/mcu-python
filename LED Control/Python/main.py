import sys
from ui_serial import *
from serial_comms import Communication
from PyQt5.QtCore import QTimer 
from PyQt5.QtGui import QPixmap

class MiApp(QtWidgets.QMainWindow):
    def __init__(self,*args, **kwargs):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        
        self.serial = Communication()
        self.get_port()
        self.ui.lcdNumber.display("000")
        
        self.serial.data_received.connect(self.data_rx)
        self.ui.cboBaud.addItems(self.serial.baudrates)
        self.ui.cboBaud.setCurrentText("9600")
        
        self.ui.pushButton.clicked.connect(self.connect)
        self.ui.pushButton_2.clicked.connect(self.disconnect)
        self.ui.btnLed1On.clicked.connect(self.led1On)
        self.ui.btnLED2On.clicked.connect(self.led2On)
        
        pixmap = QPixmap('switch-off.png')
        self.ui.lblSw.setPixmap(pixmap)
       
      
        
    
    def data_rx(self,data):
        d1 = data.split(",")
         
        print(d1[1])
        
        swVal = int(d1[1])
        if(swVal == 1):
            pixmap = QPixmap('switch-off.png')
            self.ui.lblSw.setPixmap(pixmap)
        else:
            pixmap = QPixmap('switch-on.png')
            self.ui.lblSw.setPixmap(pixmap)    
        
        
        
    def led1On (self):   
        if(self.ui.btnLed1On.text() == "LED1 On"):
            self.ui.btnLed1On.setText("LED1 Off")
            self.serial.arduino.write('<LED,1,1>'.encode())
            print("LED1 On")
        
        elif(self.ui.btnLed1On.text() == "LED1 Off"):
            self.ui.btnLed1On.setText("LED1 On")
            self.serial.arduino.write('<LED,1,0>'.encode())
            print("LED1 Off")        
      

    def led2On (self):
        if(self.ui.btnLED2On.text() == "LED2 On"):
            self.ui.btnLED2On.setText("LED2 Off")
            self.serial.arduino.write('<LED,2,1>'.encode())
            print("LED2 On")
        
        elif(self.ui.btnLED2On.text() == "LED2 Off"):
            self.ui.btnLED2On.setText("LED2 On")
            self.serial.arduino.write('<LED,2,0>'.encode())
            print("LED1 Off") 

    def get_port(self):
        self.serial.get_ports()
        self.ui.cboPort.clear
        self.ui.cboPort.addItems(self.serial.ports)

    def connect(self):
        port = self.ui.cboPort.currentText()
        baud = self.ui.cboBaud.currentText()
        self.serial.arduino.port = port
        self.serial.arduino.baudrate = baud
        self.serial.connect_serial()
        #QTimer.singleShot(20,self.data_rx(data_received))
    
    def disconnect(self):
        self.serial.disconnect()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        mi_app = MiApp()
        mi_app.show()
        sys.exit(app.exec_())	