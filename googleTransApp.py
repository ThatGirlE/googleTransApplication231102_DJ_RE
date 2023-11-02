import sys

from PyQt5 import uic  # Qt Designer에서 제작한 ui를 불러와주는 클래스from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import googletrans


form_class =  uic.loadUiType("ui/googleUi.ui")[0]  # 인덱스 0으로 / Qt Designer에서 제작한 ui 불러오기

class MyGoogleTrans(QMainWindow, form_class):
    def __init__(self): # 초기화자
        super().__init__() # 부모 클래스의 초기화자 호출
        self.setupUi(self) # 제작해 놓은 googleUi.ui를 연결
        self.setWindowTitle("구글 번역기") # 번역기 앱의 타이틀
        self.setWindowIcon(QIcon("icon/google.png"))  #번역기 앱의 아이콘
        self.statusBar().showMessage("Google Trans App v1.0") # 상태 표시줄

        self.btn_trans.clicked.connect(self.trans_function)  # signal
        self.btn_reset.clicked.connect(self.reset_clear)


    def trans_function(self):   # slot
        trans_kor = self.input_kor_text.text() # input_kor_text 에 입력된 한글을 가져옴

        trans = googletrans.Translator() # 구글트랜스 모듈의 객체(번역해주는 객체)
        trans_eng = trans.translate(trans_kor, dest="en")
        trans_jpn = trans.translate(trans_kor, dest="ja")
        trans_chn = trans.translate(trans_kor, dest="zh-cn")

        self.output_eng_text.append(trans_eng.text) # text로 바꿔서
        self.output_jpn_text.append(trans_jpn.text)
        self.output_chn_text.append(trans_chn.text)

    def reset_clear(self):
        self.input_kor_text.clear()
        self.output_eng_text.clear()
        self.output_jpn_text.clear()
        self.output_chn_text.clear()


if __name__ == '__main__':  # 자동실행 방지
    app = QApplication(sys.argv)
    myApp = MyGoogleTrans()
    myApp.show()
    sys.exit(app.exec_()) # 멈춤






