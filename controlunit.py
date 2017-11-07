from serial import Serial
from Project import ControlUnitProt as CUP
import time


class ControlUnit:
    def __init__(self, hw_device):
        self.connected = False
        self.serial_connection = Serial(hw_device)

    def request_connection(self):
        time.sleep(2)
        self.serial_connection.write(bytes.fromhex("3F"))
        self.serial_connection.write(bytes.fromhex("00 00"))
        response = self.serial_connection.read()
        self.serial_connection.read(2)
        if response == bytes.fromhex(CUP.ACK_CONNECTION):
            self.connected = True
            return True
        else:
            self.connected = False
            return False

    def request_device_name(self):
        if self.connected and self.serial_connection.is_open:
            self.serial_connection.write(bytes.fromhex(CUP.REQ_DEVICE_NAME))
            self.serial_connection.write(bytes.fromhex("00 00"))

            response = self.serial_connection.readline()
            if response[0] == bytes.fromhex(CUP.RET_DEVICE_NAME)[0]:
                return response[1:-1].__repr__()[2:-1]  # remove response byte and newline character

    def update_device_name(self, new_name):
        """
        Does nothing, is a method stub
        :return:
        """
        if self.connected:
            length = "00 09"
            print("updating name")
            print("lenght:", length)
            self.serial_connection.write(bytes.fromhex(CUP.UPD_DEVICE_NAME))
            self.serial_connection.write(bytes.fromhex(length))
            print(self.serial_connection.write(bytes(new_name, encoding="ascii")))
            print("Done updating")

    def request_sensor_type(self):
        if self.connected and self.serial_connection.is_open:
            self.serial_connection.write(bytes.fromhex(CUP.REQ_SENSOR_TYPE))
            self.serial_connection.write(bytes.fromhex("0000"))

            response = self.serial_connection.read(3)
            return int(response[1:].hex(), 16)

    def request_status(self):
        if self.connected:
            self.serial_connection.write(bytes.fromhex(CUP.REQ_STATUS + "0000"))

            response = self.serial_connection.read()
            distance = self.serial_connection.read(2)
            sensor = self.serial_connection.read(2)
            if response.hex() == CUP.RET_STATUS:
                return int(distance.hex(), 16), int(sensor.hex(), 16)
            else:
                return None

    def request_setting(self, setting):
        if self.connected:
            self.serial_connection.write(bytes.fromhex(CUP.REQ_SETTING))
            self.serial_connection.write(bytes.fromhex(setting))

            response = self.serial_connection.read()
            value = self.serial_connection.read(2).hex()
            if response.hex() == CUP.RET_SETTING:
                return int(value, 16)

    def update_setting(self, setting, new_value):
        pass

    def request_disconnect(self):
        if self.connected:
            self.serial_connection.write(bytes.fromhex("00 00 00"))
            response = self.serial_connection.read()
            self.serial_connection.read(2)

            if response.hex() == CUP.ACK_DISCONNECT:
                self.connected = False
                self.serial_connection.close()

    def __repr__(self):
        name = self.request_device_name()
        sensor_type = self.request_sensor_type()

        return "Device name: {}\nConnected: {}\nSensor type: {}".format(name, sensor_type, self.connected)
