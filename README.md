# Mutting Room

music + fitting room. 음악을 틀면서 테마와 위젯을 갈아입혀 보는 뮤직 플레이어.

## 목표

- 뮤직 플레이어 (앨범 재킷 표시)
- 테마 커스텀
- 위젯 커스텀
- 재생 목록, 즐겨찾기, 재생 기록

## 사용 도구

- Python 3.13
- PySide6 (QtWidgets)
- 데이터: iTunes Search API (필요하면 MusicBrainz + Cover Art Archive 추가)
- DB: SQLite

## 폴더 구조
- (작성예정)

## 실행 방법

```bash
conda create -n mutting-room python=3.13 -y
conda activate mutting-room
conda env config vars set PYTHONNOUSERSITE=1
conda deactivate
conda activate mutting-room
conda env config vars list      # PYTHONNOUSERSITE가 정상적으로 적용되었는지 확인 '1'이 나오면 OK
python -m pip install PySide6 mutagen requests
python -m pip check             # 충돌하는 패키지가 있는지 확인
```

## 상태

시작 전. 진행 계획은 [ROADMAP.md](ROADMAP.md) 참고.
