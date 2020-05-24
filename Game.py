# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random

class UiMainWindow(object):

    def __init__(self):
        self.chanceCounter = 5
        self.rangeStart = 0
        self.rangeEnd = 0
        self.rangeDifference = 10
        self.number = 0
        self.guess = 0

    def setupUi(self, MainWindow):
        # MainWindow----------------------------------------------------------------------------------------------------
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 400))
        MainWindow.setMaximumSize(QtCore.QSize(350, 400))
        font = QtGui.QFont()
        font.setFamily("Nunito SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        # CentralWidget-------------------------------------------------------------------------------------------------
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        # VerticalLayout------------------------------------------------------------------------------------------------
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        # LabelTop------------------------------------------------------------------------------------------------------
        self.labelTop = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTop.sizePolicy().hasHeightForWidth())
        self.labelTop.setSizePolicy(sizePolicy)
        self.labelTop.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTop.setFont(font)
        self.labelTop.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelTop.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelTop.setLineWidth(1)
        self.labelTop.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTop.setObjectName("labelTop")
        self.verticalLayout.addWidget(self.labelTop)
        # LAbelHint-----------------------------------------------------------------------------------------------------
        self.labelHint = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHint.sizePolicy().hasHeightForWidth())
        self.labelHint.setSizePolicy(sizePolicy)
        self.labelHint.setMinimumSize(QtCore.QSize(0, 50))
        self.labelHint.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.labelHint.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHint.setObjectName("labelHint")
        self.verticalLayout.addWidget(self.labelHint)
        # HorizontalLayout----------------------------------------------------------------------------------------------
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Spacer1-------------------------------------------------------------------------------------------------------
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        # EdtAnswer-----------------------------------------------------------------------------------------------------
        self.edtAnswer = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtAnswer.sizePolicy().hasHeightForWidth())
        self.edtAnswer.setSizePolicy(sizePolicy)
        self.edtAnswer.setMinimumSize(QtCore.QSize(60, 60))
        self.edtAnswer.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.edtAnswer.setFont(font)
        self.edtAnswer.setValidator(QtGui.QIntValidator())
        self.edtAnswer.setMaxLength(3)
        self.edtAnswer.setAlignment(QtCore.Qt.AlignCenter)
        self.edtAnswer.setObjectName("edtAnswer")
        self.horizontalLayout.addWidget(self.edtAnswer)
        # Spacer2-------------------------------------------------------------------------------------------------------
        spacerItem1 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        # BtnCheck------------------------------------------------------------------------------------------------------
        self.btnCheck = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCheck.sizePolicy().hasHeightForWidth())
        self.btnCheck.setSizePolicy(sizePolicy)
        self.btnCheck.setMinimumSize(QtCore.QSize(60, 60))
        self.btnCheck.setMaximumSize(QtCore.QSize(60, 60))
        self.btnCheck.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnCheck.setInputMethodHints(QtCore.Qt.ImhNone)
        self.btnCheck.setObjectName("btnCheck")
        self.horizontalLayout.addWidget(self.btnCheck)
        # Spacer3-------------------------------------------------------------------------------------------------------
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        # LabelCounter--------------------------------------------------------------------------------------------------
        self.labelCounter = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCounter.sizePolicy().hasHeightForWidth())
        self.labelCounter.setSizePolicy(sizePolicy)
        self.labelCounter.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelCounter.setFont(font)
        self.labelCounter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelCounter.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.labelCounter.setObjectName("labelCounter")
        self.verticalLayout.addWidget(self.labelCounter)
        # LabelResult---------------------------------------------------------------------------------------------------
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelResult.sizePolicy().hasHeightForWidth())
        self.labelResult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelResult.setFont(font)
        self.labelResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)
        MainWindow.setCentralWidget(self.centralwidget)
        # MenuBar-------------------------------------------------------------------------------------------------------
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 350, 24))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        # MenuOptions---------------------------------------------------------------------------------------------------
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menuOptions.setFont(font)
        self.menuOptions.setObjectName("menuOptions")
        # MenuDifficulty------------------------------------------------------------------------------------------------
        self.menuDifficulty = QtWidgets.QMenu(self.menuOptions)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(9)
        self.menuDifficulty.setFont(font)
        self.menuDifficulty.setObjectName("menuDifficulty")
        MainWindow.setMenuBar(self.menuBar)
        # ActionRestartGame---------------------------------------------------------------------------------------------
        self.actionRestartGame = QtWidgets.QAction(MainWindow)
        self.actionRestartGame.setCheckable(False)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.actionRestartGame.setFont(font)
        self.actionRestartGame.setObjectName("actionRestartGame")
        # ActionExitGame------------------------------------------------------------------------------------------------
        self.actionExitGame = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(9)
        self.actionExitGame.setFont(font)
        self.actionExitGame.setObjectName("actionExitGame")
        # ActionEasy----------------------------------------------------------------------------------------------------
        self.actionEasy = QtWidgets.QAction(MainWindow)
        self.actionEasy.setCheckable(True)
        self.actionEasy.setChecked(True)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(9)
        self.actionEasy.setFont(font)
        self.actionEasy.setObjectName("actionEasy")
        # ActionMedium--------------------------------------------------------------------------------------------------
        self.actionMedium = QtWidgets.QAction(MainWindow)
        self.actionMedium.setCheckable(True)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(9)
        self.actionMedium.setFont(font)
        self.actionMedium.setObjectName("actionMedium")
        # ActionHard----------------------------------------------------------------------------------------------------
        self.actionHard = QtWidgets.QAction(MainWindow)
        self.actionHard.setCheckable(True)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(9)
        self.actionHard.setFont(font)
        self.actionHard.setObjectName("actionHard")
        self.menuDifficulty.addAction(self.actionEasy)
        self.menuDifficulty.addAction(self.actionMedium)
        self.menuDifficulty.addAction(self.actionHard)
        self.menuOptions.addAction(self.actionRestartGame)
        self.menuOptions.addAction(self.menuDifficulty.menuAction())
        self.menuOptions.addAction(self.actionExitGame)
        self.menuBar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Number Guessing Game"))
        self.labelTop.setText(_translate("MainWindow", "What\'s your guess?"))
        self.labelHint.setText(_translate("MainWindow", "Hint:"))
        self.btnCheck.setText(_translate("MainWindow", "GO"))
        self.labelCounter.setText(_translate("MainWindow", "{} chances left.".format(self.chanceCounter)))
        self.labelResult.setText(_translate("MainWindow", ""))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuDifficulty.setTitle(_translate("MainWindow", "Difficulty"))
        self.actionRestartGame.setText(_translate("MainWindow", "Restart Game"))
        self.actionExitGame.setText(_translate("MainWindow", "Exit Game"))
        self.actionEasy.setText(_translate("MainWindow", "Easy"))
        self.actionMedium.setText(_translate("MainWindow", "Medium"))
        self.actionHard.setText(_translate("MainWindow", "Hard"))
        # setup game as easy
        self.difficultCheckMenu(0)
        self.setActionsToUi()

    def setActionsToUi(self):
        self.menuOptions.triggered[QtWidgets.QAction].connect(self.menuFunction)
        self.btnCheck.clicked.connect(self.checkTheGuess)

    def menuFunction(self, action):
        actiontext = action.text()
        if actiontext == 'Exit Game':
            sys.exit(0)
        elif actiontext == 'Restart Game':
            self.resetGame()
            pass
        elif actiontext == 'Easy':
            self.difficultCheckMenu(0)
            pass
        elif actiontext == 'Medium':
            self.difficultCheckMenu(1)
            pass
        elif actiontext == 'Hard':
            self.difficultCheckMenu(2)
            pass

    def resetGame(self):
        self.edtAnswer.setText("")
        self.labelHint.setText("Hint:")
        self.labelCounter.setText(str(self.chanceCounter) + " chances left")
        self.labelResult.setText("")
        self.btnCheck.setEnabled(True)
        self.chanceCounter = 5
        self.chooseNumber()
        pass

    def difficultCheckMenu(self, d):
        # uncheck all checkbox and then check the one selected
        self.actionEasy.setChecked(False)
        self.actionMedium.setChecked(False)
        self.actionHard.setChecked(False)
        if d == 0:
            self.actionEasy.setChecked(True)
            self.rangeDifference = 10
        elif d == 1:
            self.actionMedium.setChecked(True)
            self.rangeDifference = 15
        elif d == 2:
            self.actionHard.setChecked(True)
            self.rangeDifference = 20
        # Now setup the number and game
        self.resetGame()
        self.chooseNumber()
        pass

    def chooseNumber(self):
        self.rangeStart = random.randint(1, 100)
        self.rangeEnd = self.rangeStart + self.rangeDifference
        self.number = random.randint(self.rangeStart, self.rangeEnd)
        self.labelHint.setText("Hint: The number lies between {} and {}.".format(self.rangeStart, self.rangeEnd))

    def checkTheGuess(self):
        if self.edtAnswer.text() == "":
            return
        self.guess = int(self.edtAnswer.text())
        print(self.guess)
        print(self.number)
        self.chanceCounter -= 1
        result = ""
        if self.guess == self.number:
            self.btnCheck.setEnabled(False)
            result = 'Well Done! You are smart enough.'
            pass
        elif self.guess > self.number:
            result = 'Guess lower.'
            pass
        elif self.guess < self.number:
            result = 'Guess higher.'
            pass
        self.labelResult.setText(result)
        if self.chanceCounter == 0:
            self.btnCheck.setEnabled(False)
            self.labelCounter.setText("OOPS! Out of chabces.")
            pass
        else:
            self.labelCounter.setText('{} chances left.'.format(self.chanceCounter))
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
