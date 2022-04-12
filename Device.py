import serial
import time


class pump():
    def __init__(self, port):
        self.port = port
        self.rate = 0
        self.state = 0  #The pump is on:1, off:0


    # 泵的流速，设定值和刷新

class knauer(pump):
    def __init__(self, port):
        super().__init__(port)

    def initiate(self):
        # 泵接口的初始化函数
        ser = serial.Serial(
            port=self.port,
            baudrate=9600,
            stopbits=1,
            parity='PARITY_NONE',
        )
        flag = ser.isOpen()
        if flag:
            return ser

    def turn_on(self):
        ser = self.initiate()
        ser.write(b'ON\r')
        ser.readall()
        self.state = 1

    def set_value(self, value):
        ser = self.initiate()
        ser.write(value.encode())
        self.rate = value
        ser.readall()

    def refresh(self):
        #刷新流速，运行状态两个参数。
        ser = self.initiate()
        ser.flush()
        ser.write(b'RATE?\r')
        time.sleep(0.1)
        ser.readall()
        pass

class oxford(pump):
    def __init__(self, port):
        super().__init__(port)

    def initiate(self):
        ser = serial.Serial(
            port=self.port,
            baudrate=9600,
            stopbits=1,
            parity='PARITY_NONE',
        )
        flag = ser.isOpen()
        if flag:
            return ser

    def turn_on(self):
        ser = self.initiate()
        ser.write(b'irun')
        ser.readall()
        self.state = 1
