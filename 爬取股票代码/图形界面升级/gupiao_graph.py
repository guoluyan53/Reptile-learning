import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
import gupiao
import requests
import time
from bs4 import BeautifulSoup
import pyqtgraph as pg




headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS"}
#存放所有数据的列表
listx = []
arr = []
arrx = []
arry = []
def get_message(text, page):
    soup = BeautifulSoup(text, 'lxml')
    if soup.tbody.string !=None:
        return 0
    else:
        for each in soup.tbody.find_all('tr'):
            th = each.select('th')
            td = each.select('td')
            listline = [th[0].string, td[0].string, td[1].string, td[2].string, td[3].string, th[1].contents[0].string]
            listx.append(listline)
        #初始化表格的行和列
        ui.tableWidget.setColumnCount(6)
        ui.tableWidget.setRowCount(len(listx))
        line = 0
        # 遍历每行的元素并写入
        for i in listx:
            for j in range(6):
            # print(list[i])
                ui.tableWidget.setItem(line, j, QTableWidgetItem(i[j]))
            line+=1

def compute(listx):
    summ = 0.0
    for i in listx:
        arr.append(i[1])
    # 画图的横坐标数组
    for k in listx:
        arrx.append(k[0])
    #画图的纵坐标数组
    for n in arr:
        arry.append(eval(n))

    for j in arr:
        summ += eval(j)  #数组里的每个元素都是str类型了，所以要转为数字类型

    avg = summ/len(arr)
    ui.textBrowser.setText(max(arr))
    ui.textBrowser_2.setText(min(arr))
    ui.textBrowser_3.setText(str(avg))
    # print(arrx)
    # print(len(arrx))
    # print(arry)
    # print(len(arry))
    # print(type(max(arr)))
    # print(min(arr))
    # print(avg)


def gethtml(gupiao,date,page):
    url = 'https://market.finance.sina.com.cn/transHis.php?symbol=' + gupiao + '&date=' + date + '&page=' + str(page)
    print(url)
    try:
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        flag = get_message(r.text, page)
        if flag == 0:
            return 0
    except Exception as result:
        print("错误原因：", result)
        return 0

def graph(x, y):
    xdict = dict(enumerate(x))
    win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
    win.resize(600, 400)
    stringaxis = pg.AxisItem(orientation='bottom')
    stringaxis.setTicks([xdict.items()])
    # win.setWindowTitle('pyqtgraph example: Plotting')
    # Enable antialiasing for prettier plots
    p1 = win.addPlot(axisItems={'bottom': stringaxis})
    p1.plot(list(xdict.keys()), y)
    pg.setConfigOptions(antialias=True)
    pg.show()


def mainexe():
    # gupiao = input("请输入你想要查询的股票（例如sz000001）：")
    # date = input("请输入你想要查询的日期（格式为2021-04-27）：")
    gupiao= ui.lineEdit.text()
    date = ui.lineEdit_2.text()
    for i in range(1, 1000):
        # 返回如果是0则说明爬取错误或者到达尾页，要跳出循环
        flag = gethtml(gupiao, date, i)
        # 间隔2s爬取
        time.sleep(2)
        if flag == 0:
            break
    #计算股票单价平均值最大值最小值
    compute(listx)
    graph(arrx,arry)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gupiao.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(mainexe)
    pg.exec()
    sys.exit(app.exec_())

