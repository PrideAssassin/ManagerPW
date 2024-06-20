from PySide2.QtCore import QModelIndex
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import Qt, QAbstractItemModel
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
from PySide2.QtWidgets import QListWidgetItem, QMessageBox
import ui_login
import ui_search1
import ui_change1_PW
import sys
from functools import partial
import pickle



correct_key = None
encryption_path = None
iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
file_dict = {}          # 存放所有账号的字典


class login_MyWindow(QtWidgets.QMainWindow, ui_login.Ui_MainWindow):
    """
    ui组件对象列表：
        加密文件：lineEdit，主控密码：lineEdit_2，
        选择加密文件：pushButton，解密文件：pushButton_2，修改主控密码：pushButton_3
    """
    # -----------------------信号--------------
    close_signal = QtCore.Signal()

    def __init__(self, parent=None):
        super(login_MyWindow, self).__init__(parent)
        self.setupUi(self)

        # ------------------------信号--------------
        # 3个按钮的信号与槽连接：选择加密文件，解密文件，修改主控密码
        self.pushButton.clicked.connect(self.select_file)
        self.pushButton_2.clicked.connect(self.decode_file)
        # self.pushButton_3.clicked.connect(self.change_PW)

    def select_file(self):
        """
        功能：打开文件选择对话框，选择加密文件后在lineEdit组件中显示文件路径
        :return:
        """
        path1 = QtWidgets.QFileDialog.getOpenFileName()
        self.lineEdit.setText(path1[0])

    def decode_file(self):
        """
        功能：
            1. 点击解密按钮后，先判断用户是否输入了密码。(没有输入密码，直接退出程序。)
            2. 如果输入了用户了密码，再判断是否用户是否选择了加密文件。(没有选择加密文件，就新建一个加密文件，并使用输入的密码当作文件解密密码)。
            3. 如果用户选择了加密文件，并且输入了密码，则对密码进行验证，判断该密码能否正常解密文件。
        :return:
        """
        # 1. 判断是否输入了主控密码
        if self.lineEdit_2.text() == "":
            print("没有输入主控密码，直接退出程序")
        else:
            # 2 如果输入了主控密码，再判断是否选择了加密文件
            if self.lineEdit.text() == "":
                # print("没有选择加密文件(测试)")
                # 2.1 没有选择加密文件，则创建一个加密文件
                with open("测试99", mode="w+") as encryptedFile:
                    pass
                self.newKeyFile()
            else:
                # 3. 对加密文件进行密码验证并解密文件
                self.validatePW()

    def newKeyFile(self):
        """
        功能：对新文件的加密，并将key追加在文件
        :return:
        """
        # 1. 先获取密钥key
        self.key = self.newKey(self.getPW())

        # 2. 使用秘钥key初始化AES加密器
        global iv
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)

        # 3. 打开文件，读取文件内容，并使用密钥key进行加密
        with open("测试99", "rb+") as file1:
            # 填充数据      (使用AES加密内容，内容必需是16字节的倍数，所以需要填充)
            fo_fill = pad(self.key, AES.block_size)
            # 加密数据
            cipherFo = cipher.encrypt(fo_fill)
            # 加密完成后写入文件，使用with关键字，不用手动关闭文件对象了
            pickle.dump(cipherFo, file1)
            tip("由于没有选择加密文件，所以使用当前输入的密码，在当前路径创建一个新的加密文件：测试99")

    def validatePW(self):
        """
        功能：实现对文件的解密，并判断解密后的密码是否正确
        :return:
        """
        # 1. 先获取密钥key
        self.key = self.newKey(self.getPW())
        file_name = self.lineEdit.text()
        list_temp = []
        # 1. 取出文件内所有数据
        try:
            with open(file_name, "rb+") as file1:
                try:
                    while True:
                        load_data = pickle.load(file1)
                        list_temp.append(load_data)
                except Exception as e:
                    print("pickle取出了所有加密文件对象包", e)
            # 2. 使用秘钥key和iv初始化AES解密器
            global iv
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            # 3. 解密文件内容
            nn = cipher.decrypt(list_temp[0])
            # 4. 去除填充区  (如果文件没有正确解密，去除填充的时候会产生异常，所以出现异常直接报密码错误)
            XX = unpad(nn, AES.block_size)
            # 5. 获取解密后的密钥key
            PW = XX[-32:]
            # 6. 使用文件解密后的密钥key,对比主控密码的秘钥key。
            yanzheng1 = self.newKey(self.getPW())
            if PW == yanzheng1:
                # print("密码正确")
                # 将正确的秘钥key和当前加密文件的路径，传出去(使用全局变量)
                global correct_key
                global encryption_path
                correct_key = PW
                encryption_path = self.lineEdit.text()
                # 7. 密码正确，跳转到search窗口，并关闭当前窗口
                self.close_signal.emit()  # 发射关闭信号
                self.close()  # 关闭login 窗口
            else:
                # 8. 即使使用错误密码在去除填充后，没有出现异常，2个秘钥key不匹配就是密码错误
                # print("密码错误:密钥key不匹配")
                tip("密码错误")
        except Exception as e:
            # 代码直接过程中出现异常，说明密码错误
            # print("密码错误:去除填充区产生异常", e)
            tip("密码错误")



    def getPW(self):
        """
        功能：获取用户输入的主控密码(lineEdit_2)
        :return: 用户密码
        """
        password = self.lineEdit_2.text()
        return password

    @staticmethod
    def newKey(password):
        """
        功能：使用用户输入的PW生成一个AES加密用的密钥key
        :param password:  传入一个PW
        :return: 返回一个秘钥key
        """
        # 设置盐值salt
        salt = "zxc"

        # 使用PBKDF2派生出秘钥
        iterations = 3000
        key_length = 32
        key = PBKDF2(password, salt, dkLen=key_length, count=iterations, hmac_hash_module=SHA256)
        return key


