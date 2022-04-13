import serial
import time
import propar # pip install bronkhorst-propar


class pump():
    def __init__(self, port):
        self.port = port
        self.rate = 0
        self.state = 0  # The pump is on:1, off:0

    def initiate(self):
        # 设备端口初始化。检查一下设定。
        ser = serial.Serial(
            port=self.port,
            baudrate=9600,
            stopbits=1,
            parity='PARITY_NONE',
        )
        flag = ser.isOpen()
        if flag:
            return ser

    # 泵的流速，设定值和刷新


class knauer(pump):
    def __init__(self, port):
        super().__init__(port)

    def turn_on(self):
        ser = self.initiate()  # 最好每一个方法独自initiate一次，避免端口占用
        ser.write(b'ON\r')
        ser.readall()
        self.state = 1

    def turn_off(self):
        ser = self.initiate()
        ser.write(b'OFF\t')
        ser.readall()
        self.state = 0

    def set_value(self, value):
        ser = self.initiate()
        ser.write(value.encode())
        self.rate = value
        ser.readall()

    def refresh(self):
        # 刷新流速，运行状态两个参数。
        ser = self.initiate()
        ser.flush()
        ser.write(b'RATE?\r')
        time.sleep(0.1)
        ser.readall()
        pass


class oxford(pump):
    def __init__(self, port):
        super().__init__(port)

    def turn_on(self):
        ser = self.initiate()
        ser.write(b'run')
        ser.readall()
        self.state = 1

    def turn_off(self):
        ser = self.initiate()
        ser.write(b'stp')
        ser.readall()
        self.state = 0

    def set_value(self, value):
        ser = self.initiate()
        ser.write(b'irate' + value.encode())
        ser.readall()
        self.rate = value

    def refresh(self):
        ser = self.initiate()
        ser.write(b'crate')
        self.rate = ser.readall()


class jingjin(pump):
    def __init__(self, port):
        super().__init__(port)


class bronkhorst():
    # Bronkhorst有自己设备的控制包，文档请见：
    # https://bronkhorst-propar.readthedocs.io/en/latest/index.html
    def __init__(self):
        pass # 我还没想好怎么写