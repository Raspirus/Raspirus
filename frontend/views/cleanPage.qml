import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    // Primary color: Material.Cyan
    id: cleanpage
    // flags: Qt.FramelessWindowHint
    width: 800
    height: 480
    visible: true
    Material.theme: Material.Light
    title: "Raspirus - CLEAN"

    Label {
        text: "NO VIRUS FOUND"
        font.pixelSize: 48
        color: Material.color(Material.Green)
        width: 325
        height: 60
        x: 200
        y: 45
    }

    Image {
        width: 200
        height: 200
        x: 300
        y: 140
        source: "images/clean_page/partying-face.png"
    }

    Button {
        id: confirmbtn
        text: "SUBMIT"
        font.pixelSize: 24
        width: 170
        height: 50
        x: 315
        y: 380
        Material.background: Material.Green
        onClicked: {
            // Needs to be replaced with signals
            var component = Qt.createComponent("main.qml")
            var window = component.createObject(cleanpage)
            window.show()
            cleanpage.hide()
        }
    }
}