class changePW_MyWindow(QtWidgets.QMainWindow, ui_change1_PW.Ui_Form):
    """
         ui组件对应对象：
             原文件密码：lineEdit，新密码：lineEdit_2，确认密码：lineEdit_3，确认：pushButton
         :param parent:
         """
    def __init__(self, parent=None):
        super(changePW_MyWindow, self).__init__(parent)
        self.setupUi(self)
        # --------------------信号----------------------
        self.pushButton.clicked.connect(self.confirm_change)

    def confirm_change(self):
        """
        功能：修改密码
        :return:
        """
        iterations = 3000
        key_length = 32
        salt = "zxc"
        # 1. 判断3个编辑框内容是否为空
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "":
            # print("密码不能为空")
            tip("密码不能为空")
            return

        # 2. 判断新密码和确认密码是否一致
        new_password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()
        password = self.lineEdit.text()
        if new_password == confirm_password:
            # 使用PBKDF2派生出秘钥
            key = PBKDF2(password, salt, dkLen=key_length, count=iterations, hmac_hash_module=SHA256)
            global correct_key
            # 3. 判断输入的原密码是否正确
            if correct_key == key:
                print("当前输入的密码正确")
                # 4. 获取新密码的key
                new_key = PBKDF2(new_password, salt, dkLen=key_length, count=iterations, hmac_hash_module=SHA256)
                correct_key = new_key
                try:
                    with open(encryption_path, "wb+") as file2:
                        cipher = AES.new(correct_key, AES.MODE_CBC, iv=iv)
                        fo_fill = pad(correct_key, AES.block_size)
                        cipherFo = cipher.encrypt(fo_fill)
                        pickle.dump(cipherFo, file2)
                        for key, value in file_dict.items():
                            temp_dict = {key: value}
                            xx = encryption_file(temp_dict)
                            pickle.dump(xx, file2)
                        tip("密码修改成功")
                except Exception as e:
                    print("加密文件打开失败", e)
            else:
                # print("输入的原文件密码错误")
                tip("输入的原文件密码错误")
        else:
            # print("新密码和确认密码不一致")
            tip("新密码和确认密码不一致")


