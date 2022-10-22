import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

ApplicationWindow {
    // Primary color: Material.Cyan
    id: mainpage
    width: 800
    height: 480
    visible: true
    Material.theme: Material.Light
    Material.accent: Material.Red
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
        Material.background: Material.White
    }

    // The start button
    Button {
        id: startbtn
        text: "Start"
        width: 170
        height: 50
        x: 190
        y: 310
        Material.background: Material.Cyan
    }
}