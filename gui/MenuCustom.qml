import QtQuick 2.0
import QtQuick.Window 2.2
//import QtQuick.Controls 2.0
import QtQuick.Controls 2.0

Item {
    id: idRoot
    width: 1800
    height: 720


     Button {
         id: idUpload
         x: 200
         y: idRoot.height/2
         width: 200
         height: 200
         background: Rectangle {
                color: "grey"
                border.width: 1
                border.color: "Black"
                radius: 20
            }
        text: "Load Image"
        onClicked: {
            console.log("Load the image")
            // we call the function responsible for loading from pc
            // the function must handle the "return message"
        }
     }

     Button {
         id: fileButton
         text: "Menu"
         onClicked: menu.open()

         Menu {
             id: menu
             y: fileButton.height

             MenuItem {
                 text: "Settings"
             }
             MenuItem {
                 text: "Reports"
             }
             MenuItem {
                 text: "Save"
             }
         }
     }



}
