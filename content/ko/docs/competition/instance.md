---
title: "인스턴스 초기 설정"
description: ""
lead: "처음 받은 인스턴스에는 이미 초기 설정이 되어 있습니다. 인스턴스를 새로 발급받는 경우에는 직접 아래 방법으로 설정을 진행하셔야 합니다."
date: 2022-01-05T15:20:58Z
lastmod: 2022-01-05T15:20:58Z
draft: false
images: []
menu: 
  docs:
    parent: "competition"
weight: 33
toc: true
---

## System
* AWS EC2 Instance: c5.xlarge
* OS: Ubuntu 20.04

## Preparation

```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo reboot
```

## Compilers

```bash
$ sudo apt install build-essential gfortran
```

## OpenMPI
```bash
$ sudo apt install openmpi-bin
```

## GNU Plot
```bash
$ sudo apt install gnuplot
```

## Anaconda
```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
$ bash Anaconda3-2021.11-Linux-x86_64.sh -b
$ rm Anaconda3-2021.11-Linux-x86_64.sh
$ eval "$(~/anaconda3/bin/conda shell.bash hook)"
$ conda init
$ conda update --all
```

## GWpy
```bash
$ conda install -y -c conda-forge gwpy
```

## LALSuite
```bash
$ conda install -y -c conda-forge lalsuite
```

## PyCBC
```bash
$ conda install -y -c conda-forge pycbc
```

## Bilby
```bash
$ conda install -y -c conda-forge bilby
```

### Nestle
```bash
$ conda install -y -c conda-forge nestle
```