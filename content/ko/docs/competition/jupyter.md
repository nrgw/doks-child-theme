---
title: "Jupyter Lab 설정 방법"
description: ""
lead: "Jupyter Lab을 사용하면 웹브라우져를 통해 코딩하고 출력 이미지 등을 간편하게 확인할 수 있습니다."
date: 2022-01-18T00:52:30Z
lastmod: 2022-01-18T00:52:30Z
draft: false
images: []
menu: 
  docs:
    parent: "competition"
weight: 34
toc: true
---

## Jupyter Lab 설치

제공된 인스턴스의 터미널 상에서 다음을 실행한다.

```bash
$ pip install jupyterlab
```

## Jupyter Lab 서버 띄우기

### 일반적인 방법

터미널 상에서 다음 명령어를 실행한다.
```bash
$ jupyter lab --ip=0.0.0.0
```
화면에서 출력된 token을 따로 저장해둔다. 웹브라우져로
```url
http://[ip 주소]:8888
```
에 접속한다. 비밀번호를 입력하는 란에 token을 입력한다. Jupyter Lab을 띄우는데 사용한 터미널을 종료하는 경우 서버도 함께 종료되니 주의한다.

### Visual Studio Code를 사용하는 경우

새로운 터미널 창을 생성하여 다음 명령어를 실행한다.
```bash
$ jupyter lab
```
화면에서 출력된 token을 따로 저장해둔다. 하단에서 띄워진 메시지에서 '브라우저에서 열기'를 누르거나, 직접 웹브라우져로
```url
http://localhost:8888
```
에 접속한다. 비밀번호를 입력하는 란에 token을 입력한다. Jupyter Lab을 띄우는데 사용한 터미널을 종료하는 경우 서버도 함께 종료되니 주의한다.