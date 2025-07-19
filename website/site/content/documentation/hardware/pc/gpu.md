+++
title = "Mesa GPU drivers"
description = "Mesa GPU drivers"
date = 2025-03-21T00:00:00Z
draft = false
aliases = ["en/documentation/hardware/pc/gpu/"]

[taxonomies]
tags = ["Features","GPU","Mesa","Drivers","AMD","Intel","Nvidia"]
categories = ["Hardware","Software"]
[extra]
keywords = "Mesa, GPU, Drivers, AMD, Intel, Nvidia"
toc = true
series = "Features"
+++


# Introduction

You can find below a list of GPU architectures and their corresponding Mesa drivers and API support.

## AMD Graphics

| **Release** | **GFX Core** | **Architecture**  | **GPU Models/Series**                                                       | **OpenGL** | **OpenCL** | **Vulkan** |
| ----------- | ------------ | ----------------- | --------------------------------------------------------------------------- | ---------- | ---------- | ---------- |
| 2000-2002   | GFX1         | -                 | Radeon 7xxx                                                                 | 1.3        | N/A        | N/A        |
| 2002-2004   | GFX1         | -                 | Radeon 8xxx, Radeon 9000, Radeon 9200, Radeon 9250                          | 1.4        | N/A        | N/A        |
| 2002-2005   | GFX2         | -                 | Radeon 9500, Radeon 9600, Radeon 9700, Radeon 9800, Radeon X300-X850        | 2.1        | N/A        | N/A        |
| 2004-2005   | GFX2         | -                 | Radeon X700, Radeon X800, Radeon X850, Radeon Xpress 200-1250               | 2.1        | N/A        | N/A        |
| 2005-2006   | GFX2         | -                 | Radeon X1300, Radeon X1600, Radeon X1800, Radeon X1900, Radeon X1950        | 2.1        | N/A        | N/A        |
| 2007-2008   | GFX3         | Ultra-Threaded SE | Radeon HD 2xxx, Radeon HD 3xxx                                              | 3.3        | N/A        | N/A        |
| 2008-2009   | GFX3         | TeraScale 1       | Radeon HD 4xxx                                                              | 3.3        | 1.1        | N/A        |
| 2009-2011   | GFX4         | TeraScale 2       | Radeon HD 5xxx, Radeon HD 6xxx                                              | 4.x        | 1.2        | N/A        |
| 2010-2012   | GFX5         | TeraScale 3       | Radeon HD 69xx, Radeon HD 7xxx (Trinity/Richland APUs)                      | 4.x        | 2.1        | N/A        |
| 2012-2013   | GFX6         | GCN 1.0           | Radeon HD 7xxx-8xxx, Radeon R7 240/250, Radeon R9 280/290                   | 4.x        | 2.1        | 1.2        |
| 2013-2014   | GFX7         | GCN 2.0           | Radeon R7 260, Radeon R9 290X, Radeon R9 295X2, Kaveri APUs                 | 4.x        | 2.1        | 1.2        |
| 2014-2015   | GFX8         | GCN 3.0           | Radeon R9 285, Radeon R9 380, Radeon R9 390                                 | 4.x        | 2.1        | 1.2        |
| 2015-2017   | GFX8.1       | GCN 4.0           | Radeon R9 Fury series, Radeon RX 4xx/5xx, Stoney Ridge APUs                 | 4.x        | 2.1        | 1.4        |
| 2017-2019   | GFX9         | GCN 5.0           | Radeon RX Vega 56/64, Radeon VII, Raven Ridge/Renoir APUs                   | 4.x        | 2.1        | 1.4        |
| 2019-2020   | GFX10        | RDNA 1.0          | Radeon RX 5xxx (Navi 10, Navi 12, Navi 14)                                  | 4.6        | 2.1        | 1.4        |
| 2020-2022   | GFX10        | RDNA 2.0          | Radeon RX 6xxx (Navi 21, Navi 22, Navi 23, Navi 24), Van Gogh, Raphael APUs | 4.6        | 2.1        | 1.4        |
| 2022-2024   | GFX11        | RDNA 3.0          | Radeon RX 7xxx (Navi 31, Navi 32, Navi 33), Phoenix APUs (780M, 760M)       | 4.6        | 2.1        | 1.4        |
| 2024        | GFX11        | RDNA 3.5          | Radeon RX 8xxM (Strix Point APUs)                                           | 4.6        | 2.1        | 1.4        |
| 2025        | GFX12        | RDNA 4.0          | Radeon RX 9xxx                                                              | 4.6        | 2.1        | 1.4        |

### Mesa drivers

