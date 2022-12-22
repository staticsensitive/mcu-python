import sys
from ui_led import *
import serial

global serial
ser = serial.Serial('COM5',baudrate=9600,timeout=10)

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        
        self.ui.pbLED1On.clicked.connect(self.led1On)
        self.ui.pbLED2On.clicked.connect(self.led2On)


    def led1On (self):   
        if(self.ui.pbLED1On.text() == "LED 1 ON"):
            self.ui.pbLED1On.setText("LED 1 OFF")
            ser.write('<LED,1,1>'.encode())
            print("LED1 On")
        
        elif(self.ui.pbLED1On.text() == "LED 1 OFF"):
            self.ui.pbLED1On.setText("LED 1 ON")
            ser.write('<LED,1,0>'.encode())
            print("LED1 Off")        
      

    def led2On (self):
        if(self.ui.pbLED2On.text() == "LED 2 ON"):
            self.ui.pbLED2On.setText("LED 2 OFF")
            ser.write('<LED,2,1>'.encode())
            print("LED1 On")
        
        elif(self.ui.pbLED2On.text() == "LED 2 OFF"):
            self.ui.pbLED2On.setText("LED 2 ON")
            ser.write('<LED,2,0>'.encode())
            print("LED1 Off") 


        
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        mi_app = MyApp()
        mi_app.show()
        sys.exit(app.exec())	                                                                                                          