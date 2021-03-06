# -*- coding: utf-8 -*-
import sys
import images_qr
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from main import Query


class Example(QWidget):


    def __init__(self):
        self.TYPE = 1
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        # 设置全局字体大小
        self.setFont(QFont('微软雅黑', 10))

        # 顶部的水平布局label+labelEdit+button
        self.top = QHBoxLayout()
        label = QLabel('学号')
        self.input = QLineEdit()
        query = QPushButton('查询')
        query.clicked.connect(self.Query)
        self.top.addWidget(label)
        self.top.addWidget(self.input)
        self.top.addWidget(query)

        # 位于中间的布局选择查询类型
        typeselect = QHBoxLayout()
        self.rbtn_1 = QRadioButton('本学期成绩(推荐)')
        rbtn_2 = QRadioButton('历史全部成绩')
        # 默认选中
        self.rbtn_1.toggle()
        self.rbtn_1.toggled.connect(self.rbtnchange)
        typeselect.addWidget(self.rbtn_1)
        typeselect.addWidget(rbtn_2)

        # 底部的表格
        self.table = QTableWidget()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 全局垂直布局
        self.body = QVBoxLayout()
        self.body.addLayout(self.top)
        self.body.addLayout(typeselect)
        self.body.addWidget(self.table)

        #设置窗口的位置和宽高
        self.setLayout(self.body)
        self.center()
        self.resize(800, 600)

        #设置窗口标题
        self.setWindowTitle('GradeViewer')
        self.setWindowIcon(QIcon(':/dog.jpg'))
        self.show()
        QMessageBox.information(self, '提示', '请使用校园网查询(￣▽￣)~*')

    def Query(self):
        length = -1
        if self.TYPE == 2:
            reply = QMessageBox.question(self, '重要通知(｀Д´)', '历史查询请耐心等待20s以上!!!   ', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.No:
                reply = QMessageBox.information(self, '不守规则是吧', '我也是有脾气的好吧￣へ￣')
                QCoreApplication.instance().quit()
        result = Query(self.input.text(), type=self.TYPE)
        if result == 'ERROR':
            QMessageBox.warning(self, '警告', '出现了未知的错误，请检查输入或是否使用校园网')
            return
        # 判断数据长度，若大于0
        if len(result[0]) > 0:
            length =  len(result[0])
        elif len(result) == 0:
            QMessageBox.warning(self, '警告', '未查询到成绩哦~')
            return

        if length > 0:
            self.table.setRowCount(length)
            # 如果有数据，则根据类型决定列数
            if self.TYPE == 1:
                self.table.setColumnCount(2)
                self.table.setHorizontalHeaderLabels(['课程', '成绩'])
                self.table.setColumnWidth(0, 300)
                self.table.setColumnWidth(1, 200)
                for i in range(2):
                    for j in range(length):
                        self.table.setItem(j, i, QTableWidgetItem(result[i][j]))
            elif self.TYPE == 2:
                self.table.setColumnCount(3)
                self.table.setHorizontalHeaderLabels(['课程', '成绩', '学期'])
                self.table.setColumnWidth(0, 300)
                self.table.setColumnWidth(1, 200)
                self.table.setColumnWidth(2, 150)
                for i in range(3):
                    for j in range(length):
                        self.table.setItem(j, i, QTableWidgetItem(result[i][j]))


    def rbtnchange(self):
        if self.rbtn_1.isChecked():
            self.TYPE = 1
        else:
            self.TYPE = 2

    def center(self):
        # 得到主窗口的矩形框架qr
        qr = self.frameGeometry()
        # 我们调用这些方法来得到屏幕分辨率，并最终得到屏幕中间点的坐标cp
        cp = QDesktopWidget().availableGeometry().center()
        # 这里我们将矩形框架移至屏幕正中央，大小不变
        qr.moveCenter(cp)
        # 最后我们将应用窗口移至矩形框架的左上角点，这样应用窗口就位于屏幕的中央了【注意部件的move都是左上角移动到某点】
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '通知', '你确定要退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())