| **Driver name**                                         | **Type** | **Version** | **GFX Core** |
| ------------------------------------------------------- | -------- | ----------- | ------------ |
| r200 ([mesa-amber](https://docs.mesa3d.org/amber.html)) | OpenGL   | 1.5         | GFX1         |
| r300                                                    | OpenGL   | 1.5         | GFX2         |
| r600                                                    | OpenGL   | 3.3         | GFX3-GFX5    |
| radeonsi                                                | OpenGL   | 4.6         | GFX6-GFX11   |
| radv                                                    | Vulkan   | 1.4         | GFX6-GFX11   |

## Intel Graphics

| **Release** | **GFX Core** | **Architecture**      | **GPU Models/Series**                             | **OpenGL** | **OpenCL** | **Vulkan** |
| ----------- | ------------ | --------------------- | ------------------------------------------------- | ---------- | ---------- | ---------- |
| 1998-1999   | Gen1         | 3D Accelerator        | i740, i752, i754                                  | 1.1        | N/A        | N/A        |
| 1999-2003   | Gen2         | Extreme Graphics      | 82810, 82815, 82845G, 82855GM, 82865G             | 1.3        | N/A        | N/A        |
| 2003-2004   | Gen3         | Extreme Graphics 2    | 82852GM, 82855GM, 82915G, 82925X                  | 1.4        | N/A        | N/A        |
| 2006-2007   | Gen4         | GMA 3000/3100         | G965, Q965, X3000, X3100, G31, G33, G35, Q33, Q35 | 2.1        | N/A        | N/A        |
| 2007-2009   | Gen4.5       | GMA X3500/X4500       | G35, G41, G43, G45, Q43, Q45, B43, X38, X48       | 2.1        | N/A        | N/A        |
| 2010        | Gen5         | Ironlake              | HD Graphics (Arrandale, Clarkdale)                | 2.1        | N/A        | N/A        |
| 2011        | Gen6         | Sandy Bridge          | HD Graphics 2000/3000                             | 3.1        | 1.1        | N/A        |
| 2012        | Gen7         | Ivy Bridge            | HD Graphics 2500/4000                             | 4.x        | 1.2        | N/A        |
| 2013        | Gen7.5       | Haswell               | HD Graphics 4200/4400/4600/5000/5100/5200         | 4.x        | 1.2        | N/A        |
| 2014-2015   | Gen8         | Broadwell             | HD Graphics 5300/5500/6000, Iris 6100             | 4.x        | 2.0        | 1.0        |
| 2015-2017   | Gen9         | Skylake               | HD Graphics 5xx, Iris 5xx                         | 4.6        | 2.1        | 1.4        |
| 2017-2019   | Gen9.5       | Kaby Lake/Coffee Lake | UHD Graphics 6xx, Iris Plus 6xx                   | 4.6        | 2.1        | 1.4        |
| 2019-2020   | Gen11        | Ice Lake              | Iris Plus Graphics (G4, G7)                       | 4.6        | 2.1        | 1.4        |
| 2020-2021   | Gen12        | Xe-LP                 | UHD Graphics (Rocket Lake), Iris Xe (Tiger Lake)  | 4.6        | 2.1        | 1.4        |
| 2022        | Gen12.7      | Xe-HPG/Xe-HPC         | Arc Alchemist (A7xx A3xx), Ponte Vecchio          | 4.6        | 3.0        | 1.4        |
| 2024-2025   | Gen20        | Xe2-HPG/Xe2-LPG       | Battlemage (B5xx), Lunar Lake                     | 4.6        | 3.0        | 1.4        |

### Mesa drivers

| **Driver name**                                              | **Type** | **Version**   | **GFX Core** |
| ------------------------------------------------------------ | -------- | ------------- | ------------ |
| i830/i965 ([mesa-amber](https://docs.mesa3d.org/amber.html)) | OpenGL   | 1.4           | Gen2         |
| i915                                                         | OpenGL   | 2.1           | Gen3         |
| crocus                                                       | OpenGL   | 4.6¹          | Gen4-Gen7.5  |
| iris                                                         | OpenGL   | 4.6           | Gen8-Gen20   |
| hasvk                                                        | Vulkan   | 1.0 (partial) | Gen6-Gen8    |
| anv                                                          | Vulkan   | 1.4           | Gen9-Gen20   |

**¹**: May vary depending on hardware.


## Nvidia Graphics

| **Release** | **GFX Core** | **Architecture**  | **GPU Models/Series**                         | **OpenGL** | **OpenCL** | **Vulkan** |
| ----------- | ------------ | ----------------- | --------------------------------------------- | ---------- | ---------- | ---------- |
| 1995        | NV1          | STG-2000          | NV1 (Diamond Edge 3D)                         | 1.1        | N/A        | N/A        |
| Cancelled   | NV2          |                   | Cancelled                                     | 1.1        | N/A        | N/A        |
| 1997        | NV3          | RIVA 128          | NV3, RIVA 128, RIVA 128ZX                     | 1.1        | N/A        | N/A        |
| 1998-1999   | NV4          | TNT               | RIVA TNT, TNT2, TNT2 Ultra, Vanta, M64        | 1.2        | N/A        | N/A        |
| 1999-2000   | NV10         | GeForce 256       | GeForce 256, GeForce 2, Quadro                | 1.3        | N/A        | N/A        |
| 2001-2002   | NV20         | GeForce 3         | GeForce 3, GeForce 4 Ti                       | 1.4        | N/A        | N/A        |
| 2003-2004   | NV30         | GeForce FX        | GeForce FX 5xx Series                         | 2.1        | N/A        | N/A        |
| 2004-2006   | NV40         | GeForce 6/7       | GeForce 6000/7000, Quadro FX                  | 2.1        | N/A        | N/A        |
| 2006-2008   | G80          | Tesla (1st Gen)   | GeForce 8000, 9xx, 1xx, GTX 2xx               | 3.3        | 1.1        | N/A        |
| 2008-2009   | GT200        | Tesla (2nd Gen)   | GeForce GTX 260, 280, 295                     | 3.3        | 1.1        | N/A        |
| 2010-2011   | GF100        | Fermi             | GeForce GT/GTX 4xx/5xx, Quadro 4000/5000/6000 | 4.x        | 1.1        | N/A        |
| 2012-2013   | GK100        | Kepler            | GeForce GT/GTX 6xx/7xx, Quadro K-series       | 4.x        | 1.1        | N/A        |
| 2014        | GM100        | Maxwell (1st Gen) | GeForce GTX 750/750 Ti, 8xx                   | 4.x        | 1.2        | N/A        |
| 2014-2015   | GM200        | Maxwell (2nd Gen) | GeForce GT/GTX 9xx, Quadro M-series           | 4.6        | 1.2        | 1.1        |
| 2016-2017   | GP100        | Pascal            | GeForce GTX 1xxx, Titan Xp, Quadro P-series   | 4.6        | 2.0        | 1.1        |
| 2018-2019   | TU100        | Turing            | GeForce RTX 2xxx, Quadro RTX                  | 4.6        | 2.0        | 1.1        |
| 2020-2021   | GA100        | Ampere            | GeForce RTX 3xxx, Quadro RTX A-series         | 4.6        | 3.0        | 1.2        |
| 2022-2023   | AD100        | Ada Lovelace      | GeForce RTX 4xxx,                             | 4.6        | 3.0        | 1.3        |
| 2025        | GB100        | Blackwell         | GeForce RTX 5xxx                              | 4.6        | 3.0        | 1.3        |

### Mesa drivers

| **Driver name** | **Type** | **Version** | **GFX Core** |
| --------------- | -------- | ----------- | ------------ |
| nv50            | OpenGL   | 3.3         | G80-GT200    |
| nvc0            | OpenGL   | 4.5         | GF100-?      |
| nvk             | Vulkan   | 1.4¹        | GK100-GB100  |

**¹**: May vary depending on hardware.

## Broadcom VideoCore

It is mainly used in Raspberry Pi.

| **Release** | **GFX Core**  | **Architecture** | **SOC Models/Series** | **OpenGL** | **OpenCL** | **Vulkan** |
| ----------- | ------------- | ---------------- | --------------------- | ---------- | ---------- | ---------- |
| 2012-2016   | VideoCore IV  | -                | BCM2835-BCM2837       | 2.x        | N/A        | N/A        |
| 2012-2016   | VideoCore VI  | -                | BCM2711B0             | 3.3        | N/A        | 1.0        |
| 2012-2016   | VideoCore VII | -                | BCM2712               | 3.3        | N/A        | 1.0        |

### Mesa drivers

| **Driver name** | **Type** | **Version** | **GFX Core**     |
| --------------- | -------- | ----------- | ---------------- |
| vc4             | OpenGL   | 2.1         | VideoCore IV     |
| v3d             | OpenGL   | 3.3         | VideoCore VI-VII |
| v3dv            | Vulkan   | 1.0         | VideoCore VI-VII |

Source:
- [RadeonFeature](https://www.x.org/wiki/RadeonFeature/)
- [IntelGraphics](https://en.wikipedia.org/wiki/Intel_Graphics_Technology)
- [NvidiaGraphics](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units)
- [AMDGraphics](https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units)
- [Mesa Matrix](https://mesamatrix.net/)
- [Vulkan Hardware Database](https://vulkan.gpuinfo.org/)
- [Crocus](https://airlied.blogspot.com/2021/04/crocus-gallium-for-gen4-7-generation.html)
- [OpenGL Archlinux](https://wiki.archlinux.org/title/OpenGL)
