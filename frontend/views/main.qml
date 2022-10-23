import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    // Primary color: Material.Cyan
    id: mainpage
    // flags: Qt.FramelessWindowHint
    width: 800
    height: 480
    visible: true
    Material.theme: Material.Light
    title: "Raspirus"

    // The settings button
    Button {
        id: settingsbtn
        text: "Settings"
        width: 100
        height: 50
        x: 680
        y: 10
        Material.foreground: Material.DeepOrange
        Material.background: "#fff"
        onClicked: {
            // Needs to be replaced with signals
            var component = Qt.createComponent("settings.qml")
            var window    = component.createObject(mainpage)
            window.show()
            mainpage.visible = 0
        }
    }

    Label {
        text: "RASPIRUS"
        font.pixelSize: 64
        color: Material.color(Material.Cyan)
        width: 510
        height: 120
        x: 250
        y: 110
    }

    ComboBox {
        id: combo
        editable: false
        width: 610
        height: 50
        x: 100
        y: 210
        currentIndex: 2
        // Need to be emptied and replaced with the actual hardware names
        model: ["Test1", "Test2", "Test3"]
    }

    // The start button
    Button {
        id: startbtn
        text: "START"
        width: 170
        height: 50
        x: 190
        y: 310
        Material.background: Material.Cyan
    }

    Button {
        id: infobtn
        text: "INFO"
        width: 170
        height: 50
        x: 420
        y: 310
        Material.foreground: Material.Cyan
        Material.background: "#fff"
    }
}