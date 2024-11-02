import sys
import cv2 as cv
import numpy as np
import winsound
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QFont

class Panorama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('파노라마 영상')
        self.setGeometry(200, 200, 700, 400)

        # UI 요소 설정
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.collectButton = QPushButton('영상 수집', self)
        self.collectButton.setIcon(QIcon('start_icon.png'))  # Add custom icon here
        self.showButton = QPushButton('영상 보기', self)
        self.stitchButton = QPushButton('합병', self)
        self.saveButton = QPushButton('저장', self)
        self.quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다!', self)

        # 버튼 스타일 적용 (가시성 개선)
        self.collectButton.setStyleSheet("background-color: #5CB85C; color: #FFFFFF; border-radius: 8px; padding: 10px; margin: 5px;")  # Green
        self.showButton.setStyleSheet("background-color: #5CB85C; color: #FFFFFF; border-radius: 8px; padding: 10px; margin: 5px;")
        self.stitchButton.setStyleSheet("background-color: #5CB85C; color: #FFFFFF; border-radius: 8px; padding: 10px; margin: 5px;")
        self.saveButton.setStyleSheet("background-color: #5BC0DE; color: #FFFFFF; border-radius: 8px; padding: 10px; margin: 5px;")  # Blue
        self.quitButton.setStyleSheet("background-color: #D9534F; color: #FFFFFF; border-radius: 8px; padding: 10px; margin: 5px;")  # Red

        # 버튼과 레이블을 레이아웃에 추가
        self.layout.addWidget(self.collectButton)
        self.layout.addWidget(self.showButton)
        self.layout.addWidget(self.stitchButton)
        self.layout.addWidget(self.saveButton)
        self.layout.addWidget(self.quitButton)
        self.layout.addWidget(self.label)

        # 버튼 초기 상태 비활성화
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)

        # 버튼 클릭 이벤트 연결
        self.collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)
        self.stitchButton.clicked.connect(self.stitchFunction)
        self.saveButton.clicked.connect(self.saveFunction)
        self.quitButton.clicked.connect(self.quitFunction)

    def collectFunction(self):
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.label.setText('C를 여러 번 눌러 수집하고 끝나면 Q를 눌러 비디오를 끕니다.')

        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not self.cap.isOpened():
            sys.exit('카메라 연결 실패')

        self.imgs = []
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            cv.imshow('video display', frame)
            key = cv.waitKey(1)
            if key == ord('c'):
                self.imgs.append(frame)
            elif key == ord('q'):
                self.cap.release()
                cv.destroyWindow('video display')
                break

        if len(self.imgs) >= 2:
            self.showButton.setEnabled(True)
            self.stitchButton.setEnabled(True)
            self.saveButton.setEnabled(True)

    def showFunction(self):
        self.label.setText(f'수집된 영상은 {len(self.imgs)}장입니다.')
        stack = cv.resize(self.imgs[0], dsize=(0, 0), fx=0.25, fy=0.25)
        for i in range(1, len(self.imgs)):
            stack = np.hstack((stack, cv.resize(self.imgs[i], dsize=(0, 0), fx=0.25, fy=0.25)))
        cv.imshow('Image collection', stack)

    def stitchFunction(self):
        stitcher = cv.Stitcher_create()
        status, self.img_stitched = stitcher.stitch(self.imgs)
        if status == cv.STITCHER_OK:
            cv.imshow('Image stitched panorama', self.img_stitched)
            self.label.setText('파노라마 합성이 성공적으로 완료되었습니다.')
        else:
            winsound.Beep(3000, 500)
            self.label.setText('파노라마 제작에 실패했습니다. 다시 시도하세요.')

    def saveFunction(self):
        fname, _ = QFileDialog.getSaveFileName(self, '파일 저장', './')
        if fname:
            if cv.imwrite(fname, self.img_stitched):
                self.label.setText(f'{fname}에 저장되었습니다.')
            else:
                QMessageBox.critical(self, '저장 오류', '파일 저장에 실패했습니다.')

    def quitFunction(self):
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        cv.destroyAllWindows()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Panorama()
    win.show()
    app.exec_() 
