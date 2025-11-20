+++
title = "L'évolution des CPUs"
description = "L'évolution des processeurs Intel, AMD et ARM de 1979 à 2025"
date = 2025-02-24T00:00:00Z
draft = false

[taxonomies]
tags = ["Features","x86","CPU","Processor"]
categories = ["Hardware"]
[extra]
keywords = "Processor, x86, CPU, Intel, AMD"
toc = true
series = "Features"
+++

# Introduction

## Intel CPU

| **Release** | **Microarch** | **CPU Models/Series**                     | **SIMD instructions**                          | **FMA3**                                   | **AES-NI**                                 |
| ----------- | ------------- | ----------------------------------------- | ---------------------------------------------- | ------------------------------------------ | ------------------------------------------ |
| 1979        | 8088/8086     | Intel 8088/8086                           | {{ color2(color="#FF4136", text="No") }}       | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 1982        | 80286         | Intel 80286                               | {% color(color="#FF4136") %} No {% end %}      | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 1985        | 80386         | Intel 80386                               | {% color(color="#FF4136") %} No {% end %}      | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 1989        | 80486         | Intel 80486                               | {% color(color="#FF4136") %} No {% end %}      | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 1993        | P5 (Pentium)  | Pentium                                   | {% color(color="#FF4136") %} No {% end %}      | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 1995        | P6            | Pentium Pro                               | {% color(color="#FF4136") %} No {% end %}      | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 1997        | P6            | Pentium II                                | {% color(color="#FF5645") %} MMX {% end %}     | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 1999        | P6            | Pentium III                               | {% color(color="#FF6F61") %} SSE {% end %}     | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 2000        | NetBurst      | Pentium 4 (Willamette/Northwood)          | {% color(color="#FFB347") %} SSE2 {% end %}    | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 2004        | NetBurst      | Pentium 4/D (Prescott)                    | {% color(color="#FFD700") %} SSE3 {% end %}    | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 2006        | Core          | Core 2 E6/Q6xxx, E1/E2xxx                 | {% color(color="#FFD700") %} SSE3 {% end %}    | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 2007        | Penryn        | Core 2 E7/E8/Q8/Q9xxx, E2/E5/E6xxx        | {% color(color="#ADFF2F") %} SSSE3 {% end %}   | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 2008        | Nehalem       | Core i3/i5/i7 9xx                         | {% color(color="#2ECC40") %} SSE4 {% end %}    | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#FF4136") %} No {% end %}  |
| 2010        | Westmere      | Core i3/i5/i7 xxx, Pentium G69xx          | {% color(color="#00C49A") %} SSE4.2 {% end %}  | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2011        | Sandy Bridge  | Core i3/i5/i7 2xxx, Pentium G6xx/G8xx     | {% color(color="#00D100") %} AVX {% end %}     | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2012        | Ivy Bridge    | Core i3/i5/i7 3xxx, Pentium G2xxx         | {% color(color="#00D100") %} AVX {% end %}     | {% color(color="#FF4136") %} No {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2013-2014   | Haswell       | Core i3/i5/i7 4xxx, Pentium G3xxx         | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2014        | Broadwell     | Core i3/i5/i7 5xxx                        | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2015        | Skylake       | Core i3/i5/i7 6xxx, Pentium G44xx         | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2016        | Kaby Lake     | Core i3/i5/i7 7xxx, Pentium G45xx/G46xx   | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2018-2019   | Coffee Lake   | Core i3/i5/i7/i9 8xxx/9xxx, Pentium G5xxx | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2019        | Ice Lake      | Core i3/i5/i7 10xxxGx (mobile only)       | {% color(color="#1AC7FF") %} AVX-512 {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2020        | Comet Lake    | Core i3/i5/i7/i9 10xxx, Pentium G6xxx     | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2020        | Tiger Lake    | Core i3/i5/i7 11xxxGx (mobile only)       | {% color(color="#1AC7FF") %} AVX-512 {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2021        | Rocket Lake   | Core i3/i5/i7/i9 11xxx                    | {% color(color="#1AC7FF") %} AVX-512 {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2021        | Alder Lake    | Core i3/i5/i7/i9 12xxx, Pentium G7xxx     | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2022        | Raptor Lake   | Core i3/i5/i7/i9 13xxx/14xxx              | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2024        | Meteor Lake   | Core Ultra 3/5/7/9 1xx                    | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2024        | Lunar Lake    | Core Ultra 3/5/7/9 2xx                    | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2024        | Arrow Lake    | Core Ultra 3/5/7/9 3xx                    | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2025 ?      | Nova Lake     | Core Ultra 3/5/7/9 4xx                    | {% color(color="#1EA9FF") %} 10.2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |

*Note: Les processeurs **pentium** et **celeron** jusqu'aux **Comet Lake** ne supportent pas AVX, AVX2 et AVX-512.*

## AMD CPU

| **Release** | **Microarch** | **CPU Models/Series**            | **SIMD instructions**                          | **FMA3**                                    | **AES-NI**                                 |
| ----------- | ------------- | -------------------------------- | ---------------------------------------------- | ------------------------------------------- | ------------------------------------------ |
| 1996        | K5            | AMD K5                           | {% color(color="#FF4136") %} No {% end %}      | {% color(color="#FF4136") %} No {% end %}   | {% color(color="#FF4136") %} No {% end %}  |
| 1997        | K6            | AMD K6, K6-II, K6-III            | {% color(color="#FF5645") %} MMX {% end %}     | {% color(color="#FF4136") %} No {% end %}   | {% color(color="#FF4136") %} No {% end %}  |
| 1999        | K7 (Athlon)   | AMD Athlon, Duron                | {% color(color="#FF6F61") %} SSE {% end %}     | {% color(color="#FF4136") %} No {% end %}   | {% color(color="#FF4136") %} No {% end %}  |
| 2003        | K8            | AMD Athlon 64, Opteron           | {% color(color="#FFD700") %} SSE3 {% end %}    | {% color(color="#FF4136") %} No {% end %}   | {% color(color="#FF4136") %} No {% end %}  |
| 2007        | K10           | AMD Phenom, Phenom II, Athlon II | {% color(color="#ADFF2F") %} SSE4a {% end %}   | {% color(color="#FF4136") %} No {% end %}   | {% color(color="#FF4136") %} No {% end %}  |
| 2011        | Bulldozer     | AMD FX x1xx, Opteron (Bulldozer) | {% color(color="#00D100") %} AVX {% end %}     | {% color(color="#FFD700") %} FMA4 {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2014        | Steamroller   | AMD APUs (Steamroller)           | {% color(color="#00D100") %} AVX {% end %}     | {% color(color="#1AC7FF") %} Yes {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2015        | Excavator     | AMD APUs (Excavator)             | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2017        | Zen           | AMD Ryzen 1xxx, EPYC 7xx1        | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2018        | Zen+          | AMD Ryzen 2xxx                   | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2019        | Zen 2         | AMD Ryzen 3xxx, EPYC 7xx2        | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2020        | Zen 3         | AMD Ryzen 5xxx, EPYC 7xx3        | {% color(color="#00CED1") %} AVX2 {% end %}    | {% color(color="#1AC7FF") %} Yes {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2022        | Zen 4         | AMD Ryzen 7xxx, EPYC 4/8/9xx4    | {% color(color="#1AC7FF") %} AVX-512 {% end %} | {% color(color="#1AC7FF") %} Yes {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2024        | Zen 5         | AMD Ryzen 9xxx, EPYC 9xx5        | {% color(color="#1AC7FF") %} AVX-512 {% end %} | {% color(color="#1AC7FF") %} Yes {% end %}  | {% color(color="#1AC7FF") %} Yes {% end %} |

## ARM CPU

| **Release** | **Microarch** | **CPU Models/Series** | **Inst. length** | **SIMD instructions**                                  | **Out-of-order**                           |
| ----------- | ------------- | --------------------- | ---------------- | ------------------------------------------------------ | ------------------------------------------ |
| ?           | ARMv1         | ARM1                  |                  | {% color(color="#FF4136") %} No {% end %}              | {% color(color="#FF4136") %} No {% end %}  |
| ?           | ARMv2         | ARM2                  |                  | {% color(color="#FF4136") %} No {% end %}              | {% color(color="#FF4136") %} No {% end %}  |
| ?           | ARMv3         | ARM6                  | 32-bit           | {% color(color="#FF4136") %} No {% end %}              | {% color(color="#FF4136") %} No {% end %}  |
| 1993        | ARMv4         | ARM7                  | 32-bit           | {% color(color="#FF4136") %} No {% end %}              | {% color(color="#FF4136") %} No {% end %}  |
| 1998        | ARMv5         | ARM9                  | 32-bit           | {% color(color="#FF4136") %} No {% end %}              | {% color(color="#FF4136") %} No {% end %}  |
| 2002        | ARMv6         | ARM11                 | 32-bit           | {% color(color="#FF4136") %} No {% end %}              | {% color(color="#FF4136") %} No {% end %}  |
| 2005        | ARMv7         | Cortex-A8             | 32-bit           | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2007        | ARMv7         | Cortex-A9             | 32-bit           | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2009        | ARMv7         | Cortex-A5             | 32-bit           | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#FF4136") %} No {% end %}  |
| 2011        | ARMv7         | Cortex-A7             | 32-bit           | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#FF4136") %} No {% end %}  |
| 2011        | ARMv7         | Cortex-A15            | 32-bit           | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2012        | ARMv8         | Cortex-A53            | 32-bit/64-bit    | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#FF4136") %} No {% end %}  |
| 2012        | ARMv8         | Cortex-A57            | 32-bit/64-bit    | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2013        | ARMv7         | Cortex-A12            | 32-bit           | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2014        | ARMv7         | Cortex-A17            | 32-bit           | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2016        | ARMv8         | Cortex-A72            | 32-bit/64-bit    | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2016        | ARMv8         | Cortex-A73            | 32-bit/64-bit    | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2016        | ARMv8         | Cortex-A32            | 32-bit           | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#FF4136") %} No {% end %}  |
| 2016        | ARMv8         | Cortex-A35            | 32-bit/64-bit    | {% color(color="#FFD700") %} NEON {% end %}            | {% color(color="#FF4136") %} No {% end %}  |
| 2017        | ARMv8.2       | Cortex-A75            | 32-bit/64-bit    | {% color(color="#ADFF2F") %} NEON (opt. SVE) {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2017        | ARMv8.2       | Cortex-A55            | 32-bit/64-bit    | {% color(color="#ADFF2F") %} NEON (opt. SVE) {% end %} | {% color(color="#FF4136") %} No {% end %}  |
| 2018        | ARMv8.2       | Cortex-A76            | 32-bit/64-bit    | {% color(color="#ADFF2F") %} NEON (opt. SVE) {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2019        | ARMv8.2       | Cortex-A77            | 32-bit/64-bit    | {% color(color="#ADFF2F") %} NEON (opt. SVE) {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2019        | ARMv8.2       | Cortex-A65            | 32-bit/64-bit    | {% color(color="#ADFF2F") %} NEON (opt. SVE) {% end %} | {% color(color="#FF4136") %} No {% end %}  |
| 2020        | ARMv8.2       | Cortex-A78            | 32-bit/64-bit    | {% color(color="#ADFF2F") %} NEON (opt. SVE) {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2020        | ARMv8.2       | Cortex-X1             | 32-bit/64-bit    | {% color(color="#ADFF2F") %} NEON (opt. SVE) {% end %} | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2021        | ARMv9         | Cortex-A710           | 32-bit/64-bit    | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2021        | ARMv9         | Cortex-A510           | 32-bit/64-bit    | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#FF4136") %} No {% end %}  |
| 2021        | ARMv9         | Cortex-X2             | 32-bit/64-bit    | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2022        | ARMv9         | Cortex-A715           | 64-bit           | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2022        | ARMv9         | Cortex-X3             | 64-bit           | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2023        | ARMv9.2       | Cortex-A520           | 64-bit           | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#FF4136") %} No {% end %}  |
| 2023        | ARMv9.2       | Cortex-A720           | 64-bit           | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2023        | ARMv9.2       | Cortex-X4             | 64-bit           | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2024        | ARMv9.2       | Cortex-A725           | 64-bit           | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2024        | ARMv9.2       | Cortex-X925           | 64-bit           | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |
| 2024/2025 ? | ARMv9.2       | Cortex-X930           | 64-bit           | {% color(color="#1AC7FF") %} SVE2 {% end %}            | {% color(color="#1AC7FF") %} Yes {% end %} |

*Note: Implementation can very by vendor, some may support additional features or optimizations.*

## Benchmark

### PassMark

{{ img(src="/images/articles/benchmark/cpu_performance_st.webp" class="b1" alt="" loading="lazy" caption="PassMark score from 2000 to 2025 in single-thread" link="") }}

{{ img(src="/images/articles/benchmark/cpu_performance_mt.webp" class="b1" alt="" loading="lazy" caption="PassMark score from 2000 to 2025 in multi-thread" link="") }}
