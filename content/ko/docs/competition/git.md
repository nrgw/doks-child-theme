---
title: "답안 제출 방법"
description: ""
lead: "답안 제출은 git을 사용합니다. git에 대한 매뉴얼입니다."
date: 2022-01-16T15:26:07Z
lastmod: 2022-01-16T15:26:07Z
draft: flase
images: []
menu: 
  docs:
    parent: "competition"
weight: 33
toc: true
---

## 작업 디렉토리

인스턴스를 새로 받으면 git 원격 저장소에 연결된 작업 디렉토리가 있다. 해당 디렉토리로 이동한다.

```bash
$ cd ~/2022cca/
```

## git 상태 확인

다음 명령어를 사용하여 git이 제대로 설정되어 있는지 확인한다.

```bash
$ git status
```

## git stage

다음 명령을 통해 모든 변경사항을 staging area로 옮길 수 있다.

```bash
$ git add .
```

## git commit

다음 명령을 통해 staging area의 변경사항을 repository에 commit한다.

```bash
$ git commit -m "This is a message for commit."
```

나중에 변경사항을 찾아볼 때 잘 알아볼 수 있도록 적절한 메시지를 적어주는 것이 좋다.

## git push

다음 명령을 통해 로컬 저장소를 원격 저장소와 동기화한다.

```bash
$ git push
```

채점은 원격 저장소에 저장된 소스코드를 불러와 진행된다.

## 팁

git 원격저장소는 github를 통해 호스팅되고 있다. github 계정을 가지고 있는 경우 슬랙을 통해 요청하면 해당 저장소에 사용자 권한을 추가해줄 수 있다.