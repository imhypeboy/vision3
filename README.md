📖 프로젝트 개요
dist폴더- main.exe 파일 다운하여 실행하면됩니다. 
 OpenCV와 PyQt5를 사용하여 실시간 비디오 수집 및 파노라마 이미지를 합성하는 애플리케이션입니다. 
 사용자는 카메라를 통해 이미지를 수집하고, 이를 기반으로 파노라마 이미지를 생성하며, 시인성 좋고 직관적인 UI를 통해 쉽게 사용할 수 있습니다.

🚀 주요 기능
📸 영상 수집: 실시간 카메라 피드를 통해 여러 장의 이미지를 수집합니다. 'c' 키를 눌러 이미지를 추가로 수집할 수 있습니다.
🔍 영상 보기: 수집된 이미지를 축소된 형태로 미리보기로 확인할 수 있습니다.
🖼️ 파노라마 합성: 수집된 이미지를 기반으로 파노라마 이미지를 자동으로 생성합니다.
💾 이미지 저장: 합성된 파노라마 이미지를 PNG 또는 JPG 형식으로 로컬 디렉토리에 저장할 수 있습니다.
🚪 프로그램 종료: '나가기' 버튼을 통해 애플리케이션을 안전하게 종료할 수 있습니다.
🛠️ 개발 환경
Python 버전: 3.8
라이브러리:
PyQt5
OpenCV (opencv-python, opencv-contrib-python)
NumPy
운영 체제: Windows 10 이상
📦 설치 방법

# 가상환경 생성 및 활성화
conda create -n vision_agent_project_env python=3.8
conda activate vision_agent_project_env

# 필수 라이브러리 설치
pip install pyqt5 opencv-python opencv-contrib-python numpy
💻 실행 방법
프로그램을 실행하려면 아래 명령어를 입력하세요:


python main.py
⚠️ 주의사항
카메라 연결: 프로그램 사용 시 카메라가 정상적으로 연결되어 있어야 합니다.
이미지 품질: 이미지 수집 시 프레임의 일관성을 유지하고, 카메라 움직임을 최소화하면 더 정확한 파노라마 이미지를 얻을 수 있습니다.
저장 시 오류: 저장할 파일의 확장자를 .png 또는 .jpg로 지정해야 오류가 발생하지 않습니다.
📝 추가 정보
이 프로그램은 Windows 환경에서 테스트되었습니다.
다른 운영 체제에서 실행할 경우, 호환성 문제가 발생할 수 있습니다.
PyInstaller를 사용하여 .exe 파일로 패키징할 수 있으며, 별도의 Python 설치 없이도 실행할 수 있습니다.

# .exe 파일 생성
pyinstaller --onefile --windowed --icon=app_icon.ico main.py
