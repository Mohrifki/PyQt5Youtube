import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Register Login Form")

# ------ Header ------
layouts = QVBoxLayout(win)
label = QLabel()
label.setText("Sign Up")
layouts.addWidget(label)

# ------ Return Result ------
result = {
    'name' : '',
    'nim' : '',
    'email' : '',
    'gender' : '',
    'fakultas' : '',
    'prodi' : ''
}

# ------ File Handling / Store / Save ------
f = open('data.csv', 'r')
database = []
for x in f:
    database.append(x.strip().split(',')[:6])
f.close()

# ---- Save
def save():
    f = open('data.csv', 'w')
    for item in database:
        for i in item:
            f.write(i+',')
        f.write('\n')
    f.close()

# ---- Store
def store(result):
    temp = []
    for key in result:
        temp.append(str(result[key]))
    database.append(temp)
    save()

# ------ Search ------
def alert(i):
    print(i)
    found = QMessageBox()
    found.setWindowTitle("Status")
    found.setIcon(QMessageBox.Information)
    found.setText("Found!")
    found.setInformativeText("Name : "+str(i[0])+"\nNIM : "+str(i[1])+"\nEmail : "+str(i[2])+"\nGender : "+str(i[3])+"\nFakultas : "+str(i[4])+"\nProdi : "+str(i[5]))
    found.exec_()
def search():
    text, result = QInputDialog.getText(win, 'Input Dialog', 'Cari berdasarkan NIM:')
    if result == True:
        for i in database:
            if i[1] == text:
                alert(i)
search_btn = QPushButton("Search?")
search_btn.clicked.connect(search)

# ------ On Submit ------
def on_submit():
    result['name'] = name.text()
    result['nim'] = nim.text()
    result['email'] = email.text()
    text = 'Successfull'
    isComplete = True
    for key in result:
        if result[key] == '':
            isComplete = False
            text = 'Field not correct or aren\'t filled'
    if isComplete == True:
        store(result)
    status = QMessageBox()
    status.setWindowTitle("Status")
    status.setIcon(QMessageBox.Information)
    status.setText(text)
    status.exec_()

submit = QPushButton("Submit")
submit.clicked.connect(on_submit)

# ------ Gender ------
def gender_onClick(id):
    result['gender'] = gender.button(id).text()
gender = QButtonGroup()
male = QRadioButton("Male")
fmale = QRadioButton("Female")
gender.addButton(male, 1)
gender.addButton(fmale, 2)
gender.buttonClicked[int].connect(gender_onClick)

# ------ Fakultas ------
def fakultas_onClick(id):
    result['fakultas'] = fakultas.button(id).text()
fakultas = QButtonGroup()
teknik = QRadioButton("Teknik")
lainnya = QRadioButton("Lainnya")
fakultas.addButton(teknik, 1)
fakultas.addButton(lainnya, 2)
fakultas.buttonClicked[int].connect(fakultas_onClick)

# ------ Prodi ------
def prodi_onClick(name):
    result['prodi'] = name
prodi = QComboBox()
prodi_option = [
    "Teknik Mesin",
    "Teknik Industri",
    "Teknik Elektro",
    "Teknik Mekatronika",
    "Teknik Informatika",
    "Sistem Informasi"
]
for i in prodi_option:
    prodi.addItem(i)
prodi.activated[str].connect(prodi_onClick)

# ------ Piece ------
name = QLineEdit()
name_regex = QRegExp('^[ A-Za-z]{1,20}$')
name_validate = QRegExpValidator(name_regex, name)
name.setValidator(name_validate)
nim = QLineEdit()
nim_regex = QRegExp('^[0-9]{12}$')
nim_validate = QRegExpValidator(nim_regex, nim)
nim.setValidator(nim_validate)
email = QLineEdit()
email_regex = QRegExp('^[a-zA-Z0-9_-\.]+@[a-zA-Z0-9_-\.]+\.[a-zA-Z]{2,4}$')
email_validate = QRegExpValidator(email_regex, email)
email.setValidator(email_validate)

# ------ FORM ------
form = QFormLayout()
form.addRow(QLabel("Nama"), name)
form.addRow(QLabel("NIM"), nim)
form.addRow(QLabel("Email"), email)
form.addRow(QLabel("Gender"))
form.addRow(male, fmale)
form.addRow(QLabel("Fakultas"))
form.addRow(teknik, lainnya)
form.addRow(QLabel("Prodi"))
form.addRow(prodi)
form.addRow(submit, search_btn)

layouts.addLayout(form)
win.show()
sys.exit(app.exec_())