class search1_MyWindow(QtWidgets.QMainWindow, ui_search1.Ui_MainWindow):
    """
    ui界面组件对应的对象：
        搜索：lineedit，信息：lineedit3，账号：lineedit2，密码：lineedit4，备注：textedit，列表记录 ：listview
        查看密码：PushButton2，快速查找：PushButton，确认：PushButton6，修改主控密码：pushButton_7
        修改记录：PushButton4，增加记录：PushButton3，删除记录：PushButton5
    """
    def __init__(self, parent=None):
        super(search1_MyWindow, self).__init__(parent)
        self.setupUi(self)
        # --------------------信号----------------------
        self.pushButton.clicked.connect(self.button_find)
        self.pushButton_2.clicked.connect(self.showPW)
        self.pushButton_3.clicked.connect(self.button_add)
        self.pushButton_4.clicked.connect(self.button_modify)
        self.pushButton_5.clicked.connect(self.del_item)
        self.listWidget.itemClicked.connect(self.item_clicked)
        self.pushButton_7.clicked.connect(self.changePW)

    def button_find(self):
        """
        获取当前搜索栏字符串，遍历列表元素，进行匹配
        :return:
        """
        search_str = self.lineEdit.text()
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            split_text = item.text().split(". ", 1)
            if search_str in split_text[1]:
                item.setHidden(False)
            else:
                item.setHidden(True)

    def showPW(self):
        current_mode = self.lineEdit_4.echoMode()
        if current_mode == QtWidgets.QLineEdit.EchoMode.Normal:
            self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        else:
            self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

    def button_add(self):
        """
        功能：响应增加记录按钮
            清空编辑框，并设置编辑框可编辑，并将确定按钮与增加记录按钮绑定
        :return:
        """
        self.lineEdit_3.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.textEdit.clear()
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.textEdit.setReadOnly(False)
        self.sin3 = self.pushButton_6.clicked.connect(self.confirm_add)

    def button_modify(self):
        """
        功能：响应修改记录按钮
            将编辑框3设置为只读模式，其余编辑框可编辑，并设置确定按钮与修改记录按钮绑定
        :return:
        """
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.textEdit.setReadOnly(False)
        self.sin4 = self.pushButton_6.clicked.connect(self.confirm_modify)

    def del_item(self):
        global file_dict
        global encryption_path
        global correct_key
        global iv
        current_item = self.listWidget.currentItem()
        if current_item:
            spilt_text = current_item.text().split(". ", 1)
            select_text = spilt_text[1]
            file_dict.pop(select_text)
        else:
            select_text = None
            return

        try:
            with open(encryption_path, "wb+") as file2:
                cipher = AES.new(correct_key, AES.MODE_CBC, iv=iv)
                fo_fill = pad(correct_key, AES.block_size)
                cipherFo = cipher.encrypt(fo_fill)
                pickle.dump(cipherFo, file2)
                for key, value in file_dict.items():
                    temp_dict = {key: value}
                    xx = encryption_file(temp_dict)
                    pickle.dump(xx, file2)
        except Exception as e:
            print("加密文件打开失败", e)
        file_dict = {}
        self.lineEdit_3.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.textEdit.clear()
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.textEdit.setReadOnly(True)
        self.read_all_PW()

    def confirm_add(self):
        """
        功能：确定增加记录
            1. 获取用户输入的用户名，密码，备注信息，获取用户输的账号标题信息,
            2. 将信息加入到一个临时字典中.
            3. 先判断该信息标题是否已经在字典中存在。不存在就将临时字典加密，并写入加密文件中。
            4. 将哪些编辑框设置为只读模式，并将哪些编辑框内容清空，断开确定按钮的所有槽函数
        :return:
        """
        # 1.
        account_info = {"username": self.lineEdit_2.text(), "password": self.lineEdit_4.text(),
                        "note": self.textEdit.toPlainText()}
        info = self.lineEdit_3.text()

        # 2.
        temp_dict = {info: account_info}

        # 3.
        temp_list1 = []
        for row in range(self.listWidget.count()):
            item = self.listWidget.item(row)
            split_text = item.text().split(". ", 1)
            temp_list1.append(split_text[1])

        if info in temp_list1:
            print(f"用户名： {info} 已存在。")
        else:
            global encryption_path
            xx = encryption_file(temp_dict)
            try:
                with open(encryption_path, "ab+") as file2:
                    pickle.dump(xx, file2)
                    file2.close()
            except Exception as e:
                print("加密文件打开失败", e)
        self.read_all_PW()

        # 4.
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.textEdit.setReadOnly(True)
        self.lineEdit_3.clear()
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.textEdit.clear()
        self.pushButton_6.clicked.disconnect()

    def confirm_modify(self):
        global file_dict
        global encryption_path
        global correct_key
        current_item = self.listWidget.currentItem()
        if current_item:
            spilt_text = current_item.text().split(". ", 1)
            select_text = spilt_text[1]
            file_dict.pop(select_text)
        else:
            select_text = None
            return
        account_info = {"username": self.lineEdit_2.text(), "password": self.lineEdit_4.text(),
                        "note": self.textEdit.toPlainText()}
        info = self.lineEdit_3.text()
        temp1_dict = {info: account_info}
        file_dict.update(temp1_dict)
        try:
            with open(encryption_path, "wb+") as file2:
                cipher = AES.new(correct_key, AES.MODE_CBC, iv=iv)
                fo_fill = pad(correct_key, AES.block_size)
                cipherFo = cipher.encrypt(fo_fill)
                pickle.dump(cipherFo, file2)
                for key, value in file_dict.items():
                    temp_dict = {key: value}
                    xx = encryption_file(temp_dict)
                    pickle.dump(xx, file2)
                print("重新写入全部文件")
        except Exception as e:
            print("加密文件打开失败", e)
        file_dict = {}
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.textEdit.setReadOnly(True)
        self.pushButton_6.clicked.disconnect()
        self.read_all_PW()

    def item_clicked(self):
        """
        获取listwidget组件当前选中的项,并将选中项在相关信息栏显示出来
        :return:
        """
        global file_dict
        current_item = self.listWidget.currentItem()
        if current_item:
            select_text = (current_item.text()).split(". ", 1)
            select_split_text = select_text[1]
        else:
            select_split_text = None
        if select_split_text:
            self.lineEdit_3.setText(select_split_text)
            self.lineEdit_2.setText(file_dict[select_split_text]["username"])
            self.lineEdit_4.setText(file_dict[select_split_text]["password"])
            self.textEdit.setText(file_dict[select_split_text]["note"])
        else:
            pass
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.textEdit.setReadOnly(True)

    @staticmethod
    def changePW(self):
        window3.show()

    def read_all_PW(self):
        global encryption_path
        global file_dict
        list_load_data = []  # 存放加密文件中取出的所有字典列表
        list_key = []
        # 打开文件，读取字典对象,并解密
        with open(encryption_path, "rb") as file3:
            count = 0
            while True:
                try:
                    if count == 0:
                        count += 1
                        pickle.load(file3)
                        continue
                    else:
                        load_data = pickle.load(file3)
                        list_load_data.append(load_data)
                        count += 1
                except Exception as e:
                    print("读取文件完成。(pickle读取文件结束，继续读取时触发异常)")
                    break
        # 将取出的字典对象，解密还原成字典，并用键值生成一个列表
        for x in list_load_data:
            temp_account_info = eval(decryption_file(x).decode())
            for key, value in temp_account_info.items():
                file_dict.update({key: value})
                list_key.append(key)

        self.refresh_listview(list_key)

    def refresh_listview(self, list_key):
        """
        1. 将列表中的账号信息显示在listView中
        :return:
        """
        self.listWidget.clear()
        for i, x in enumerate(list_key, start=1):
            item = QListWidgetItem(f"{i}. {x}")
            self.listWidget.addItem(item)


