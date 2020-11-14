#!/usr/bin/env python3
import os, sys, rospy

from roscam_application.msg import DHT22
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication


DHT22_value = [54, 48.2]

if __name__ == "__main__":

    app = QApplication(sys.argv)
    try:

        engine = QQmlApplicationEngine()
        ctx = engine.rootContext()

        ctx.setContextProperty("DHT22_value", DHT22_value)
        engine.load(os.path.join(os.path.dirname(__file__), "../Resources/main.qml"))

        timer = QTimer()
        timer.timeout.connect(lambda: None)
        timer.start(100)

        sys.exit(app.exec_())

    except KeyboardInterrupt:
        print("keyboard interupt")
        sys.exit(app.exec_())

    except Exception:
        print("exception")
        sys.exit(app.exec_())
