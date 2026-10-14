# 매장 공간을 만들려면 Qt가 가진 부품 중 'QMainWindow'를 빌려와야 한다.
# 도서관에서 필요한 책 한 권만 대출하듯이, PySide6.QtWidgets에서 딱 하나만 꺼내온다.
from PySide6.QtWidgets import QMainWindow

# class = 설계도면. 아직 매장 공간이 지어진 게 아니다.
# (QMainWindow) = 기본 매장 설계도를 물려받아서 "설계도에 우리 인테리어 디자인을 더한다"라는 뜻이다.
class MainWindow(QMainWindow):

    # __init__ = 매장이 처음 지어질 때 딱 한 번 실행되는 '오픈 준비 체크리스트'.
    # self = "지금 짓고 있는 매장 자신"을 가리킨다
    def __init__(self):
        # super().__init__() = 물려받은 기본 매장 설계도의 기본 공사부터 먼저 해달라는 뜻.
        # 빼먹으면 뼈대 없이 인테리어부터 하는 꼴이라 에러가 난다
        super().__init__()

        # 가게 간판 달기. 창 맨 위 제목줄 글자.
        self.setWindowTitle("Mutting Room")

        # 매장(창) 크기 정하기. (가로 900칸, 세로 600칸) 단위 = px
        self.resize(900, 600)
