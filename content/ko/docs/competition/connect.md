---
title: "인스턴스 접속 방법"
description: ""
lead: ""
date: 2022-01-10T06:10:23Z
lastmod: 2022-01-10T06:10:23Z
draft: false
images: []
menu: 
  docs:
    parent: "competition"
weight: 32
toc: true
---

## 사전에 알아야할 정보

* 접속 ip
* ssh key 파일

위의 정보들은 슬랙을 통해 개별 전달될 예정입니다.

## Windows

### Xming 설치

Xming을 다음 사이트에서 다운로드 받는다.

* [https://sourceforge.net/projects/xming/](https://sourceforge.net/projects/xming/)

설치파일을 실행한뒤 계속 `Next >` 를 누르면 된다.

### ssh 접속

`Windows Key + R` 키를 눌러 `cmd` 를 실행시킨다.

<img src="../cmd.png">

ssh key 파일이 다운로드 폴더에 있다고 가정하고 해당 디렉토리로 이동한다.

```shelll
> cd Downloads
```

X11 Forward를 위한 변수 설정을 한다.

```shell
> set DISPLAY=localhost:0.0
```

다음과 같이 ssh 접속을 한다.

```shell
> ssh -Y -i [ssh key 파일] ubuntu@[접속 ip]
```

## Mac OS

### XQuartz 설치



## Linux