import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15
import Qt.labs.platform

Window {
  id: window
  width: 1000
  height: 500
  visible: true
  title: windowTitle
  color: backgroundWindowColor

  property string backgroundWindowColor: "#212834"
  property string highlightedTextColor: "#0079F2"
  property string windowTitle: qsTr("foggie")
  property int defaultMargin: 8

  StackLayout {
    id: mainStackLayout

    anchors.fill: parent

    property int authorizationSectionIndex: 0
    property int storeSectionIndex: 1

    StackLayout {
			id: authStackLayout

			anchors.fill: parent
			anchors.margins: 8

	    property int signInFormIndex: 0
	    property int signUpFormIndex: 1

	    ColumnLayout {
				id: signInForm
				anchors.centerIn: parent

				FormInputLabel {
				  text: qsTr("ACCOUNT NAME")
				  color: highlightedTextColor
				}
				FormInput {
				  id: signInAccountNameInput
          focus: true
        }

				Indent {}

				FormInputLabel {text: qsTr("PASSWORD")}
				FormInput {}

        Indent {}

				ActionButton {
					Layout.alignment: Qt.AlignHCenter
					text: qsTr("Sign in")
				}

				Indent {}

				RowLayout {
					Layout.alignment: Qt.AlignHCenter

					Span {text: qsTr("Need an account?")}

          Link {
            message: qsTr("Sign up")

            function handler() {
              signUpEmailInput.focus = true
              authStackLayout.currentIndex = authStackLayout.signUpFormIndex
            }
          }
        }
      }

      ColumnLayout {
				id: signUpForm
				anchors.centerIn: parent

        FormInputLabel {text: qsTr("EMAIL")}
				FormInput {
				  id: signUpEmailInput
				}

				Indent {}

				FormInputLabel {text: qsTr("ACCOUNT NAME")}
				FormInput {}

				Indent {}

				FormInputLabel {text: qsTr("PASSWORD")}
				FormInput {}

        Indent {}

				ActionButton {
					Layout.alignment: Qt.AlignHCenter
					text: qsTr("Sign up")
				}

				Indent {}

				RowLayout {
					Layout.alignment: Qt.AlignHCenter

					Span {text: qsTr("Already have an account?")}

          Link {
            message: qsTr("Sign in")

            function handler() {
              signInAccountNameInput.focus = true
              authStackLayout.currentIndex = authStackLayout.signInFormIndex
            }
          }
        }
      }
    }
  }
}