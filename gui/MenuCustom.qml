import QtQuick 2.0
import QtQuick.Window 2.2
//import QtQuick.Controls 2.0
import QtQuick.Controls 2.0
import QtQuick.Dialogs 1.3


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


    //     Button {
    //         id: idUpload
    //         x: 200
    //         y: idRoot.height/2
    //         width: 200
    //         height: 200
    //         background: Rectangle {
    //                color: "grey"
    //                border.width: 1
    //                border.color: "Black"
    //                radius: 20
    //            }
    //        text: "Load Image"
    //        onClicked: {
    //            console.log("Load the image")
    //            // we call the function responsible for loading from pc
    //            // the function must handle the "return message"
    //        }
    //     }

    //     Button {
    //         id: fileButton
    //         text: "Menu"
    //         onClicked: menu.open()

    //         Menu {
    //             id: menu
    //             y: fileButton.height

    //             MenuItem {
    //                 text: "Settings"
    //             }
    //             MenuItem {
    //                 text: "Reports"
    //             }
    //             MenuItem {
    //                 text: "Save"
    //             }
    //         }
    //     }

    //     FileDialog {
    //         id: fileDialog
    //         title: "Please choose a file"
    //         folder: shortcuts.home
    //         onAccepted: {
    //             console.log("You chose: " + fileDialog.fileUrls)
    //             Qt.quit()
    //         }
    //         onRejected: {
    //             console.log("Canceled")
    //             Qt.quit()
    //         }
    //         Component.onCompleted: visible = true
    //     }

    Item {
        width: 580
        height: 400
        SystemPalette { id: palette }
        clip: true

        FileDialog {
            id: idfileDialog
//            visible: fileDialogVisible.checked
//            modality: fileDialogModal.checked ? Qt.WindowModal : Qt.NonModal
            title: "Choose File"
//            title: fileDialogSelectFolder.checked ? "Choose a folder" :
//                                                    (fileDialogSelectMultiple.checked ? "Choose some files" : "Choose a file")
//            selectExisting: fileDialogSelectExisting.checked
//            selectMultiple: fileDialogSelectMultiple.checked
//            selectFolder: fileDialogSelectFolder.checked
            nameFilters: [ "Image files (*.png *.jpg)", "All files (*)" ]
            selectedNameFilter: "All files (*)"
//            sidebarVisible: fileDialogSidebarVisible.checked
            onAccepted: {
//                console.log("Accepted: " + fileUrls)
//                if (fileDialogOpenFiles.checked)
//                    for (var i = 0; i < fileUrls.length; ++i)
//                        Qt.openUrlExternally(fileUrls[i])

                var path = idfileDialog.fileUrl.toString();
                // remove prefixed "file:///"
//                path = path.replace(/^(file:\/{3})/,"");
                // unescape html codes like '%23' for '#'
//                cleanPath = decodeURIComponent(path);
                console.log(path)
            }
            onRejected: { console.log("Rejected") }
        }

        //         ScrollView {
        //             id: scrollView
        //             anchors {
        //                 left: parent.left
        //                 right: parent.right
        //                 top: parent.top
        //                 bottom: bottomBar.top
        //                 leftMargin: 12
        //             }
        //             ColumnLayout {
        //                 spacing: 8
        //                 Item { Layout.preferredHeight: 4 } // padding
        //                 Label {
        //                     font.bold: true
        //                     text: "File dialog properties:"
        //                 }
        //                 CheckBox {
        //                     id: fileDialogModal
        //                     text: "Modal"
        //                     checked: true
        //                     Binding on checked { value: fileDialog.modality != Qt.NonModal }
        //                 }
        //                 CheckBox {
        //                     id: fileDialogSelectFolder
        //                     text: "Select Folder"
        //                     Binding on checked { value: fileDialog.selectFolder }
        //                 }
        //                 CheckBox {
        //                     id: fileDialogSelectExisting
        //                     text: "Select Existing Files"
        //                     checked: true
        //                     Binding on checked { value: fileDialog.selectExisting }
        //                 }
        //                 CheckBox {
        //                     id: fileDialogSelectMultiple
        //                     text: "Select Multiple Files"
        //                     Binding on checked { value: fileDialog.selectMultiple }
        //                 }
        //                 CheckBox {
        //                     id: fileDialogOpenFiles
        //                     text: "Open Files After Accepting"
        //                 }
        //                 CheckBox {
        //                     id: fileDialogSidebarVisible
        //                     text: "Show Sidebar"
        //                     checked: fileDialog.sidebarVisible
        //                     Binding on checked { value: fileDialog.sidebarVisible }
        //                 }
        //                 CheckBox {
        //                     id: fileDialogVisible
        //                     text: "Visible"
        //                     Binding on checked { value: fileDialog.visible }
        //                 }
        //                 Label {
        //                     text: "<b>current view folder:</b> " + fileDialog.folder
        //                 }
        //                 Label {
        //                     text: "<b>name filters:</b> {" + fileDialog.nameFilters + "}"
        //                 }
        //                 Label {
        //                     text: "<b>current filter:</b>" + fileDialog.selectedNameFilter
        //                 }
        //                 Label {
        //                     text: "<b>chosen files:</b> " + fileDialog.fileUrls
        //                 }
        //                 Label {
        //                     text: "<b>chosen single path:</b> " + fileDialog.fileUrl
        //                 }
        //             }
        //         }

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
                }
//                Button {
//                    text: "Settings"
//                    //                     tooltip: "go to my home directory"
//                    anchors.verticalCenter: parent.verticalCenter
//                    //enabled: idfileDialog.shortcuts.hasOwnProperty("Settings")
//                    onClicked: idfileDialog.folder = idfileDialog.shortcuts.home
//                }
            }
        }
    }
    Menu {
            id: contextMenu
            MenuItem { text: "View Image" }
            MenuItem { text: "ReshapeImage" }
            MenuItem { text: "Paste" }
        }

}
