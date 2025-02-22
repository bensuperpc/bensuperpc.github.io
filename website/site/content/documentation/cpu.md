+++
title = "x86 CPU"
description = "x86 CPU"
date = 2025-02-22T00:00:00Z
draft = false

[taxonomies]
tags = ["Features","x86","CPU","Processor"]
[extra]
keywords = "Processor, x86, CPU"
toc = true
series = "Features"
+++

## Introduction

# Intel CPU

| **Release** | **Microarch** | **CPU Models/Series**                         | **MMX** | **SSE** | **SSE2** | **SSE3** | **SSE4**    | **AVX** | **AVX2** | **AVX-512** | **FMA** | **AES-NI** |
| ----------- | ------------- | --------------------------------------------- | ------- | ------- | -------- | -------- | ----------- | ------- | -------- | ----------- | ------- | ---------- |
| 1979        | 8088/8086     | Intel 8088/8086                               | -       | -       | -        | -        | -           | -       | -        | -           | -       | -          |
| 1982        | 80286         | Intel 80286                                   | -       | -       | -        | -        | -           | -       | -        | -           | -       | -          |
| 1985        | 80386         | Intel 80386                                   | -       | -       | -        | -        | -           | -       | -        | -           | -       | -          |
| 1989        | 80486         | Intel 80486                                   | -       | -       | -        | -        | -           | -       | -        | -           | -       | -          |
| 1993        | P5 (Pentium)  | Pentium (P5)                                  | -       | -       | -        | -        | -           | -       | -        | -           | -       | -          |
| 1995        | P6            | Pentium Pro                                   | -       | -       | -        | -        | -           | -       | -        | -           | -       | -          |
| 1997        | P6            | Pentium II/III                                | Yes     | Yes     | -        | -        | -           | -       | -        | -           | -       | -          |
| 2000        | NetBurst      | Pentium 4 (Willamette/Northwood)              | Yes     | Yes     | Yes      | -        | -           | -       | -        | -           | -       | -          |
| 2004        | NetBurst      | Pentium 4/D (Prescott)                        | Yes     | Yes     | Yes      | Yes      | -           | -       | -        | -           | -       | -          |
| 2006        | Core          | Core 2 (Conroe/Merom), Pentium E2xxx          | Yes     | Yes     | Yes      | Yes      | -           | -       | -        | -           | -       | -          |
| 2007        | Penryn        | Core 2 (Penryn/Wolfdale), Pentium E5xxx/E6xxx | Yes     | Yes     | Yes      | Yes      | Yes (SSSE3) | -       | -        | -           | -       | -          |
| 2008        | Nehalem       | Core i3/i5/i7 9xx                             | Yes     | Yes     | Yes      | Yes      | Yes         | -       | -        | -           | -       | -          |
| 2010        | Westmere      | Core i3/i5/i7 xxx, Pentium G69xx              | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | -        | -           | -       | Yes        |
| 2011        | Sandy Bridge  | Core i3/i5/i7 2xxx, Pentium G6xx/G8xx         | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | -        | -           | -       | Yes        |
| 2012        | Ivy Bridge    | Core i3/i5/i7 3xxx, Pentium G2xxx             | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | -        | -           | -       | Yes        |
| 2013-2014   | Haswell       | Core i3/i5/i7 4xxx, Pentium G3xxx             | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2014        | Broadwell     | Core i3/i5/i7 5xxx                            | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2015        | Skylake       | Core i3/i5/i7 6xxx, Pentium G44xx             | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2016        | Kaby Lake     | Core i3/i5/i7 7xxx, Pentium G45xx/G46xx       | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2018-2019   | Coffee Lake   | Core i3/i5/i7/i9 8xxx/9xxx, Pentium G5xxx     | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2019        | Ice Lake      | Core i3/i5/i7 10xxxGx (mobile only)           | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | Yes         | Yes     | Yes        |
| 2020        | Comet Lake    | Core i3/i5/i7/i9 10xxx, Pentium G6xxx         | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2020        | Tiger Lake    | Core i3/i5/i7 11xxxGx (mobile only)           | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | Yes         | Yes     | Yes        |
| 2021        | Rocket Lake   | Core i3/i5/i7/i9 11xxx                        | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | Yes         | Yes     | Yes        |
| 2021        | Alder Lake    | Core i3/i5/i7/i9 12xxx, Pentium G7xxx         | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2022        | Raptor Lake   | Core i3/i5/i7/i9 13xxx/14xxx                  | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2024        | Meteor Lake   | Core Ultra 3/5/7 1xx                          | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |
| 2024        | Lunar Lake    | Core Ultra 3/5/7 2xx                          | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes     | Yes        |

All pentium and celron processors does not support AVX, AVX2 and AVX-512.

# AMD CPU

| **Release** | **Microarch** | **CPU Models/Series**                     | **MMX** | **SSE** | **SSE2** | **SSE3** | **SSE4**    | **AVX** | **AVX2** | **AVX-512** | **FMA**    | **AES-NI** |
| ----------- | ------------- | ----------------------------------------- | ------- | ------- | -------- | -------- | ----------- | ------- | -------- | ----------- | ---------- | ---------- |
| 1996        | K5            | AMD K5                                    | -       | -       | -        | -        | -           | -       | -        | -           | -          | -          |
| 1997        | K6            | AMD K6, K6‑II, K6‑III                     | Yes     | -       | -        | -        | -           | -       | -        | -           | -          | -          |
| 1999        | K7 (Athlon)   | AMD Athlon, Duron                         | Yes     | Yes     | -        | -        | -           | -       | -        | -           | -          | -          |
| 2003        | K8            | AMD Athlon 64, Opteron                    | Yes     | Yes     | Yes      | Yes      | -           | -       | -        | -           | -          | -          |
| 2007        | K10           | AMD Phenom, Phenom II, Athlon II, Opteron | Yes     | Yes     | Yes      | Yes      | Yes (SSE4a) | -       | -        | -           | -          | -          |
| 2011        | Bulldozer     | AMD FX x1xx, Opteron (Bulldozer)          | Yes     | Yes     | Yes      | Yes      | Yes (SSE4a) | -       | -        | -           | Yes (FMA4) | Yes        |
| 2012        | Piledriver    | AMD FX x3xx (Piledriver)                  | Yes     | Yes     | Yes      | Yes      | Yes (SSE4a) | -       | -        | -           | Yes (FMA4) | Yes        |
| 2014        | Steamroller   | AMD APUs (Steamroller)                    | Yes     | Yes     | Yes      | Yes      | Yes (SSE4a) | -       | -        | -           | Yes        | Yes        |
| 2015        | Excavator     | AMD APUs (Excavator)                      | Yes     | Yes     | Yes      | Yes      | Yes (SSE4a) | -       | -        | -           | Yes        | Yes        |
| 2017        | Zen           | AMD Ryzen 1000, EPYC (Naples)             | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes        | Yes        |
| 2018        | Zen+          | AMD Ryzen 2000, EPYC (Zen+)               | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes        | Yes        |
| 2019        | Zen 2         | AMD Ryzen 3000, EPYC (Rome)               | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes        | Yes        |
| 2020        | Zen 3         | AMD Ryzen 5000, EPYC (Milan)              | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | -           | Yes        | Yes        |
| 2022        | Zen 4         | AMD Ryzen 7000, EPYC (Genoa)              | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | Yes         | Yes        | Yes        |
| 2024        | Zen 5         | AMD Ryzen 9000, EPYC (Verona)             | Yes     | Yes     | Yes      | Yes      | Yes         | Yes     | Yes      | Yes         | Yes        | Yes        |
