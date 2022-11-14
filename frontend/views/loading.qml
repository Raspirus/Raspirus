import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    // Primary color: Material.Cyan
    id: loadingpage
    // flags: Qt.FramelessWindowHint
    width: 800
    height: 480
    visible: true
    Material.theme: Material.Light
    title: "Raspirus - LOADING"

    Label {
        text: "Scanning... Please wait"
        font.pixelSize: 64
        color: Material.color(Material.Cyan)
        width: 630
        height: 125
        x: 85
        y: 115
    }

    Rectangle {
        property int percentage: 61
        id: progressbar
        x: 50
        y: 225
        width: 700
        height: 45
        border.width: 1

        Item {
            id: cliprect
            anchors.bottom: parent.bottom
            anchors.top: parent.top
            anchors.left: parent.left
            width: parent.width * parent.percentage / 100
            clip: true

            Rectangle {
                width: progressbar.width
                height: progressbar.height
                anchors.bottom: parent.bottom
                anchors.left: parent.left
                color: Material.color(Material.Cyan)
            }
        }

        Text {
            text: progressbar.percentage + " %"
            font: progressbar.font
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }

    Label {
        id: filescanned
        property int fscanned: 123
        property int toscan: 1234
        text: "Scanned " + fscanned + " files of " + toscan + " total"
        font.pixelSize: 16
        width: 280
        height: 30
        x: 50
        y: 280
    }

    Label {
        id: virusfound
        property int vfound: 0
        text: "Virus found " + vfound
        font.pixelSize: 16
        width: 280
        height: 30
        x: 50
        y: 315
    }

    RoundButton {
        id: exitbutton
        width: 60
        height: 60
        x: 375
        y: 380
        radius: 90
        icon.source: "images/loading_page/xmark-icon.svg"
        icon.height: exitbutton.height
        icon.width: exitbutton.width
        Material.background: Material.Red
    }

}