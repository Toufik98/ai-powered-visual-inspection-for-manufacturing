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
    property var  bLocalPath: ""



    FileDialog {
        id: idfileDialog
        title: "Choose "
        folder: shortcuts.pictures
        nameFilters: [ "Image files (*.png *.jpeg *.jpg *.gif)" ]
        selectedNameFilter: "All files (*)"
        onAccepted: {
            var path = idfileDialog.fileUrl.toString();
            //console.log("File dialog: "+path)
            idMyImage_drop.source = Qt.resolvedUrl(path)
            var index = path.lastIndexOf("/") + 1;
            var filename = path.substr(index);
            //idMyText.text = filename
            QmlConnector.load_image(path)
            idMyImage_drop.source = Qt.resolvedUrl(path)
            idMyRectangle_drop.width = 0
            idMyRectangle_drop.height = 0
            idMyRectangle_drop.x = 0
            idMyRectangle_drop.y = 0


        }
        onRejected: { console.log("Rejected") }
    }

    /*Column {
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
       
    }*/

  


    /*Rectangle {
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
    }*/

    

    ////////////////////////////////////////////////////////////////////////////////////////
    // this row will hold the buttons, to upload directly from dektop, and to generate reports
    ////////////////////////////////////////////////////////////////////////////////////////
   Item {
       id: idFirstRow
       x: 200
       y: 80
        width: 1200
        height: 300
        
            //Icon Upload
            Rectangle {
                x: 100
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
                y: 105
                text: "Upload"
                font.pixelSize: 22
            }

             //Icon send
            Rectangle {
                x: 250
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
                        var data = QmlConnector.send_image()
                        console.log("data: " + data)
                        idMyRectangle_drop.width = data[5]
                        idMyRectangle_drop.height = data[6]
                        idMyRectangle_drop.x = data[3]
                        idMyRectangle_drop.y = data[4]
                        
                    }
                }
        }
            
            
            Text {
                x: 225
                y: 105
                text: "Send To Server"
                font.pixelSize: 22
            }

        //Classify 
           Rectangle {
                x: 400
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
                y: 105
                text: "Classify "
                font.pixelSize: 22
            }
    
        
    //section generate reports
     
             Rectangle{
                x: 550
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
                x: 500
                y: 105
                text: "Generate Report"
                font.pixelSize: 22
            }
        
       }
   
    ////////////////////////////////////////////////////////////////////////////////
    // this row will be responisble for visualsing the image uploaded, and predicted
    ////////////////////////////////////////////////////////////////////////////////
    Row {
        id: idSecondRow
        x: 150
        y: 300
        spacing: 10
    Item {
        width: 300
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
                x: 80
                y: 170
                text: "Drag and drop image"
                font.pixelSize: 16
        }
       
        // Instanciate DropArea
        DropArea {
            id: dropArea
            anchors.fill: parent
            
            onDropped: {
                var path = drop.text
                console.log("paaaaaaaaaaaaaath:   "+ path)
                //todo replace
                idMyImage_drop.source =  path.slice(0,-2)
                console.log("idImageDropped.source :   "+ idMyImage_drop.source)

                 //bLocalPath = path
                //console.log("bLocalPath:   "+ bLocalPath)
                //console.log("idImageDropped.source:  " + idMyImage_drop.source)
                //idImageDropped.source = "file:///home/asma/ai-powered-visual-inspection-for-manufacturing/gui/MU5TYL.png"
                // QmlConnector.load_image(path)
                //idImageDropped.source = Qt.resolvedUrl(path)
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

        Image {
            id: idMyImage_drop
            width: 224
            height: 224
            source: ""
            anchors.centerIn: parent
            Rectangle {
                id: idMyRectangle_drop
                width: 0
                height: 0
                color: "transparent"
                border.color: "blue"

            }
        }
    }

     

    
    //section resultats
    Item {
        width: 600
        height: 300
        Rectangle {
            anchors.fill: parent
            color: "#B6D5DA"
            radius: 50
        } 
        Text {
            x: 200
            text: "Inspection Results:"
            font.pixelSize: 22
        }
        Row {
            width: 600
            Row {
                x: 100
                y: 50
                width: parent.width
                Text {
                    text: "Label: "
                    font.pixelSize: 16
                    }
                Text {
                    id: idLabel
                    text: ""

                }
            }
               Row {
                   width: parent.width
                   x: 100
                   y: 150
                Text {
                    text: "Card Name: "
                    font.pixelSize: 16
                    }
                Text {
                    id: idCardName
                    text: ""
                    
                }
            }
        }
        
    }

    }
    

    

  
   
    //////////////////////////////////////////////////////////////////////////////
    //connection with the QmlConnector Component and catch the signals sent from Py
    //////////////////////////////////////////////////////////////////////////////
     


     
   NumberAnimation {
            id: idAnimateImage
            running: false
            target: idMyRectangle_drop
            property: "opacity"
            from: 0
            to: 1
            duration: 2000
            easing.type: Easing.OutQuad
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


}

