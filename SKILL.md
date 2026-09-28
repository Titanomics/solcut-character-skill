---
name: 솔커트캐릭터
description: "솔커트 캐릭터" = 솔커트(SOL-CUT) 초록 스틱 파우치 자체가 몸통이고 흰 하단에 얼굴, 흰 팔다리·흰 운동화가 달린 3D 제품 의인화 캐릭터 레퍼런스. 사용자가 "솔커트 캐릭터", "스틱 캐릭터"라고 하면 이 캐릭터를 뜻한다. 이 캐릭터로 이미지·영상·릴스를 만들거나 표정/포즈/배경을 바꿀 때 반드시 먼저 읽고 누끼·기준 이미지를 레퍼런스로 넣는다.
---

# 솔커트 캐릭터 (스틱 파우치 의인화)

"솔커트 캐릭터" = 이 캐릭터. ("솔다"는 다람쥐 마스코트로 별개 → `솔다` 스킬)

## 이미지 (`이미지/`)
| 파일 | 내용 |
|---|---|
| `솔커트캐릭터_기준_억새밭.png` | **대표 이미지.** 1080×1920, 가을 억새밭 배경, 캐릭터 왼쪽 배치 (0928 캐릭터 노래 영상 시드) |
| `솔커트캐릭터_누끼.png` | 투명 배경 캐릭터 누끼 (424×1176). 다른 배경에 합성할 때 사용 |
| `솔커트캐릭터_원본_가을길.jpg` | 생성 원본 (단풍 가을길, 캐릭터 중앙) |
| `배경_억새밭.jpg` | 캐릭터 없는 빈 억새밭 배경 |

## 외형 고정값
| 항목 | 값 |
|---|---|
| 몸통 | 솔커트 스틱 파우치 그대로. 위 진초록 + 톱니 실링, "◀OPEN", 세로 흰 글씨 **"SOL-CUT 솔커트"** |
| 중단 | 이슬 맺힌 솔잎 사진 띠 → 회색 띠 "Terpino™" |
| 하단(얼굴) | 흰 바탕에 큰 검은 눈(반짝이 ✦), 분홍 볼터치, 활짝 웃는 입. 아래 "비오리젠 BO REGEN", 초록 "20g", 맨 아래 진초록 실링 |
| 팔 | 흰색 고무 질감 팔 + 흰 장갑 손 (기본: 오른손 흔들기, 왼팔 아래) |
| 다리 | 짧은 흰 다리 + 초록 포인트 흰 운동화 |
| 질감 | 광택 비닐 토이 3D |
| 라벨 | 항상 정면. **"솔커트"가 "솔컷" 등으로 변형되면 폐기** (v2 재구도에서 실제로 발생) |

## 기본 표정·포즈·배경
- 표정: 반짝이는 눈 + 입 벌린 활짝 웃음
- 포즈: 정면 직립, 한 손 흔들기
- 배경(대표): 가을 억새밭, 맑은 파란 하늘, 먼 단풍 산 / 캐릭터는 화면 왼쪽 흙길 위, 스틱 윗단 y610 · 발끝 y1820 (1080×1920)

## 다른 배경에 합성
```
python compose.py 새배경.jpg 결과.png            # 대표 구도(왼쪽)
python compose.py 새배경.jpg 결과.png --cx 540   # 가운데
```
(Pillow만 필요. 발 아래 접지 그림자 자동)

## 생성 프롬프트 베이스 (영문)
> A cute glossy vinyl-toy 3D mascot whose body is the green SOL-CUT stick pouch: dark green top with serrated seal and "◀OPEN", vertical white text "SOL-CUT 솔커트", a band of dewy pine needles, a gray "Terpino™" band, and a white lower section with a face — big sparkly black eyes, pink blush, wide open smile — above "비오리젠 BO REGEN" and green "20g". White rubbery arms with white gloved hands, short white legs, white sneakers with green accents. Label always facing camera.

표정/포즈/배경을 바꿀 때는 `솔커트캐릭터_누끼.png`를 레퍼런스로 넣고 "same character as reference, keep the pouch label text exactly identical"을 붙인다. 생성 후 라벨 글자("SOL-CUT 솔커트", "Terpino™", "비오리젠") 확대 확인 필수.

## 변주 기록
확정된 새 표정·포즈·배경 컷은 `이미지/솔커트캐릭터_<설명>.png`로 저장하고 여기 한 줄 추가.

| 파일 | 표정 | 포즈 | 배경 |
|---|---|---|---|
| 솔커트캐릭터_기준_억새밭.png | 활짝 웃음 | 손 흔들기 | 가을 억새밭 |
| 솔커트캐릭터_원본_가을길.jpg | 활짝 웃음 | 손 흔들기 | 단풍 가을길 |

제품 정보·표현 규제는 `솔커트` 스킬을 따른다.
