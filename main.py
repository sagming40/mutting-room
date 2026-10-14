# sys = Python 자신과 OS 사이의 '안내 데스크'.
# 프로그램 종료 시 "정상 종료" 확인용
import sys

# 건물 + 영업 허가(QApplication)를 Qt 창고에서 가져온다.
from PySide6.QtWidgets import QApplication

# 매장 설계도(MainWindow)를 가져온다.
# mutting_room.ui.main_window = "mutting_room 건물 > ui 층 > main_window 호실"이라는 주소.
from mutting_room.ui.main_window import MainWindow


# main() = 가게 여는 순서를 한 묶음으로 적어둔 '오픈 매뉴얼'.
def main():
    # 1. 건물 짓기 + 영업 허가 받기. 프로그램 전체에서 딱 1개만 만든다.
    # sys.argv = 프로그램을 실행할 때 딸려온 부가 정보 (관례)
    app = QApplication(sys.argv)

    # 2. 실제로 설계도(MainWindow)대로 매장을 짓는다.
    # 아직까지 눈에는 직접 보이지 않는다.
    window = MainWindow()

    # 3. 매장의 전원을 켜서 손님한테 보이게 한다.
    # 이 줄이 없으면 매장을 지어놓고 문을 열지 않은 꼴이다.
    window.show()

    # 4. 직원이 문 앞에 서서 손님(클릭, 키보드, X 버튼)을 기다리기 시작한다.
    # 창을 닫으면 직원이 퇴근하면서 종료 코드를 돌려주고,
    # sys.exit()가 종료 코드를 받아서 "정상 종료" 보고.
    sys.exit(app.exec())


# 이 파일을 '직접 실행'했을 때만 main()을 호출하는 안전장치.
# 이유: 다른 파일이 이 파일을 빌려갈 때는 가게가 멋대로 열리면 안 되기 때문이다.
# __name__ 양옆 언더스코어 각각 2개
if __name__ == "__main__":
    main()
