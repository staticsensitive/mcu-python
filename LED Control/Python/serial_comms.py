from PyQt5.QtCore import QObject, pyqtSignal,pyqtSlot 
import serial, serial.tools.list_ports
from threading import Thread, Event

class Communication(QObject):                                                   
	data_received = pyqtSignal(str)
                                                                             

	def __init__(self):
		super().__init__()
		self.arduino  = serial.Serial()
		self.arduino.timeout = 0.5		
		
		self.baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']
		self.ports = []

		self.thread = None
		self.alive = Event() #indica que esta activo

	def get_ports(self):
		self.ports = [port.device for port in serial.tools.list_ports.comports()]

	def connect_serial(self):
		try:	
			self.arduino.open()
		except:
			pass

		if (self.arduino.is_open): # iniciamos el hilo cuando puerto esta abierto
			self.start_thread()  


	def disconnect_serial(self):
		self.stop_thread()
		self.arduino.close()

	def get_data(self):
		while(self.alive.isSet() and self.arduino.is_open):
			
			data = self.arduino.readline().decode("utf-8").strip() 
			if(len(data)>1): 
				self.data_received.emit(data) 	


	def start_thread(self):
		self.thread = Thread(target= self.get_data) 
		self.thread.setDaemon(1) 
		self.alive.set()		 
		self.thread.start()	

	def stop_thread(self):
		if(self.thread is not None):
			self.alive.clear()
			self.thread.join()
			self.thread = None	
