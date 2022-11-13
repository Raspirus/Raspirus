import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    // Primary color: Material.Cyan
    id: settingspage
    // flags: Qt.FramelessWindowHint
    width: 800
    height: 480
    visible: true
    Material.theme: Material.Light
    title: "Raspirus - SETTINGS"

    RoundButton {
        id: homebutton
        text: "HOME"
        font.pixelSize: 16
        width: 100
        height: 40
        x: 25
        y: 25
        radius: 20
        icon.source: "images/settings_page/left-arrow-icon.svg"
        Material.background: Material.BlueGrey
    }

    Label {
        text: "SETTINGS"
        font.pixelSize: 64
        color: Material.color(Material.DeepOrange)
        width: 510
        height: 120
        x: 250
        y: 50
    }

    Label {
        text: "Update Hash Signatues"
        font.pixelSize: 20
        width: 460
        height: 25
        x: 30
        y: 170
    }

    Button {
        id: updatesignaturesbtn
        text: "Last Update: 18.10.2022"
        width: 290
        height: 50
        x: 490
        y: 165
        icon.source: "images/settings_page/refresh-icon.svg"
        Material.background: Material.Cyan

        contentItem: Item {
            Image {
                source: updatesignaturesbtn.icon.source
                width: updatesignaturesbtn.icon.width
                height: updatesignaturesbtn.icon.height
                anchors.verticalCenter: parent.verticalCenter
            }
            Text {
                text: updatesignaturesbtn.text
                font: updatesignaturesbtn.font
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

    }

    Label {
        text: "Open LOG window"
        font.pixelSize: 20
        width: 460
        height: 25
        x: 30
        y: 245
    }

    Button {
        id: openlogbtn
        text: "Generated on: 18.10.2022"
        width: 290
        height: 50
        x: 490
        y: 240
        icon.source: "images/settings_page/book-icon.svg"
        Material.background: Material.Cyan

        contentItem: Item {
            Image {
                source: openlogbtn.icon.source
                width: openlogbtn.icon.width
                height: openlogbtn.icon.height
                anchors.verticalCenter: parent.verticalCenter
            }
            Text {
                text: openlogbtn.text
                font: openlogbtn.font
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }

    }

    Label {
        text: "Activate SSH"
        font.pixelSize: 20
        width: 460
        height: 25
        x: 30
        y: 325
    }

    Button {
        id: activatesshbtn
        text: "Status: Active"
        width: 290
        height: 50
        x: 490
        y: 320
        icon.source: "images/settings_page/check-icon.svg"
        Material.background: Material.Green

        contentItem: Item {
            Image {
                source: activatesshbtn.icon.source
                width: activatesshbtn.icon.width
                height: activatesshbtn.icon.height
                anchors.verticalCenter: parent.verticalCenter
            }
            Text {
                text: activatesshbtn.text
                font: activatesshbtn.font
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }
    }

    Label {
        text: "Activate FTP"
        font.pixelSize: 20
        width: 460
        height: 25
        x: 30
        y: 400
    }

    Button {
        id: activateftpbtn
        text: "Status: Deactivated"
        width: 290
        height: 50
        x: 490
        y: 395
        icon.source: "images/settings_page/xmark-icon.svg"
        Material.background: Material.Red

        contentItem: Item {
            Image {
                source: activateftpbtn.icon.source
                width: activateftpbtn.icon.width
                height: activateftpbtn.icon.height
                anchors.verticalCenter: parent.verticalCenter
            }
            Text {
                text: activateftpbtn.text
                font: activateftpbtn.font
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
            }
        }
    }

}