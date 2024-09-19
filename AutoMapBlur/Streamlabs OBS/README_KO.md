# Streamlabs OBS용 AutoMapBlur

AutoMapBlur를 사용하면 게임 내 지도가 열릴 때 게임 캡처를 자동으로 블러 처리하여 민감한 정보를 보호하고 스트림 스나이핑을 방지할 수 있습니다.

## 기능
- **블러 토글:** 지도 키(기본값: "M")를 눌러 Streamlabs OBS의 게임 캡처에서 블러를 켜거나 끕니다.
- **사용자 지정 키바인딩:** 블러를 트리거하는 키를 사용자 지정할 수 있습니다.
- **블러 강도 조절:** 1(약한 블러)부터 20(강한 블러)까지 사용자의 선호에 따라 블러 강도를 조절할 수 있습니다.

## 설치 방법

### 1단계: Streamlabs OBS에서 WebSocket 설정
1. Streamlabs OBS에서 **WebSocket**이 활성화되어 있는지 확인하세요.
   - **설정 > 리모컨**으로 이동하여 WebSocket을 활성화합니다.
   - WebSocket 암호를 설정하세요 (스크립트 연결에 필요합니다).

### 2단계: Streamlabs OBS에 스크립트 추가
1. `AutoMapBlur_Streamlabs.py` 스크립트를 다운로드하세요.
2. Streamlabs OBS에서 **도구 > 스크립트**로 이동합니다.
3. **+** 버튼을 클릭하고 다운로드한 `AutoMapBlur_Streamlabs.py` 파일을 선택하세요.
4. 추가되면 스크립트가 스크립트 창에 표시됩니다.

### 3단계: 스크립트 설정
1. 블러를 적용할 **소스**를 선택하세요 (예: 게임 캡처).
   - 스크립트 설정 패널에서 **소스 이름**이라는 텍스트 필드를 확인하세요.
2. **블러 강도**를 조절하세요.
   - **블러 강도** 슬라이더를 사용하여 1에서 20 사이의 값을 선택하세요.
3. **지도 키**를 설정하세요 (선택 사항).
   - 기본 "M" 키 대신 다른 키를 사용하려면 **지도 키** 필드에 입력하세요.

### 4단계: 스트리밍 시작
1. 설정이 완료되면, 스트림 중 지도 키를 누를 때마다 AutoMapBlur가 자동으로 블러 효과를 적용합니다.
2. 지도 키를 다시 누르면 블러가 제거됩니다.

## 프로젝트 보드
[AutoMapBlur 프로젝트 보드](https://github.com/users/WhyTrashEarth/projects/1)에서 진행 상황을 확인하고 기여할 수 있습니다.

## GitHub 리포지토리
전체 소스 코드와 자세한 내용은 [GitHub 리포지토리](https://github.com/WhyTrashEarth/AUTOMAPBLUR)에서 확인하세요.

## 사용법
- **블러 토글:** 게임의 지도가 열려 있을 때 지도 키를 눌러 블러 효과를 적용합니다. 다시 누르면 블러가 해제됩니다.
- **커스터마이징:** Streamlabs OBS의 스크립트 설정 패널에서 블러 강도와 키바인딩을 수정할 수 있습니다.

## 문제 해결
- **소스 이름**이 Streamlabs OBS에서 게임 캡처 또는 원하는 소스와 정확히 일치하는지 확인하세요.
- 블러 효과가 활성화되지 않으면 키 설정을 확인하거나 블러 강도를 높여보세요.
- 스크립트가 작동하지 않으면 **도구 > 스크립트**에서 스크립트를 제거한 후 다시 추가하세요.

## 기여
기여하거나 문제를 보고하려면 [AutoMapBlur GitHub 리포지토리](https://github.com/WhyTrashEarth/AUTOMAPBLUR)를 방문하세요.

## 크레딧
AutoMapBlur는 [@WhyTrashEarth](https://x.com/WhyTrashEarth)에서 구상하였으며 커뮤니티의 지원으로 개발되었습니다.

## 라이선스
이 프로젝트는 **CC0 1.0 Universal (Creative Commons Zero v1.0)** Public Domain Dedication에 따라 라이선스가 부여되었습니다. 자유롭게 사용, 수정 및 배포하세요.
