from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
def window():
    # ========== Layouts Instance ==========
    layouts = QVBoxLayout() # Layout paling besar
    topLayout = QHBoxLayout()
    midLayout = QHBoxLayout()
    bottomLayout = QHBoxLayout()

    # ========== Top Layout ==========
    palette = app.palette() # Untuk Palette
    styleOption = QComboBox()
    styleOption.addItems(QStyleFactory.keys()) # Windows Vista, Windows, Fusion

    styleLabel = QLabel("&Style:")
    styleLabel.setBuddy(styleOption)
    usePalette = QCheckBox("&Use style's standart palette")
    usePalette.setChecked(True)

    disableWidget = QCheckBox("&Disable widgets")
    def changeStyle(theme):
        app.setStyle(theme)
        changePalette()
    def changePalette():
        if (usePalette.isChecked()):
            app.setPalette(app.style().standardPalette())
        else:
            app.setPalette(palette)
    styleOption.activated[str].connect(changeStyle)
    usePalette.toggled.connect(changePalette)

    topLayout.addWidget(styleLabel)
    topLayout.addWidget(styleOption)
    topLayout.addStretch(1)
    topLayout.addWidget(usePalette)
    topLayout.addWidget(disableWidget)

    # ========== Mid Layout ==========
    # ------ Group 1 ------
    group1 = QGroupBox("Group 1")
    rb1 = QRadioButton("Radio Button 1")
    rb2 = QRadioButton("Radio Button 2")
    rb3 = QRadioButton("Radio Button 3")
    rb1.setChecked(True)

    triState = QCheckBox("Tri-State Checkbox")
    triState.setTristate(True)
    triState.setCheckState(Qt.PartiallyChecked)

    group1Layout = QVBoxLayout()
    group1Layout.addWidget(rb1)
    group1Layout.addWidget(rb2)
    group1Layout.addWidget(rb3)
    group1Layout.addWidget(triState)
    group1.setLayout(group1Layout)

    # ------ Group 2 ------
    group2 = QGroupBox("Group 2")
    defaultPB = QPushButton("Default Push Button")
    defaultPB.setDefault(True)
    toggledPB = QPushButton("Toggled Push Button")
    toggledPB.setChecked(True) # Ceklisnya gak perlu ditahan
    toggledPB.setCheckable(True)
    flatPB = QPushButton("Flat Push Button")
    flatPB.setFlat(True)

    group2Layout = QVBoxLayout()
    group2Layout.addWidget(defaultPB)
    group2Layout.addWidget(toggledPB)
    group2Layout.addWidget(flatPB)
    group2Layout.addStretch(1)
    group2.setLayout(group2Layout)

    # ========== Bottom Layout ==========
    # ------ Group 4 ------
    group4 = QTabWidget()

    tableTab = QWidget()
    tableWidget = QTableWidget(10, 10)
    tableTabLayout = QHBoxLayout()
    tableTabLayout.setContentsMargins(5, 5, 5, 5)
    tableTabLayout.addWidget(tableWidget)
    tableTab.setLayout(tableTabLayout)

    textTab = QWidget()
    editArea = QTextEdit()
    textTabLayout = QHBoxLayout()
    textTabLayout.setContentsMargins(5, 5, 5, 5)
    textTabLayout.addWidget(editArea)
    textTab.setLayout(textTabLayout)

    group4.addTab(tableTab, "&Table")
    group4.addTab(textTab, "Text &Edit")

    # ------ Group 3 ------
    group3 = QGroupBox("Group 3")
    group3.setCheckable(True)
    group3.setChecked(True)

    pwd = QLineEdit()
    pwd.setEchoMode(QLineEdit.Password)

    spinBox = QSpinBox()
    spinBox.setValue(50)

    dateTimeEdit = QDateTimeEdit()
    dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    slider = QSlider(Qt.Vertical)
    slider.setValue(40)

    scrollBar = QScrollBar(Qt.Horizontal)
    scrollBar.setValue(60)

    dial = QDial()
    dial.setValue(100)
    # dial.setNotchesVisible(True)

    group3Layout = QFormLayout()
    group3Layout.addRow(pwd)
    group3Layout.addRow(spinBox)
    group3Layout.addRow(dateTimeEdit)

    tmp1 = QHBoxLayout()
    tmp2 = QVBoxLayout()
    tmp2.addWidget(slider)
    tmp2.addWidget(scrollBar)
    tmp1.addLayout(tmp2)
    tmp1.addWidget(dial)
    group3Layout.addRow(tmp1)

    group3.setLayout(group3Layout)

    # ========== Progess Bar ==========
    def barLoading():
        curVal = progressBar.value()
        maxVal = progressBar.maximum()
        progressBar.setValue(curVal + (maxVal - curVal) // 100)
    progressBar = QProgressBar()
    progressBar.setRange(0, 10000)
    progressBar.setValue(0)
    
    timer = QTimer(win)
    timer.timeout.connect(barLoading)
    timer.start(1000)

    disableWidget.toggled.connect(group1.setDisabled)
    disableWidget.toggled.connect(group2.setDisabled)
    disableWidget.toggled.connect(group3.setDisabled)
    disableWidget.toggled.connect(group4.setDisabled)
    disableWidget.toggled.connect(progressBar.setDisabled)

    # ========== Core Of The Core ==========
    midLayout.addWidget(group1)
    midLayout.addWidget(group2)
    bottomLayout.addWidget(group4)
    bottomLayout.addWidget(group3)
    layouts.addLayout(topLayout)
    layouts.addLayout(midLayout)
    layouts.addLayout(bottomLayout)
    layouts.addWidget(progressBar)
    win.setLayout(layouts)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    window()
    win.setWindowTitle("Learning \"Almost\" All Widgets")
    win.setFixedWidth(600)
    win.show()
    sys.exit(app.exec_())