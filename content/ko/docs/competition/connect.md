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

## 윈도우즈 사용자

### Xming 설치

Xming을 다음 사이트에서 다운로드 받는다.

* [https://sourceforge.net/projects/xming/](https://sourceforge.net/projects/xming/)

설치파일을 실행한뒤 계속 `Next >` 를 누르면 된다.

### 명령 프롬프트 실행

`Windows Key + R` 키를 눌러 `cmd` 를 실행시킨다.

<img src="../cmd.png">

### ssh 접속

다운로드 받은 ssh key 파일이 있는 디렉토리로 이동한다. (여기서는 다운로드 폴더에 있다고 가정한다.)

```shelll
> cd Downloads
```

X11 Forward를 위한 변수 설정을 한다.

```shell
> set DISPLAY=localhost:0.0
```

다음과 같이 ssh 접속을 한다.

```shell
> ssh -Y -i [ssh key 파일이름] ubuntu@[접속 ip]
```

## 맥 OS 사용자

### XQuartz 설치

XQuartz를 다음 사이트에서 다운로드 받는다.

* [https://www.xquartz.org/](https://www.xquartz.org/)

설치파일을 실행한뒤 "계속", "동의", "설치" 등을 누른다.

### 터미널 실행

`Command + Space` 키를 눌러 `터미널.app` 을 실행한다.

<img src="../terminal.png">

### ssh 접속

다운로드 받은 ssh key 파일이 있는 디렉토리로 이동한다. (여기서는 다운로드 폴더에 있다고 가정한다.)

```shell
% cd ~/Downloads/
```

ssh key 파일의 접근 권한을 제한해준다.

```shell
% chmod 600 [ssh key 파일이름]
```

다음과 같이 ssh 접속을 한다.

```shell
% ssh -Y -i [ssh key 파일이름] ubuntu@[접속 ip]
```

## 리눅스 사용자

우분투를 기준으로 설명합니다. 대부분의 리눅스 데스크톱은 X11을 기반으로 구동되기 때문에 별도의 프로그램 설치가 필요 없습니다.

### 터미널 실행

`Ctrl + Alt + T` 키를 눌러 `Terminal` 을 실행한다.

### ssh 접속

다운로드 받은 ssh key 파일이 있는 디렉토리로 이동한다. (여기서는 다운로드 폴더에 있다고 가정한다.)

```shell
$ cd ~/Downloads/
```

ssh key 파일의 접근 권한을 제한해준다.

```shell
$ chmod 600 [ssh key 파일이름]
```

다음과 같이 ssh 접속을 한다.

```shell
$ ssh -Y -i [ssh key 파일이름] ubuntu@[접속 ip]
```

## 팁

### ssh config 설정

ssh config 파일을 이용하면 매번 ssh를 접속할 때마다 긴 명령을 치는 수고를 덜어줄 수 있다. ssh key 파일을 일단 `~/.ssh/`에 옮긴다. (윈도우는 파일 탐색기를 이용해 `$HOME\.ssh\`에 옮긴다.)

```shell
% cd ~/Downloads/
% mv [ssh key 파일이름] ~/.ssh/
```

ssh config 파일은 `~/.ssh/config`에 위치하고 있다. (윈도우는 `$HOME\.ssh\`) 이를 텍스트 에디터로 열어 아래 설정을 추가한다.

```shell
Host 2022cca
  HostName [접속 ip]
  User ubuntu
  IdentityFile ~/.ssh/[ssh key 파일이름]
  ForwardX11Trusted yes
```

설정을 한 뒤에는 ssh를 접속할 때 다음과 같은 명령을 사용하면 된다.

```shell
% ssh 2022cca
```