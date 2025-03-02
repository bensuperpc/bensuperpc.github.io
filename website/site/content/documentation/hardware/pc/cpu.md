+++
title = "Evolutions of x86 CPUs"
description = "Evolutions of x86 CPUs"
date = 2025-02-22T00:00:00Z
draft = false
aliases = ["en/documentation/hardware/pc/cpu/"]

[taxonomies]
tags = ["Features","x86","CPU","Processor"]
categories = ["Hardware"]
[extra]
keywords = "Processor, x86, CPU, Intel, AMD"
toc = true
series = "Features"
+++

## Introduction

# Intel CPU

| **Release** | **Microarch** | **CPU Models/Series**                     | **MMX** | **SSE** | **SSE2** | **SSE3** | **SSE4** | **AVX2** | **AVX-512** | **FMA3** | **AES-NI** |
| ----------- | ------------- | ----------------------------------------- | ------- | ------- | -------- | -------- | -------- | -------- | ----------- | -------- | ---------- |
| 1979        | 8088/8086     | Intel 8088/8086                           | -       | -       | -        | -        | -        | -        | -           | -        | -          |
| 1982        | 80286         | Intel 80286                               | -       | -       | -        | -        | -        | -        | -           | -        | -          |
| 1985        | 80386         | Intel 80386                               | -       | -       | -        | -        | -        | -        | -           | -        | -          |
| 1989        | 80486         | Intel 80486                               | -       | -       | -        | -        | -        | -        | -           | -        | -          |
| 1993        | P5 (Pentium)  | Pentium (P5)                              | -       | -       | -        | -        | -        | -        | -           | -        | -          |
| 1995        | P6            | Pentium Pro                               | -       | -       | -        | -        | -        | -        | -           | -        | -          |
| 1997        | P6            | Pentium II/III                            | Yes     | Yes     | -        | -        | -        | -        | -           | -        | -          |
| 2000        | NetBurst      | Pentium 4 (Willamette/Northwood)          | Yes     | Yes     | Yes      | -        | -        | -        | -           | -        | -          |
| 2004        | NetBurst      | Pentium 4/D (Prescott)                    | Yes     | Yes     | Yes      | Yes      | -        | -        | -           | -        | -          |
| 2006        | Core          | Core 2 E6/Q6xxx, E1/E2xxx                 | Yes     | Yes     | Yes      | Yes      | -        | -        | -           | -        | -          |
| 2007        | Penryn        | Core 2 E7/E8/Q8/Q9xxx, E2/E5/E6xxx        | Yes     | Yes     | Yes      | Yes      | SSSE3    | -        | -           | -        | -          |
| 2008        | Nehalem       | Core i3/i5/i7 9xx                         | Yes     | Yes     | Yes      | Yes      | Yes      | -        | -           | -        | -          |
| 2010        | Westmere      | Core i3/i5/i7 xxx, Pentium G69xx          | Yes     | Yes     | Yes      | Yes      | Yes      | -        | -           | -        | Yes        |
| 2011        | Sandy Bridge  | Core i3/i5/i7 2xxx, Pentium G6xx/G8xx     | Yes     | Yes     | Yes      | Yes      | Yes      | AVX      | -           | -        | Yes        |
| 2012        | Ivy Bridge    | Core i3/i5/i7 3xxx, Pentium G2xxx         | Yes     | Yes     | Yes      | Yes      | Yes      | AVX      | -           | -        | Yes        |
| 2013-2014   | Haswell       | Core i3/i5/i7 4xxx, Pentium G3xxx         | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2014        | Broadwell     | Core i3/i5/i7 5xxx                        | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2015        | Skylake       | Core i3/i5/i7 6xxx, Pentium G44xx         | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2016        | Kaby Lake     | Core i3/i5/i7 7xxx, Pentium G45xx/G46xx   | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2018-2019   | Coffee Lake   | Core i3/i5/i7/i9 8xxx/9xxx, Pentium G5xxx | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2019        | Ice Lake      | Core i3/i5/i7 10xxxGx (mobile only)       | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | Yes         | Yes      | Yes        |
| 2020        | Comet Lake    | Core i3/i5/i7/i9 10xxx, Pentium G6xxx     | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2020        | Tiger Lake    | Core i3/i5/i7 11xxxGx (mobile only)       | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | Yes         | Yes      | Yes        |
| 2021        | Rocket Lake   | Core i3/i5/i7/i9 11xxx                    | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | Yes         | Yes      | Yes        |
| 2021        | Alder Lake    | Core i3/i5/i7/i9 12xxx, Pentium G7xxx     | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2022        | Raptor Lake   | Core i3/i5/i7/i9 13xxx/14xxx              | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2024        | Meteor Lake   | Core Ultra 3/5/7/9 1xx                    | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |
| 2024        | Lunar Lake    | Core Ultra 3/5/7/9 2xx                    | Yes     | Yes     | Yes      | Yes      | Yes      | Yes      | -           | Yes      | Yes        |

