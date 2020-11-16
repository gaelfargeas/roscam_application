import QtQuick 2.0
import QtQuick.Controls 1.6
import QtQuick.Window 2.10
import QtQuick.Layouts 1.3
import QtMultimedia 5.4

ApplicationWindow {
    id:main_windows
    visible: true
    width: 800
    height: 800
    title: qsTr("test QTROS app")

    color: "#121212"

    
    Rectangle{
        id: sensors_background_rectangle
        height: 100
        
        anchors.top: parent.top
        anchors.topMargin: 20
        anchors.right: parent.right
        anchors.rightMargin: 20        
        anchors.left: parent.left
        anchors.leftMargin: 20

        color: "#424242"
        radius: 20

        Rectangle{
            id: dht22_text_rectangle

            height: 22
            width: 120

            anchors.top: parent.top
            anchors.topMargin: 20
            anchors.left: parent.left
            anchors.leftMargin: 20

            radius: 5

            color: "#757575"


            Text {
                id: dht22_text
                text: "DHT22 Sensor"

                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter

                anchors.fill: dht22_text_rectangle
            
            }
        }

        Rectangle{
            id: dht22_values_rectangle

            width: dht22_text_rectangle.width
            
            anchors.top: dht22_text_rectangle.bottom
            
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 10
            anchors.left: parent.left
            anchors.leftMargin: 20

            radius: 5

            color: "#757575"


            Text {
                id: dht2_value_text
                text: "Humidity: " + roscam_main.DHT22_humidity_value + "%\nTemp: " + roscam_main.DHT22_temperature_value +"°C"

                verticalAlignment: Text.AlignTop
                horizontalAlignment: Text.AlignLeft

                anchors.fill: parent
                anchors.topMargin: 10
                anchors.leftMargin: 10
            
            }
        }

        
    }

   
    Rectangle
    {
        id: camera_background_rectangle

        anchors.top: sensors_background_rectangle.bottom
        anchors.topMargin: 20
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        anchors.right: parent.right
        anchors.rightMargin: 20        
        anchors.left: parent.left
        anchors.leftMargin: 20

        color: "#757575"
        radius: 20

        border.width: 5
        border.color: "#424242"

        MediaPlayer {
            id: mediaplayer1
            //source: "rtsp://admin:admin@192.168.1.q/1/stream1"
        }

        VideoOutput {
            anchors.fill: parent
            anchors.margins: 10
            source: mediaplayer1

        }
    }




}
