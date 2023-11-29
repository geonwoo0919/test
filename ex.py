import random

import pygame as pg


def genSprite(image, pos, status=None):
    Sprite = pg.sprite.Sprite()
    Sprite.image = image
    Sprite.rect = Sprite.image.get_rect()
    Sprite.rect.x, Sprite.rect.y = pos[0], pos[1]
    if status != None:
        Sprite.status = status
    return Sprite


# 게임기본설정
실행여부 = True
화면가로길이, 화면세로길이 = 1000, 800

화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
## 화면 크기 정하기
pg.display.set_caption('광석채굴!')
배경이미지 = pg.image.load('img/r1.jpg')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))
## 이미지를 정해진 사이즈로 변경

소울곰위치 = [화면가로길이 // 2, 화면세로길이 // 2]

게임요소크기 = (152, 152)
소울곰이미지딕셔너리 = {"이동": [], "반대이동": []}
소울곰멈춤이미지 = pg.image.load(f'img/s.png')
소울곰멈춤이미지 = pg.transform.scale(소울곰멈춤이미지, 게임요소크기)
소울곰이미지딕셔너리["멈춤"] = 소울곰멈춤이미지

for 인덱스 in range(6):
    소울곰뛰는모습이미지 = pg.image.load(f'img/{인덱스 + 1}.png')
    소울곰뛰는모습이미지 = pg.transform.scale(소울곰뛰는모습이미지, 게임요소크기)
    if 인덱스 < 3:
        소울곰이미지딕셔너리["이동"].append(소울곰뛰는모습이미지)
    else:
        소울곰이미지딕셔너리["반대이동"].append(소울곰뛰는모습이미지)

# 광석이미지리스트 = []
# for 인덱스 in range(c):
자동차이미지 = pg.image.load(f'img/c.png')
자동차이미지 = pg.transform.scale(자동차이미지, 게임요소크기)
# 광석이미지리스트.append(광석이미지)


소울곰이미지상태 = "멈춤"
소울곰이미지인덱스 = 0
소울곰이미지흐름 = 1
소울곰스프라이트 = genSprite(소울곰이미지딕셔너리[소울곰이미지상태], 소울곰위치)

이미지움직임최대시간 = 0.2
이미지움직임시간 = 0

시계 = pg.time.Clock()
전체시간 = 0
이미지움직임최대시간 = 1
이미지움직임시간 = 0

차스프라이트리스트 = []

광석자동생성남은시간 = 2
광석자동생성시간 = 9

while 실행여부:
    화면.blit(배경이미지, (0, 0))
    흐른시간 = 시계.tick(60) / 1000
    전체시간 += 흐른시간
    화면.blit(소울곰스프라이트.image, 소울곰스프라이트.rect)
    광석자동생성남은시간 -= 흐른시간
    #화면.blit(자동차이미지.image, 자동차이미지.rect)
    if 광석자동생성남은시간 <= 0:
        생성위치 = [random.random() * (화면가로길이 - 게임요소크기[0]), random.random() * (화면세로길이 - 게임요소크기[1])]
        차스프라이트리스트.append(genSprite(자동차이미지, 생성위치))
        광석자동생성남은시간 = 광석자동생성시간

    idx = 0

    for 차_스프라이트 in 차스프라이트리스트:
        if idx % 4 == 0:
            차_스프라이트.rect.x -= 1
        elif idx % 4 == 1:
            차_스프라이트.rect.x += 1
        elif idx % 4 == 2:
            차_스프라이트.rect.y += 1
        else:
            차_스프라이트.rect.y -= 1
        idx += 1
        화면.blit(차_스프라이트.image, 차_스프라이트.rect)
    #자동차이미지.rect = 생성위치

    # 차스프라이트리스트.append(스프라이트생성(광석이미지리스트[-1], (200, 200), 광석최대상태))

    pg.event.get()
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_RIGHT] or keys[pg.K_UP] or keys[pg.K_DOWN]:
        이미지움직임시간 -= 흐른시간
        if keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
            if keys[pg.K_LEFT]:
                if 소울곰이미지상태 != '이동':
                    소울곰이미지상태 = '이동'
                if 소울곰위치[0] >= 0:
                    소울곰위치[0] -= 1  # 원하는 속도
            if keys[pg.K_RIGHT]:
                if 소울곰이미지상태 != "반대이동":
                    소울곰이미지상태 = "반대이동"
                if 소울곰위치[0] < 화면가로길이 - 게임요소크기[0] + 20:
                    소울곰위치[0] += 1
        if keys[pg.K_UP] or keys[pg.K_DOWN]:
            if 소울곰이미지상태 != '이동' and 소울곰이미지상태 != '반대이동':
                소울곰이미지상태 = '이동'
            if keys[pg.K_UP]:
                소울곰위치[1] -= 1
            elif keys[pg.K_DOWN]:
                소울곰위치[1] += 1
            else:
                이미지움직임시간 = 0.2
            소울곰이미지상태 = '멈춤'
            소울곰이미지흐름 = 1
            소울곰이미지인덱스 = 0
            소울곰스프라이트.image = 소울곰이미지딕셔너리[소울곰이미지상태]
            if 이미지움직임시간 <= 0:
                이미지움직임시간 = 이미지움직임최대시간
                소울곰이미지인덱스 += 소울곰이미지흐름
                if 소울곰이미지상태 == '멈춤':
                    소울곰스프라이트.image = 소울곰이미지딕셔너리[소울곰이미지상태]
                else:
                    소울곰스프라이트.image = 소울곰이미지딕셔너리[소울곰이미지상태][소울곰이미지인덱스]
                    if 소울곰이미지인덱스 == 0 or 소울곰이미지인덱스 == len(소울곰이미지딕셔너리[소울곰이미지상태]) - 1:
                        소울곰이미지흐름 *= -1
    소울곰스프라이트.rect = 소울곰위치
    pg.display.update()

pg.display.quit()
