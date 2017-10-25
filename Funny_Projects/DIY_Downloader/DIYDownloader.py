# -*- coding:utf-8 -*-


import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QInputDialog, QApplication

def download(dir, filename, url):
    """
      用于下载图片、视频、github项目等文件
      :param dir: 更改当前工作目录
      :param filename: 待下载的文件名
      :param url: 待下载的资源地址
      """
    if 'https://github.com' in url:
        import os
        os.chdir(dir)
        command = 'git clone {project}'.format(project=url)
        os.system(command)
    else:
        import requests
        import os
        data = requests.get(url).content
        os.chdir(dir)  # 文件保存路径
        with open(filename, 'wb') as f:
            f.write(data)
    print('下载完成！')



class Downloader(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        生成我们熟悉的台式机上的软件，通过点击按钮执行下载任务
        :return: 
        """

        # QToolTip.setFont(QFont('SansSerif', 10))
        # 输入url的文本框
        self.urlbox = QLineEdit(self)
        self.urlbox.setText("请输入url")
        #当文本框数据变化会执行connect联系的函数urlChanged
        self.urlbox.textChanged[str].connect(self.urlChanged)
        self.urlbox.resize(300,20)
        self.urlbox.move(50,20)

        #输入保存数据的路径
        self.dirbox = QLineEdit(self)
        self.dirbox.setText("请输入保存的文件夹路径")
        #当文本框数据变化会执行connect联系的函数dirChanged
        self.dirbox.textChanged[str].connect(self.dirChanged)
        self.dirbox.resize(300,20)
        self.dirbox.move(50,50)

        #输入保存时的文件名
        self.filenamebox = QLineEdit(self)
        self.filenamebox.setText("请输入文件名")
        #当文本框数据变化会执行connect联系的函数filenameChanged
        self.filenamebox.textChanged[str].connect(self.filenameChanged)
        self.filenamebox.resize(300,20)
        self.filenamebox.move(50,80)

        #点击按钮，执行下载任务
        self.btn = QPushButton("确定", self)
        self.btn.resize(300,20)
        self.btn.move(50,110)
        #按钮状态改变时候，会执行connect联系的函数onClick
        self.btn.clicked.connect(self.onClick)

        #设置窗体的大小和在屏幕中的位置
        self.setGeometry(400,400,400,200)
        self.setWindowTitle("简易下载器")
        self.show()

    def urlChanged(self, text):
        sender = self.sender()
        self.url = sender.text()

    def dirChanged(self, text):
        sender = self.sender()
        self.dir = sender.text()

    def filenameChanged(self, text):
        sender = self.sender()
        self.filename = sender.text()

    def onClick(self):
        sender = self.sender()
        if sender.text() and self.filename and self.url and self.dir:
            download(dir = self.dir, filename = self.filename, url = self.url)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dl = Downloader()
    sys.exit(app.exec_())
