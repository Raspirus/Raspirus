import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

Dialog {
    id: dialog
    title: "Confirm Selected Actions"
    modal: true
    standardButtons: Dialog.Ok | Dialog.Cancel

    onAccepted: console.log("Ok clicked")
    onRejected: console.log("Cancel clicked")
}