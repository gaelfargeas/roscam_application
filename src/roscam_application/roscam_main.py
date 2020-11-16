#!/usr/bin/env python3
import os, sys, rospy, math

from roscam_application.msg import DHT22
from PyQt5 import QtCore
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication

# from threaded_node import threaded_node_class
# import threaded_node

from . import threaded_node

DEBUG = False


class roscam_application(QtCore.QObject):
    DHT22_value_Changed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

        self.m_DHT22_temperature_value = 0.0
        self.m_DHT22_humidity_value = 0

        self.application_node = threaded_node.threaded_node_class(
            node_name="application_node", anonymous=True
        )
        self.application_node.add_subscriber(
            sub_name="DHT22_sensor", msg_format=DHT22, callback=self.DHT22_callback
        )
        self.application_node.start()

        self.start_GUI()

    def start_GUI(self):

        app = QApplication(sys.argv)
        try:

            engine = QQmlApplicationEngine()
            ctx = engine.rootContext()

            ctx.setContextProperty("roscam_main", self)
            engine.load(
                os.path.join(os.path.dirname(__file__), "../../Resources/main.qml")
            )

            timer = QtCore.QTimer()
            timer.timeout.connect(lambda: None)
            timer.start(100)

            sys.exit(self.Close_fct(app=app, sub=self.application_node))

        except KeyboardInterrupt:
            print("keyboard interupt")
            sys.exit(self.Close_fct(app=app, sub=self.application_node))

        except Exception:
            print("exception")
            sys.exit(self.Close_fct(app=app, sub=self.application_node))

    def Close_fct(self, app, sub):

        # stop app
        ret = app.exec_()
        # stop rospy
        sub.stop()
        # stop thread
        sub.join()

        return ret

    def DHT22_callback(self, data):

        if DEBUG:
            print("Received data :\n", data)

        self.m_DHT22_humidity_value = data.humidity
        self.m_DHT22_temperature_value = round(data.temperature, 2)

        self.DHT22_value_Changed.emit()

    @QtCore.pyqtProperty(int, notify=DHT22_value_Changed)
    def DHT22_humidity_value(self):
        return self.m_DHT22_humidity_value

    @QtCore.pyqtProperty(float, notify=DHT22_value_Changed)
    def DHT22_temperature_value(self):
        return self.m_DHT22_temperature_value
