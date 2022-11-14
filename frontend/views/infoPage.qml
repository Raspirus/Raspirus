import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    // Primary color: Material.Cyan
    id: infopage
    // flags: Qt.FramelessWindowHint
    width: 800
    height: 480
    visible: true
    Material.theme: Material.Light
    title: "Raspirus - INFO"

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

        onClicked: {
            // Needs to be replaced with signals
            var component = Qt.createComponent("main.qml")
            var window = component.createObject(infopage)
            window.show()
            infopage.hide()
        }

    }

    Label {
        text: "APP INFO"
        font.pixelSize: 48
        color: Material.color(Material.DeepPurple)
        width: 325
        height: 60
        y: 45
        x: 290
    }

    Rectangle {
        property string name: "Raspirus"
        property string version: "v1.0.0"
        property string creator: "Benjamin Demetz"
        property string license: "Alperia AG"
        property string contact: "demetzbenjamin23@gmail.com"
        property int tmargin: 20
        property int lrmargin: 20
        width: 745
        height: 270
        x: 25
        y: 155
        border.width: 1
        border.color: Material.color(Material.Cyan)

        Text {
            id: nametxt
            text: "Name:"
            font.pixelSize: 20
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.topMargin: parent.tmargin
            anchors.leftMargin: parent.lrmargin
        }

        Text {
            text: parent.name
            font.pixelSize: 20
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.topMargin: parent.tmargin
            anchors.rightMargin: parent.lrmargin
        }

        Text {
            id: versiontxt
            text: "Version:"
            font.pixelSize: 20
            anchors.left: parent.left
            anchors.top: nametxt.bottom
            anchors.topMargin: parent.tmargin
            anchors.leftMargin: parent.lrmargin
        }

        Text {
            text: parent.version
            font.pixelSize: 20
            anchors.right: parent.right
            anchors.top: nametxt.bottom
            anchors.topMargin: parent.tmargin
            anchors.rightMargin: parent.lrmargin
        }

        Text {
            id: creatortxt
            text: "Creator:"
            font.pixelSize: 20
            anchors.left: parent.left
            anchors.top: versiontxt.bottom
            anchors.topMargin: parent.tmargin
            anchors.leftMargin: parent.lrmargin
        }

        Text {
            text: parent.creator
            font.pixelSize: 20
            anchors.right: parent.right
            anchors.top: versiontxt.bottom
            anchors.topMargin: parent.tmargin
            anchors.rightMargin: parent.lrmargin
        }

        Text {
            id: licensetxt
            text: "License:"
            font.pixelSize: 20
            anchors.left: parent.left
            anchors.top: creatortxt.bottom
            anchors.topMargin: parent.tmargin
            anchors.leftMargin: parent.lrmargin
        }

        Text {
            text: parent.license
            font.pixelSize: 20
            anchors.right: parent.right
            anchors.top: creatortxt.bottom
            anchors.topMargin: parent.tmargin
            anchors.rightMargin: parent.lrmargin
        }

        Text {
            id: contacttxt
            text: "Contact:"
            font.pixelSize: 20
            anchors.left: parent.left
            anchors.top: licensetxt.bottom
            anchors.topMargin: parent.tmargin
            anchors.leftMargin: parent.lrmargin
        }

        Text {
            text: parent.contact
            font.pixelSize: 20
            anchors.right: parent.right
            anchors.top: licensetxt.bottom
            anchors.topMargin: parent.tmargin
            anchors.rightMargin: parent.lrmargin
        }

    }
}