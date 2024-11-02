# README.md

## 프로젝트 개요
이 프로젝트는 OpenCV와 PyQt5를 사용하여 실시간 비디오 수집 및 파노라마 이미지를 합성하는 애플리케이션입니다. 사용자는 카메라를 통해 이미지를 수집하고, 수집한 이미지를 합성하여 파노라마 이미지를 만들고 저장할 수 있습니다. 이 프로그램은 직관적인 UI를 통해 쉽게 사용할 수 있으며, 프로그램 종료는 '나가기' 버튼을 통해 이루어집니다.

## 주요 기능
- **영상 수집**: 실시간 카메라 피드를 통해 여러 장의 이미지를 수집합니다.
- **영상 보기**: 수집된 이미지를 축소된 형태로 확인할 수 있습니다.
- **파노라마 합성**: 수집된 이미지를 기반으로 파노라마 이미지를 생성합니다.
- **이미지 저장**: 합성된 파노라마 이미지를 로컬 디렉토리에 저장할 수 있습니다.
- **프로그램 종료**: '나가기' 버튼을 통해 애플리케이션을 종료할 수 있습니다.

## 사용법
1. **`영상 수집` 버튼 클릭**: 카메라 피드가 열리며, 'c' 키를 눌러 이미지를 수집합니다. 'q' 키를 눌러 영상 수집을 종료합니다.
2. **`영상 보기` 버튼 클릭**: 수집된 이미지들을 확인할 수 있습니다.
3. **`합병` 버튼 클릭**: 파노라마 합성을 시도합니다. 성공 시 합성된 이미지가 표시됩니다.
4. **`저장` 버튼 클릭**: 합성된 파노라마 이미지를 파일로 저장할 수 있습니다.
5. **`나가기` 버튼 클릭**: 프로그램을 종료합니다.

## 개발 환경
- Python 3.8
- PyQt5
- OpenCV
- NumPy
- Windows 10

## 설치 방법
```
conda create -n vision_agent_project5_env python=3.8
conda activate vision_agent_project5_env
pip install pyqt5 opencv-python numpy
```

## 실행 방법
```
python main.py
```

## 주의사항
- 프로그램 사용 시 카메라 장치가 정상적으로 연결되어 있어야 합니다.
- 이미지 수집 시 각도 및 프레임의 일관성을 유지하여 보다 정확한 파노라마 이미지를 얻을 수 있습니다.

