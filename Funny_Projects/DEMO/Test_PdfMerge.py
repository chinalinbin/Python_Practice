# -*- coding:utf-8 -*-

'''
使用pypdf2库，实现对PDF文档的合并功能
'''

import PyPDF2
import os


# 建立一个装PDF文件的数组
pdfFiles = [1,2]

# 遍历该目录下的文件
for filename in os.listdir("."):
    # 找到pdf结尾的文件
    if filename.endswith(".pdf"):
        # 将pdf文件写入pdfFiles内
        pdfFiles.append(filename)

# 排序
pdfFiles.sort()

# 生产一个空白的pdf文档
pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfReader = PyPDF2.PdfFileReader(open(filename,"rb"))

    # 以读取方式依次打开pdf文件
    for pageNum in range(pdfReader.numPages):
        # 将打开的pdf文件内容一页一页复制到新建的空白pdf里面
        pdfWriter.addPage(pdfReader.getPage(pageNum))

# 生成combine.pdf文件
pdfOutput = open("combine.pdf","wb")
# 将复制 的内容全部写入
pdfWriter.write(pdfOutput)
pdfOutput.close()





