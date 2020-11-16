#!/usr/bin/env python3
import rospy
from roscam_application.msg import DHT22
from threading import Thread

DEBUG = False


class threaded_node_class(Thread):
    def __init__(self, node_name="listener", anonymous=True, *args, **kwargs):

        super(threaded_node_class, self).__init__(*args, **kwargs)

        rospy.init_node(node_name, anonymous=anonymous, disable_signals=True)

        self.subcriber_dict = {}
        self.publisher_dict = {}

    def add_subscriber(self, callback, sub_name="chatter", msg_format=DHT22):

        try:
            sub = rospy.Subscriber(sub_name, msg_format, callback)
            self.subcriber_dict[sub_name] = sub
            if DEBUG:
                print("Subscriber succefully added")

        except Exception as ex:
            print("error during Subscriber adding")
            print(ex)

    def add_publisher(self, pub_name="Publisher", msg_format=DHT22, queue_size=10):

        try:
            pub = rospy.Publisher(
                name=pub_name, data_class=msg_format, queue_size=queue_size
            )
            self.publisher_dict[pub_name] = pub

        except Exception as ex:
            print("error during Publisher adding")
            print(ex)

    def stop(self):

        rospy.signal_shutdown("app stop")

    def run(self):

        try:
            rospy.spin()
        except Exception as ex:
            print(ex)

    def callback(self, data):

        print(data)
