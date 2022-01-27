import QtQuick 2.0
import QtQuick.Window 2.2
//import QtQuick.Controls 2.0
import QtQuick.Controls 2.3
import QtQuick.Dialogs 1.2
import QtPositioning 5.5
import QtLocation 5.6

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
    property var  labelLocal: ""
    property int  xLocal: 0
    property int  yLocal: 0
    property int  widthLocal: 0
    property int  heightLocal: 0
    property bool bLoadReport: false



    FileDialog {
        id: idfileDialog
        title: "Choose "
        folder: shortcuts.pictures
        nameFilters: [ "Image files (*.png *.jpg)"]
        selectedNameFilter: "All files (*)"
        onAccepted: {
            var path = idfileDialog.fileUrl.toString();
            //console.log("File dialog: "+path)
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

   onBLoadChanged: {
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
    }
    ////////////////////////////////////////////////////////////////////////////////////////
    // this row will hold the buttons, to upload directly from dektop, and to generate reports
    ////////////////////////////////////////////////////////////////////////////////////////
   Row {
       id: idFirstRow
       y: 80
       spacing: 10
        Item {
            width: 600
            height: 300
            // color: "#B6D5DA"
            // radius: 50
            
            //Icon Upload
            Rectangle{
                x: 100
                y: x
                width: 100
                height: 100
                color:  "#b8e0e7"
                radius: 100
            Image {
                id: idUploadImage
                width: 50
                height: 50
                anchors.centerIn: parent
                source: "ICONS/upload.png"
                
            }
            MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                     property bool hovered: false
                    onEntered:  {
                        console.log("hiiiiii m hoveriiiiiiiiiiiiiiiiiing on ur btn ")
                        hovered = true
                        parent.opacity = 0.5
                    }
                    onExited: parent.opacity = 1
                    onClicked: { 
                        idfileDialog.open()
                    }
                }
        }

            Text {
                x: 110
                y: 205
                text: "Upload"
                font.pixelSize: 22
            }

             //Icon send
            Rectangle{
                x: 250
                y: 100
                width: 100
                height: 100
                color:  "#b8e0e7"
                radius: 100
            Image {
                id: idSendImage
                width: 50
                height: 50
                anchors.centerIn: parent
                source: "ICONS/send.png"
                
            }
            MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                     property bool hovered: false
                    onEntered:  {
                        console.log("hiiiiii m hoveriiiiiiiiiiiiiiiiiing on ur btn ")
                        hovered = true
                        parent.opacity = 0.5
                    }
                    onExited: parent.opacity = 1
                    onClicked: { 
                        QmlConnector.send_image()
                    }
                }
        }
            
            
            Text {
                x: 225
                y: 205
                text: "Send To Server"
                font.pixelSize: 22
            }

        //Classify 
           Rectangle{
                x: 400
                y: 100
                width: 100
                height: 100
                color:  "#b8e0e7"
                radius: 100
            Image {
                id: idClassify
                width: 50
                height: 50
                anchors.centerIn: parent
                source: "ICONS/inspect.png"
                
            }
            MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                     property bool hovered: false
                    onEntered:  {
                        console.log("hiiiiii m hoveriiiiiiiiiiiiiiiiiing on ur btn ")
                        hovered = true
                        parent.opacity = 0.5
                    }
                    onExited: parent.opacity = 1
                    onClicked: { 
                        QmlConnector.send_image()
                    }
                }
        }
           
            Text {
                x: 400
                y: 205
                text: "Classify "
                font.pixelSize: 22
            }
    
             
        }
       
            

    //section generate reports
       Item {
            width: 600
            height: 300
             Rectangle{
                anchors.centerIn: parent
                width: 100
                height: 100
                color:  "#b8e0e7"
                radius: 100
            Image {
                id: idGenerateReports
                width: 50
                height: 50
                anchors.centerIn: parent
                source: "ICONS/generate_report.png"
                
            }
            MouseArea {
                    anchors.fill: parent
                    hoverEnabled: true
                     property bool hovered: false
                    onEntered:  {
                        console.log("hiiiiii m hoveriiiiiiiiiiiiiiiiiing on ur btn ")
                        hovered = true
                        parent.opacity = 0.5
                    }
                    onExited: parent.opacity = 1
                    onClicked: { 
                        bLoadReport = true
                    }
                }
        }
       
            Text {
                x: 220
                y: 200
                text: "Generate Report"
                font.pixelSize: 22
            }
        }
       }
   
    ////////////////////////////////////////////////////////////////////////////////
    // this row will be responisble for visualsing the image uploaded, and predicted
    ////////////////////////////////////////////////////////////////////////////////
    Row {
        id: idSecondRow
        y: 400
        spacing: 10
    Item {
        width: 600
        height: 300
         Rectangle {
            anchors.fill: parent
            color: "#B6D5DA"
            radius: 50
        }
        
        Image {
                id: idDragAndDrop
                width: 50
                height: 50
                anchors.centerIn: parent
                source: "ICONS/drag_and_drop.png"
            }

            Text {
                x: 200
                y: 170
            text: "Drag and drop image"
            font.pixelSize: 22
        }
        // Instanciate DropArea
        DropArea {
            id: dropArea
            anchors.fill: parent
            onDropped: {
                var path = drop.text
                console.log("ppppppppppppppppath: "+path)
                console.log(path)
                QmlConnector.load_image(path)
                //idMyImage.source = Qt.resolvedUrl(path)
                //var index = path.lastIndexOf("/") + 1
                //var filename = path.substr(index)
                //idMyText.text = filename
                //QmlConnector.load_image(path)
            }
            onEntered: {
                console.log("Entred")
            }
            onExited: {
                console.log("Exited")
            }
        }
         //ProgressBar {
        //id: idPogressBar
        //value: 0.5
    //}
    }
    //section resultats
    Item {
        width: 600
        height: 300
        Image {
            id: idMyImageAfterPrediction
            //visible: (labelLocal == "Defected") ? true: false
            source: ""
        }
        Rectangle {
            x: xLocal
            y: yLocal
            width: widthLocal
            height: heightLocal
            //visible: (labelLocal == "Defected") ? true: false

        }
        Rectangle {
            anchors.fill: parent
            color: "#B6D5DA"
            radius: 50
        } 
    }


    }
   
    //////////////////////////////////////////////////////////////////////////////
    //connection with the QmlConnector Component and catch the signals sent from Py
    //////////////////////////////////////////////////////////////////////////////
     Connections {
        target: QmlConnector
        function onLabel(Label, X, Y, Width, Height) {
            labelLocal = Label
            xLocal = X
            yLocal = Y
            widthLocal = Width
            heightLocal = Height
            idMyText2.text = Label
        }
    }


}

