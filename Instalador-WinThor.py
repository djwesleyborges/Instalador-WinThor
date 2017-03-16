# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
import socket
import subprocess
from os import mkdir
from sys import stderr
import webbrowser
import cx_Oracle
import shutil
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QWidget

import meumodulo

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 572)
        Form.setMinimumSize(QtCore.QSize(400, 572))
        Form.setMaximumSize(QtCore.QSize(400, 572))
        self.lbl_titulo = QtGui.QLabel(Form)
        self.lbl_titulo.setGeometry(QtCore.QRect(110, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setObjectName(_fromUtf8("lbl_titulo"))
        # Label Instancia do Oracle
        self.lbl_instOracle = QtGui.QLabel(Form)
        self.lbl_instOracle.setGeometry(QtCore.QRect(10, 60, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_instOracle.setFont(font)
        self.lbl_instOracle.setObjectName(_fromUtf8("lbl_instOracle"))
        # LineEdit Instancia do Oracle
        self.lineEdit_instOracle = QtGui.QLineEdit(Form)
        self.lineEdit_instOracle.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.lineEdit_instOracle.setObjectName(_fromUtf8("lineEdit_instOracle"))
        # Label ADM do Oracle
        self.lbl_adminInst = QtGui.QLabel(Form)
        self.lbl_adminInst.setGeometry(QtCore.QRect(10, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_adminInst.setFont(font)
        self.lbl_adminInst.setObjectName(_fromUtf8("lbl_adminInst"))
        # LineEdit ADM do Oracle
        self.lineEdit_adminInst = QtGui.QLineEdit(Form)
        self.lineEdit_adminInst.setGeometry(QtCore.QRect(150, 110, 113, 20))
        self.lineEdit_adminInst.setObjectName(_fromUtf8("lineEdit_adminInst"))
        # LineEdit Senha do Oracle
        self.lineEdit_passOracle = QtGui.QLineEdit(Form)
        self.lineEdit_passOracle.setGeometry(QtCore.QRect(150, 150, 113, 20))
        self.lineEdit_passOracle.setObjectName(_fromUtf8("lineEdit_passOracle"))
        # Label Senha do Oracle
        self.lbl_passOracle = QtGui.QLabel(Form)
        self.lbl_passOracle.setGeometry(QtCore.QRect(10, 140, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_passOracle.setFont(font)
        self.lbl_passOracle.setObjectName(_fromUtf8("lbl_passOracle"))
        # Label Criando Usuario do Oracle
        self.lbl_userComum = QtGui.QLabel(Form)
        self.lbl_userComum.setGeometry(QtCore.QRect(10, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_userComum.setFont(font)
        self.lbl_userComum.setObjectName(_fromUtf8("lbl_userComum"))
        # LineEdit Criando Usuario do Oracle
        self.lineEdit_userComum = QtGui.QLineEdit(Form)
        self.lineEdit_userComum.setGeometry(QtCore.QRect(150, 190, 113, 20))
        self.lineEdit_userComum.setObjectName(_fromUtf8("lineEdit_userComum"))
        # LineEdit Criando Senha do Usuario do Oracle
        self.lineEdit_passComum = QtGui.QLineEdit(Form)
        self.lineEdit_passComum.setGeometry(QtCore.QRect(150, 230, 113, 20))
        self.lineEdit_passComum.setObjectName(_fromUtf8("lineEdit_passComum"))
        self.lbl_passComum = QtGui.QLabel(Form)
        self.lbl_passComum.setGeometry(QtCore.QRect(10, 220, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        # Label Criando Senha do Usuario do Oracle
        self.lbl_passComum.setFont(font)
        self.lbl_passComum.setObjectName(_fromUtf8("lbl_passComum"))
        self.lbl_passDMP = QtGui.QLabel(Form)
        self.lbl_passDMP.setGeometry(QtCore.QRect(10, 260, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_passDMP.setFont(font)
        self.lbl_passDMP.setObjectName(_fromUtf8("lbl_passDMP"))
        # LineEdit Criando Senha do Usuario do Oracle
        self.lineEdit_passDMP = QtGui.QLineEdit(Form)
        self.lineEdit_passDMP.setGeometry(QtCore.QRect(150, 270, 113, 20))
        self.lineEdit_passDMP.setObjectName(_fromUtf8("lineEdit_passDMP"))
        # Label Diretorio do DMP
        self.lbl_dirDMP = QtGui.QLabel(Form)
        self.lbl_dirDMP.setGeometry(QtCore.QRect(10, 300, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_dirDMP.setFont(font)
        self.lbl_dirDMP.setObjectName(_fromUtf8("lbl_dirDMP"))
        # LineEdit Diretorio do DMP
        self.lineEdit_dirDMP = QtGui.QLineEdit(Form)
        self.lineEdit_dirDMP.setGeometry(QtCore.QRect(150, 310, 113, 20))
        self.lineEdit_dirDMP.setObjectName(_fromUtf8("lineEdit_dirDMP"))
        # Label Diretorio do WinThor
        self.lbl_dirWinThor = QtGui.QLabel(Form)
        self.lbl_dirWinThor.setGeometry(QtCore.QRect(10, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_dirWinThor.setFont(font)
        self.lbl_dirWinThor.setObjectName(_fromUtf8("lbl_dirWinThor"))
        # LineEdit Diretorio do WinThor
        self.lineEdit_dirWinThor = QtGui.QLineEdit(Form)
        self.lineEdit_dirWinThor.setGeometry(QtCore.QRect(150, 350, 113, 20))
        self.lineEdit_dirWinThor.setObjectName(_fromUtf8("lineEdit_dirWinThor"))
        # Botão Importar Base
        self.btn_impBase = QtGui.QPushButton(Form)
        self.btn_impBase.setGeometry(QtCore.QRect(10, 380, 81, 31))
        self.btn_impBase.setObjectName(_fromUtf8("btn_impBase"))
        self.btn_impBase.clicked.connect(self.recolheform)
        # Botão ID Banco
        self.btn_idBanco = QtGui.QPushButton(Form)
        self.btn_idBanco.setGeometry(QtCore.QRect(10, 420, 81, 31))
        self.btn_idBanco.setObjectName(_fromUtf8("btn_idBanco"))
        self.btn_idBanco.clicked.connect(self.selectIdBanco)
        # LineEdit ID_Banco
        self.lineEdit_idBanco = QtGui.QLineEdit(Form)
        self.lineEdit_idBanco.setGeometry(QtCore.QRect(100, 430, 113, 20))
        self.lineEdit_idBanco.setObjectName(_fromUtf8("lineEdit_idBanco"))

        ############  Label Ajustar CodCli   ############
        self.lineEdit_ajustCodCli = QtGui.QLineEdit(Form)
        self.lineEdit_ajustCodCli.setGeometry(QtCore.QRect(100, 480, 113, 20))
        self.lineEdit_ajustCodCli.setObjectName(_fromUtf8("lineEdit_ajustCodCli"))
        # Botão Autenticar WinThor
        self.btn_autWinThor = QtGui.QPushButton(Form)
        self.btn_autWinThor.setGeometry(QtCore.QRect(10, 530, 101, 31))
        self.btn_autWinThor.setObjectName(_fromUtf8("btn_autWinThor"))
        self.btn_autWinThor.clicked.connect(self.autenticador)
        # Botão Ajustar CodCli
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 470, 81, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.ajustarCodcli)
        # Label nome do Autor do Codigo
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 550, 211, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Instalação do WinThor", None))
        self.lbl_titulo.setText(_translate("Form", "Instalação WinThor", None))
        self.lbl_instOracle.setText(_translate("Form", "Instancia Oracle:", None))
        self.lbl_adminInst.setText(_translate("Form", "Admin da Instancia:", None))
        self.lbl_passOracle.setText(_translate("Form", "Senha do Oracle:", None))
        self.lbl_userComum.setText(_translate("Form", "Usuario a ser Criado:", None))
        self.lbl_passComum.setText(_translate("Form", "Senha a ser Criada:", None))
        self.lbl_passDMP.setText(_translate("Form", "Senha do DMP:", None))
        self.lbl_dirDMP.setText(_translate("Form", "Diretorio do DMP:", None))
        self.lbl_dirWinThor.setText(_translate("Form", "Diretorio do WinThor:", None))
        self.btn_impBase.setText(_translate("Form", "Importar Base", None))
        self.btn_idBanco.setText(_translate("Form", "ID do Banco", None))
        self.btn_autWinThor.setText(_translate("Form", "Autenticar WinThor", None))
        self.pushButton.setText(_translate("Form", "Ajustar CodCli", None))
        self.label.setText(_translate("Form", "Wesley Borges - Analista de Infraestrutura", None))


    def autenticador(self):
        verifica_autenticador = os.path.exists('C:\pcsist')
        if verifica_autenticador:
            print "Autenticador ja esta instalado.\nAbrindo o Autenticador,aguarde um momento."
            webbrowser.open('http://localhost:8888/autenticador/')

        else:
             os.system('C:\\InstallWinthor\\setup-nfe-1.2.3-auth-2.9.5.exe')
             webbrowser.open('http://localhost:8888/autenticador/')

   # Recolhe dados do Formulario e inicia o processo de importacao de base.
    def recolheform(self):

        modulo = getModulo()

        if dadosValidos(modulo):
           geraArquivosImportacao(modulo)

    def selectIdBanco(self): # Retorna ID do banco em EditText

        modulo = getModulo()

        connection = cx_Oracle.connect(str(modulo.usuarioASerCriado) + '/' + str(modulo.senhaASerCriada) + '@' + str(modulo.hostname) + '/' + str(modulo.instancia))
        cur = connection.cursor()
        cur.execute(
            "SELECT ((BASE.DBID + USUARIO.USER_ID) * 3) IDENTIFICADOR FROM V$DATABASE BASE,PCCONSUM,(SELECT USERNAME, USER_ID FROM ALL_USERS) USUARIO WHERE UPPER(USUARIO.USERNAME) = '%s'" % str(modulo.instancia).upper())
        for result in cur:
            t = str(result[0])
            self.lineEdit_idBanco.setText(t) # --> Retorna o ID na Edit Box
        cur.close()
        connection.close()


    def ajustarCodcli(self):
        modulo = getModulo()

        connection = cx_Oracle.connect(str(modulo.usuarioASerCriado) + '/' + str(modulo.senhaASerCriada) + '@' + str(modulo.hostname) + '/' + str(modulo.instancia))
        cursor = connection.cursor()
        sql1 = "UPDATE PCCONSUM SET CODCLIPC= : 1"
        sql2 = "UPDATE PCPARAMFILIAL SET VALOR= :2 WHERE NOME='CODCLIPC'"
        cursor.execute(sql1, (str(modulo.ajustarCodcli),))
        cursor.execute(sql2, (str(modulo.ajustarCodcli),))
        connection.commit()
        cursor.close()
        connection.close()

        ja = QWidget()
        QMessageBox.information(ja, "Aviso", "CodCliPC ajustado com sucesso!")




def getModulo(): # Esta função recebe tudo que e digitado no formulario
    modulo = meumodulo.Modulo()
    modulo.instancia = ui.lineEdit_instOracle.text()
    modulo.adminInstancia = ui.lineEdit_adminInst.text()
    modulo.senhaOracle = ui.lineEdit_passOracle.text()
    modulo.usuarioASerCriado = ui.lineEdit_userComum.text()
    modulo.senhaASerCriada = ui.lineEdit_passComum.text()
    modulo.senhaDMP = ui.lineEdit_passDMP.text()
    modulo.diretorioDMP = ui.lineEdit_dirDMP.text()
    modulo.diretorioWinthor = ui.lineEdit_dirWinThor.text()
    modulo.ajustarCodcli = ui.lineEdit_ajustCodCli.text()

    return modulo


def dadosValidos(modulo): # Valida se todas caixas estão preenchidas

    w = QWidget()

    if (modulo.hostname) in open("C:\\oracle\\product\\10.2.0\\db_1\\network\ADMIN\\tnsnames.ora").read():
        QMessageBox.information(w, "Aviso", "Iniciando processo de importacao de base.")
    else:
        QMessageBox.critical(w, "Aviso", "Favor corigir o nome do computador nos arquivos, tnsnames.ora e listener.ora")
        return False

    if modulo.instancia == '':
        QMessageBox.warning(w, "Aviso", "Favor informe a instancia")
        return False

    if modulo.adminInstancia == '':
        QMessageBox.warning(w, "Aviso", "Favor informe o administrador da instancia")
        return False

    if modulo.senhaOracle == '':
        QMessageBox.warning(w, "Aviso", "Favor informe a senha oracle")
        return False

    if modulo.usuarioASerCriado == '':
        QMessageBox.warning(w, "Aviso", "Favor informe o usuario")
        return False

    if modulo.senhaASerCriada == '':
        QMessageBox.warning(w, "Aviso", "Favor informe a senha")
        return False

    if modulo.senhaDMP == '':
        QMessageBox.warning(w, "Aviso", "Favor informe a senha DMP")
        return False

    if modulo.diretorioDMP == '':
        QMessageBox.warning(w, "Aviso", "Favor informe o diretorio DMP")
        return False

    if modulo.diretorioWinthor == '':
        QMessageBox.warning(w, "Aviso", "Favor informe o diretorio Winthor")
        return False

    return True

def geraArquivosImportacao(modulo):

    verifica_BDE = os.path.exists('C:\\WinThor\\Prod')
    if verifica_BDE == True:
        print 'Ok!'
    else:
        os.system('C:\\InstallWinthor\\WinThorInstall.exe')

    os.path.abspath('C:\\inswinthor\\atbd.sql')

    verifica_Ins = os.listdir('C:\\oracle\\product\\10.2.0\\oradata')  # Lista o conteudo do diretorio e salva em uma lista
    nome_Ins = " ".join(verifica_Ins)  # converte a lista para string

    verifica_TS_DADOS = os.path.exists('C:\\oracle\\product\\10.2.0\\oradata\\local\\TS_DADOS.ORA')
    verifica_TS_INDICE = os.path.exists('C:\\oracle\\product\\10.2.0\\oradata\\local\\TS_INDICE.ORA')

    verifica_Pasta = os.path.exists('C:\\inswinthor')

    if verifica_Pasta == True:
        os.chdir('C:\\inswinthor')
        os.unlink('impBase.bat')
        os.unlink('atbd.sql')
        os.unlink('atdw.sql')
        os.chdir(os.pardir)
        os.rmdir('C:\\inswinthor')

    else:
        mkdir("C:\\inswinthor")


        impBase = open("C:\\inswinthor\\impBase.bat", "w")
        impBase.write("@echo off\nsqlplus" + " " + modulo.adminInstancia + "/" +
                        modulo.senhaOracle + "@" +
                        modulo.instancia + " " +
                        "@C:\\inswinthor\\atbd.sql\nimp" + " " +
                        modulo.adminInstancia + "/" +
                        modulo.senhaOracle + "@" +
                        modulo.instancia + " " +
                        "fromuser=" + modulo.senhaDMP +
                        " " + "touser=" + modulo.usuarioASerCriado +
                        " " + "file=" + modulo.diretorioDMP +
                        "\nsqlplus" + " " + modulo.usuarioASerCriado +
                        "/" + modulo.senhaASerCriada + "@" + modulo.instancia + " " + "@C:\\inswinthor\\atdw.sql\nexit")
        impBase.close()

        arq = open("C:\\inswinthor\\atbd.sql", "w")
        arq.write(
                "Drop user " + "" + modulo.usuarioASerCriado + ""
                + " cascade;\nCreate user " + ""
                + modulo.usuarioASerCriado + "" + " identified by " + ""
                + modulo.usuarioASerCriado + "" + " default tablespace ts_dados;\nGrant connect, resource to "
                + "" + modulo.usuarioASerCriado + "" + ";\nalter user "
                + "" + modulo.usuarioASerCriado + "" + " quota unlimited on ts_dados;\nalter user " + ""
                + modulo.usuarioASerCriado + "" + " quota unlimited on ts_indice;\nalter user " + ""
                + modulo.usuarioASerCriado + "" + " quota 0m on system;\ngrant debug connect session to "
                + "" + modulo.usuarioASerCriado + "" + ";\ngrant create view to " + "" + modulo.usuarioASerCriado + "" +
                ";\ngrant dba to " + "" + modulo.usuarioASerCriado + "" + ";\ncommit;\nquit;")
        arq.close()

        arq1 = open("C:\\inswinthor\\atdw.sql", "w")
        arq1.write(
                "update pcconsum set dirwinthor = '" + modulo.diretorioWinthor +
                "';\ncommit;\nupdate pcparamfilial set valor ='" +
                modulo.diretorioWinthor + "' where nome = 'CON_CAMINHODIR';\ncommit\nupdate pcparamfilial set valor ='" +
                modulo.diretorioWinthor + "' where nome  ='CON_DIRWINTHOR';\ncommit;\nquit;")
        arq1.close()

        os.system('C:\inswinthor\impBase.bat')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())