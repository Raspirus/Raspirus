// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial

import QtQuick 2.12
import QtQuick.Controls 2.12

Page {
    width: 640
    height: 480
    required property var myModel

    header: Label {
        color: "#15af15"
        text: qsTr("Where do people use Qt?")
        font.pointSize: 17
        font.bold: true
        font.family: "Arial"
        renderType: Text.NativeRendering
        horizontalAlignment: Text.AlignHCenter
        padding: 10
    }
    Rectangle {
        id: root
        width: parent.width
        height: parent.height

        Image {
            id: image
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: root
            source: "../images/logo.png"
            opacity: 0.5

        }

        ListView {
            id: view
            anchors.fill: root
            anchors.margins: 25
            model: myModel
            delegate: Text {
                anchors.leftMargin: 50
                font.pointSize: 15
                horizontalAlignment: Text.AlignHCenter
                text: display
            }
        }
    }
    NumberAnimation {
        id: anim
        running: true
        target: view
        property: "contentY"
        duration: 500
    }
}
