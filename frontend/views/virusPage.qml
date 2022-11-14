import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.15
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    // Primary color: Material.Cyan
    id: viruspage
    // flags: Qt.FramelessWindowHint
    width: 800
    height: 480
    visible: true
    Material.theme: Material.Light
    title: "Raspirus - VIRUS"

    Image {
        width: 60
        height: 60
        x: 150
        y: 45
        source: "images/virus_page/warning-icon.svg"
    }

    Label {
        text: "VIRUS FOUND"
        font.pixelSize: 48
        color: Material.color(Material.Red)
        width: 325
        height: 60
        x: 245
        y: 45
    }

    Image {
        width: 60
        height: 60
        x: 590
        y: 45
        source: "images/virus_page/warning-icon.svg"
    }

    ScrollView {
        id: viruslist
        property int viruscount: 30
        width: 600
        height: 150
        x: 100
        y: 165
        spacing: 10
        ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
        ScrollBar.vertical.policy: ScrollBar.AlwaysOn

        ListView {
            model: viruslist.viruscount
            delegate: ItemDelegate {
                Rectangle {
                    width: viruslist.width
                    height: 30
                    border.width: 1
                    border.color: Material.color(Material.Red)

                    Text {
                        text: " Some test text"
                        font.pixelSize: 16
                        anchors.verticalCenter: parent.verticalCenter
                    }

                    ComboBox {
                        editable: false
                        width: 180
                        height: parent.height + 12
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        model: ["Test1", "Test2", "Test3"]
                        Material.background: Material.Red
                    }

                }
            }
        }
    }

    Button {
        id: submitbtn
        text: "CONFIRM"
        x: 290
        y: 370
        width: 170
        height: 60
        font.pixelSize: 24
        Material.background: Material.Red
    }

}