def encryption_file(data):
    """
    这个是适合对字符串数据进行加密。(因为有编码转换，对字节型加密有误，如果有需要可以自行修改这个函数
    主要是我懒得修改了，能代码跑就行反正自己用)
    :param data:
    :return:
    """
    global iv
    global correct_key
    # 1. 使用秘钥key和iv 初始化AES加密器
    cipher = AES.new(correct_key, AES.MODE_CBC, iv)
    # 2. 打开文件，读取文件内容，并使用密钥key进行加密
    # 填充数据
    data_bytes = str(data).encode()
    fo_fill = pad(data_bytes, AES.block_size)
    # 加密数据
    cipherFo = cipher.encrypt(fo_fill)
    # 加密完成后写入文件，使用with关键字，不用手动关闭文件对象了
    # 3. 返回加密的数据
    return cipherFo


def tip(text):
    """
    设置成全局，方便在所有地方直接调用。
    :param text:
    :return:
    """
    msg_box = QMessageBox()
    msg_box.setWindowTitle("提示")
    msg_box.setText(text)
    msg_box.exec_()

def decryption_file(data):
    global iv
    global correct_key
    # 1. 使用秘钥key和iv 初始化AES解密器
    cipher = AES.new(correct_key, AES.MODE_CBC, iv)
    # 2. 解密
    cipherFo = cipher.decrypt(data)
    # 3. 去除填充数据
    fill_data = unpad(cipherFo, AES.block_size)
    return fill_data


if __name__ == '__main__':
    # 创建应用程序对象
    app = QtWidgets.QApplication()
    # 创建窗口对象
    window1 = login_MyWindow()
    window2 = search1_MyWindow()
    window3 = changePW_MyWindow()
    # 运行窗口
    window1.show()
    # 连接信号与槽
    window1.close_signal.connect(window2.show)
    window1.close_signal.connect(window2.read_all_PW)
    # 运行应用程序
    sys.exit(app.exec_())
