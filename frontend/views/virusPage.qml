import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
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
        height: 35
        x: 235
        y: 45
    }

    Image {
        width: 60
        height: 60
        x: 580
        y: 45
        source: "images/virus_page/warning-icon.svg"
    }

}