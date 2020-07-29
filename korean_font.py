# 시각화  처리시 한글 폰트를 적용하는 모듈이다.
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rc
import matplotlib as mpl
# 파이썬이 운영되는 환경을 확인할 수 있다 => os를 구분
import platform


def initKoreaFont():
    print(platform.system())
    if platform.system() == 'Darwin':  # 맥
        plt.rc('font', family='AppleGothic')
    elif platform.system() == 'Windows':  # 윈도우
        # 맑은체
        path = 'C:/Windows/Fonts/malgun.ttf'
        font = fm.FontProperties(fname=path, size=10)
        plt.rc('font', family=font.get_name())

    else:  # Linux
        path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
        font = fm.FontProperties(fname=path, size=10)
        plt.rc('font', family=font.get_name())
        mpl.font_manager._rebuild()