All **pentium** and **celeron** processors does not support AVX, AVX2 and AVX-512.

# AMD CPU

| **Release** | **Microarch** | **CPU Models/Series**            | **MMX** | **SSE** | **SSE2** | **SSE3** | **SSE4** | **AVX** | **AVX2** | **AVX-512** | **FMA3** | **AES-NI** |
| ----------- | ------------- | -------------------------------- | ------- | ------- | -------- | -------- | -------- | ------- | -------- | ----------- | -------- | ---------- |
| 1996        | K5            | AMD K5                           | -       | -       | -        | -        | -        | -       | -        | -           | -        | -          |
| 1997        | K6            | AMD K6, K6-II, K6-III            | Yes     | -       | -        | -        | -        | -       | -        | -           | -        | -          |
| 1999        | K7 (Athlon)   | AMD Athlon, Duron                | Yes     | Yes     | -        | -        | -        | -       | -        | -           | -        | -          |
| 2003        | K8            | AMD Athlon 64, Opteron           | Yes     | Yes     | Yes      | Yes      | -        | -       | -        | -           | -        | -          |
| 2007        | K10           | AMD Phenom, Phenom II, Athlon II | Yes     | Yes     | Yes      | Yes      | SSE4a    | -       | -        | -           | -        | -          |
| 2011        | Bulldozer     | AMD FX x1xx, Opteron (Bulldozer) | Yes     | Yes     | Yes      | Yes      | SSE4a    | -       | -        | -           | FMA4     | Yes        |
| 2012        | Piledriver    | AMD FX x3xx (Piledriver)         | Yes     | Yes     | Yes      | Yes      | SSE4a    | -       | -        | -           | FMA4     | Yes        |
| 2014        | Steamroller   | AMD APUs (Steamroller)           | Yes     | Yes     | Yes      | Yes      | SSE4a    | -       | -        | -           | Yes      | Yes        |
| 2015        | Excavator     | AMD APUs (Excavator)             | Yes     | Yes     | Yes      | Yes      | SSE4a    | -       | -        | -           | Yes      | Yes        |
| 2017        | Zen           | AMD Ryzen 1xxx, EPYC 7xx1        | Yes     | Yes     | Yes      | Yes      | Yes      | Yes     | Yes      | -           | Yes      | Yes        |
| 2018        | Zen+          | AMD Ryzen 2xxx                   | Yes     | Yes     | Yes      | Yes      | Yes      | Yes     | Yes      | -           | Yes      | Yes        |
| 2019        | Zen 2         | AMD Ryzen 3xxx, EPYC 7xx2        | Yes     | Yes     | Yes      | Yes      | Yes      | Yes     | Yes      | -           | Yes      | Yes        |
| 2020        | Zen 3         | AMD Ryzen 5xxx, EPYC 7xx3        | Yes     | Yes     | Yes      | Yes      | Yes      | Yes     | Yes      | -           | Yes      | Yes        |
| 2022        | Zen 4         | AMD Ryzen 7xxx, EPYC 4/8/9xx4    | Yes     | Yes     | Yes      | Yes      | Yes      | Yes     | Yes      | Yes         | Yes      | Yes        |
| 2024        | Zen 5         | AMD Ryzen 9xxx, EPYC 9xx5        | Yes     | Yes     | Yes      | Yes      | Yes      | Yes     | Yes      | Yes         | Yes      | Yes        |
