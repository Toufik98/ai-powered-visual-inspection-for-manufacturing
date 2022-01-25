import QtQuick 2.0
import QtQuick.Window 2.2
//import QtQuick.Controls 2.0
import QtQuick.Controls 2.3
import QtQuick.Dialogs 1.2


////


//import QtQuick 2.2
//import QtQuick.Controls 1.2
//import QtQuick.Dialogs 1.1
import QtQuick.Layouts 1.1
//import QtQuick.Window 2.0



Item {
    id: idRoot
    width: 1200
    height: 720
    SystemPalette { id: palette }

    // true: load the image, false: Unload it
    property bool bLoad: false



    FileDialog {
        id: idfileDialog
        title: "Choose "
        folder: shortcuts.pictures
        nameFilters: [ "Image files (*.png *.jpg)"]
        selectedNameFilter: "All files (*)"
        onAccepted: {
            var path = idfileDialog.fileUrl.toString();
            console.log(path)
            idMyImage.source = Qt.resolvedUrl(path)
            var index = path.lastIndexOf("/") + 1;
            var filename = path.substr(index);
            idMyText.text = filename
            QmlConnector.load_image(path)

        }
        onRejected: { console.log("Rejected") }
    }

    Column {
        id: idMyImageContainer
        width: 700
        height: 700
        x: 350
        y: 100
        opacity: 0
        spacing: 15
        Text {
            id: idMyText
            font.pixelSize: 20
            color: "white"
            style: Text.Raised
            text: ""
        }
        Image {
            id: idMyImage
            width: 500
            height: 500
            //            anchors.centerIn: parent
            source: ""
        }
        NumberAnimation {
            id: idAnimateImage
            running: false
            target: idMyImageContainer
            property: "opacity"
            from: 0
            to: 1
            duration: 2000
            easing.type: Easing.OutQuad
        }
    }



    Rectangle {
        id: bottomBar
        height: buttonRow.height * 1.2
        color: Qt.darker(palette.window, 1.1)
        border.color: Qt.darker(palette.window, 1.3)
        Row {
            id: buttonRow
            spacing: 6
            anchors.left: parent.left
            anchors.leftMargin: 12
            height: implicitHeight
            width: parent.width
            Button {
                text: "Menu"
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {contextMenu.popup()}
            }
            Button {
                text: "Upload Image"
                anchors.verticalCenter: parent.verticalCenter
                onClicked: idfileDialog.open()
            }

            Button {
                text: "Send Image"
                anchors.verticalCenter: parent.verticalCenter
                onClicked: {
                    QmlConnector.send_image()
                }
            }
            Button {
                text: "Display Image"
                onClicked: {
                    //si on clique une fois we load the image
                    // si on clique deux fois we Unload the image
                    bLoad = !bLoad
                }
            }
        }
    }

    Text {
        id: idMyText2
        font.pixelSize: 20
        color: "white"
        style: Text.Raised
        text: "Merde"
    }

    Menu {
        id: contextMenu
        cascade: true
        MenuItem { text: "Reports" }
        MenuItem { text: "ReshapeImage" }
        MenuItem { text: "Paste" }
    }

   /*onBLoadChanged: {
        console.log("Heyyyyyyyyyyyyyyyyy: " + bLoad )
        if (true === bLoad){
            idAnimateImage.from = 0
            idAnimateImage.to = 1
            idAnimateImage.running = true

        }
        else {
            idAnimateImage.from = 1
            idAnimateImage.to = 0
            idAnimateImage.running = true
        }
    }*/

    Connections {
        target: QmlConnector
        function onLabel(Label) {
            idMyText2.text = Label
        }
    }
}