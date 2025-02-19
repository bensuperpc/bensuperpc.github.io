+++
title = "Mesa GPU drivers"
description = "Mesa GPU drivers"
date = 2025-02-21T00:00:00Z
draft = false

[taxonomies]
tags = ["Features","GPU","Mesa","Drivers"]
[extra]
keywords = "Mesa, GPU, Drivers"
toc = true
series = "Features"
+++

## Introduction

You can find below a list of GPU architectures and their corresponding Mesa drivers and API support.

## AMD Graphics

| **GFX Core** | **Architecture**  | **Engineering Names**                                                                                 | **Shader Model** | **DirectX** | **OpenGL** | **OpenCL** | **Vulkan** |
| ------------ | ----------------- | ----------------------------------------------------------------------------------------------------- | ---------------- | ----------- | ---------- | ---------- | ---------- |
| GFX1         |                   | R100, RV100, RV200, RS100, RS200                                                                      | N/A              | 7           | 1.3        | N/A        | N/A        |
| GFX1         |                   | R200, RV250, RV280, RS300                                                                             | 1                | 8           | 1.4        | N/A        | N/A        |
| GFX2         |                   | R300, R350, RV350, RV380, RS400, RS480                                                                | 2                | 9           | 2.1        | N/A        | N/A        |
| GFX2         |                   | R420, R423, RV410, RS600, RS690, RS740                                                                | 2                | 9           | 2.1        | N/A        | N/A        |
| GFX2         |                   | RV515, R520, RV530, RV560, RV570, R580                                                                | 3                | 9           | 2.1        | N/A        | N/A        |
| GFX3         | Ultra-Threaded SE | R600, RV610, RV630, RV620, RV635, RV670, RS780, RS880                                                 | 4                | 10          | 3.3        | N/A        | N/A        |
| GFX3         | TeraScale 1       | RV770, RV730, RV710, RV740                                                                            | 4                | 10          | 3.3        | N/A        | N/A        |
| GFX4         | TeraScale 2       | CEDAR, REDWOOD, JUNIPER, CYPRESS, PALM, SUMO, SUMO2, BARTS, TURKS, CAICOS                             | 5                | 11          | 4.x        | 2.1        | N/A        |
| GFX5         | TeraScale 3       | CAYMAN, ARUBA (Trinity/Richland)                                                                      | 5                | 11          | 4.x        | 2.1        | N/A        |
| GFX6         | GCN 1.0           | CAPE VERDE, PITCAIRN, TAHITI, OLAND, HAINAN                                                           | 5                | 12          | 4.x        | 2.1        | 1.2        |
| GFX7         | GCN 2.0           | BONAIRE, KABINI, MULLINS, KAVERI, HAWAII                                                              | 5                | 12          | 4.x        | 2.1        | 1.2        |
| GFX8         | GCN 3.0           | VOLCANIC/PIRATE ISLANDS                                                                               | 5                | 12          | 4.x        | 2.1        | 1.2        |
| GFX8.1       | GCN 4.0           | TONGA, ICELAND/TOPAZ, CARRIZO, FIJI, STONEY, POLARIS10, POLARIS11, POLARIS12, VEGAM                   | 6                | 12          | 4.x        | 2.1        | 1.4        |
| GFX9         | GCN 5.0           | VEGA10, VEGA12, VEGA20, RAVEN, RENOIR                                                                 | 6                | 12          | 4.x        | 2.1        | 1.4        |
| GFX10        | RDNA 1.0          | NAVI10, NAVI12, NAVI14                                                                                | 6                | 12          | 4.x        | 2.1        | 1.4        |
| GFX10        | RDNA 2.0          | SIENNA CICHLID, NAVY FLOUNDER, DIMGREY CAVEFISH, BEIGE GOBY, YELLOW CARP, VANGOGH, RAPHAEL, MENDOCINO | 6                | 12          | 4.x        | 2.1        | 1.4        |
| GFX11        | RDNA 3.0          | NAVI31, NAVI32, NAVI33, PHOENIX                                                                       | 6                | 12          | 4.x        | 2.1        | 1.4        |
| GFX11        | RDNA 3.5          | STRIX                                                                                                 | 6                | 12          | 4.x        | 2.1        | 1.4        |

### Mesa drivers

| **Driver name** | **Type** | **Version**   | **GFX Core** |
| --------------- | -------- | ------------- | ------------ |
| r300            | OpenGL   | 1.5           | GFX2         |
| r600            | OpenGL   | 3.3           | GFX3-GFX5    |
| radeonsi        | OpenGL   | 4.6           | GFX6-GFX11   |
| radv            | Vulkan   | 1.4           | GFX6-GFX11   |

## Intel Graphics

| **GFX Core** | **Architecture**         | **Engineering Names**                                           | **Shader Model** | **DirectX** | **OpenGL** | **OpenCL** | **Vulkan** |
| ------------ | ------------------------ | --------------------------------------------------------------- | ---------------- | ----------- | ---------- | ---------- | ---------- |
| Gen1         | 3D Accelerator           | i740, i752, i754                                                | N/A              | 6           | 1.1        | N/A        | N/A        |
| Gen2         | Extreme Graphics         | 82810, 82815, 82845G, 82855GM, 82865G                           | N/A              | 7           | 1.3        | N/A        | N/A        |
| Gen3         | Extreme Graphics 2       | 82852GM, 82855GM, 82915G, 82925X                                | N/A              | 8           | 1.4        | N/A        | N/A        |
| Gen4         | GMA 3000/3100            | G965, Q965, X3000, X3100, G31, G33, G35, Q33, Q35               | 3                | 9           | 2.1        | N/A        | N/A        |
| Gen4.5       | GMA X3500/X4500          | G35, G41, G43, G45, Q43, Q45, B43, X38, X48                     | 4                | 10          | 2.1        | N/A        | N/A        |
| Gen5         | Ironlake                 | HD Graphics (Arrandale, Clarkdale)                              | 4                | 10          | 2.1        | N/A        | N/A        |
| Gen6         | Sandy Bridge             | HD Graphics 2000/3000                                           | 5                | 10.1        | 3.1        | 1.1        | N/A        |
| Gen7         | Ivy Bridge               | HD Graphics 2500/4000                                           | 5                | 11          | 4.x        | 1.2        | N/A        |
| Gen7.5       | Haswell                  | HD Graphics 4200/4400/4600/5000/5100/5200, Iris Pro 5200        | 5                | 11.1        | 4.x        | 1.2        | N/A        |
| Gen8         | Broadwell                | HD Graphics 5300/5500/6000, Iris 6100                           | 5                | 12          | 4.x        | 2.0        | 1.0        |
| Gen9         | Skylake/Kaby Lake        | HD Graphics 510/515/520/530/630, Iris 540/550/580, Iris Pro 580 | 6                | 12          | 4.x        | 2.1        | 1.0        |
| Gen9.5       | Coffee Lake/Whiskey Lake | UHD Graphics 610/620/630, Iris Plus 640/650/655                 | 6                | 12          | 4.x        | 2.1        | 1.2        |
| Gen11        | Ice Lake                 | Iris Plus Graphics (G4, G7)                                     | 6                | 12          | 4.x        | 2.1        | 1.2        |
| Gen12        | Xe-LP                    | UHD Graphics (Rocket Lake), Iris Xe (Tiger Lake)                | 6                | 12          | 4.x        | 2.1        | 1.2        |
| Gen12.5      | Xe-HPG/Xe-HPC            | Arc Alchemist, Ponte Vecchio                                    | 6                | 12          | 4.x        | 3.0        | 1.3        |
| Gen12.7      | Xe2-HPG/Xe2-LPG          | Battlemage, Lunar Lake                                          | 6                | 12          | 4.x        | 3.0        | 1.3        |

### Mesa drivers

| **Driver name** | **Type** | **Version**   | **GFX Core** |
| --------------- | -------- | ------------- | ------------ |
| i915            | OpenGL   | 2.1           | Gen3         |
| crocus          | OpenGL   | 4.6           | Gen4-Gen7.5  |
| iris            | OpenGL   | 4.6           | Gen8-Gen12.7 |
| hasvk           | Vulkan   | 1.2 (partial) | Gen6-Gen8    |
| anv             | Vulkan   | 1.4           | Gen9-Gen12.7 |


## Nvidia Graphics

| **GFX Core** | **Architecture**  | **Engineering Names**                            | **Shader Model** | **DirectX** | **OpenGL** | **OpenCL** | **Vulkan** |
| ------------ | ----------------- | ------------------------------------------------ | ---------------- | ----------- | ---------- | ---------- | ---------- |
| NV1          | STG-2000          | NV1 (Diamond Edge 3D)                            | N/A              | 5           | 1.1        | N/A        | N/A        |
| NV2          |                   | Annulé                                           | N/A              | N/A         | N/A        | N/A        | N/A        |
| NV3          | RIVA 128          | NV3, RIVA 128, RIVA 128ZX                        | N/A              | 5           | 1.1        | N/A        | N/A        |
| NV4          | TNT               | RIVA TNT, TNT2, TNT2 Ultra, Vanta, M64           | N/A              | 6           | 1.2        | N/A        | N/A        |
| NV10         | GeForce 256       | GeForce 256, GeForce 2, Quadro                   | 1                | 7           | 1.3        | N/A        | N/A        |
| NV20         | GeForce 3         | GeForce 3, GeForce 4 Ti                          | 1.3              | 8           | 1.4        | N/A        | N/A        |
| NV30         | GeForce FX        | GeForce FX 5000 Series                           | 2.0              | 9           | 2.1        | N/A        | N/A        |
| NV40         | GeForce 6/7       | GeForce 6000/7000, Quadro FX                     | 3.0              | 9           | 2.1        | N/A        | N/A        |
| G80          | Tesla (1st Gen)   | GeForce 8000, 9000, 100, GTX 200                 | 4.0              | 10          | 3.3        | 1.1        | N/A        |
| GT200        | Tesla (2nd Gen)   | GeForce GTX 260, 280, 295                        | 4.0              | 10          | 3.3        | 1.1        | N/A        |
| GF100        | Fermi             | GeForce GTX 400/500, Quadro 4000/5000/6000       | 5.0              | 11          | 4.x        | 1.1        | N/A        |
| GK100        | Kepler            | GeForce GTX 600/700, Quadro K-series             | 5.0              | 11          | 4.x        | 1.1        | N/A        |
| GM100        | Maxwell (1st Gen) | GeForce GTX 750/750 Ti                           | 5.0              | 12          | 4.x        | 1.2        | N/A        |
| GM200        | Maxwell (2nd Gen) | GeForce GTX 900, Quadro M-series                 | 5.0              | 12          | 4.x        | 1.2        | 1.1        |
| GP100        | Pascal            | GeForce GTX 10 Series, Titan Xp, Quadro P-series | 6.0              | 12          | 4.x        | 2.0        | 1.1        |
| TU100        | Turing            | GeForce RTX 20 Series, Quadro RTX                | 6.0              | 12          | 4.x        | 2.0        | 1.1        |
| GA100        | Ampere            | GeForce RTX 30 Series, Quadro RTX A-series       | 6.0              | 12          | 4.x        | 3.0        | 1.2        |
| AD100        | Ada Lovelace      | GeForce RTX 40 Series, RTX 6000 Ada              | 6.0              | 12          | 4.x        | 3.0        | 1.3        |
| GB100        | Blackwell         | GeForce RTX 50 Series (à venir)                  | 6.0              | 12          | 4.x        | 3.0        | 1.3        |

### Mesa drivers

| **Driver name** | **Type** | **Version** | **GFX Core** |
| --------------- | -------- | ----------- | ------------ |
| nv50            | OpenGL     | ?           | ?            |
| nvc0            | OpenGL     | ?           | ?            |
| nvk             | Vulkan     | ?           | ?            |


Source:
- [RadeonFeature](https://www.x.org/wiki/RadeonFeature/)
- [IntelGraphics](https://en.wikipedia.org/wiki/Intel_Graphics_Technology)
- [NvidiaGraphics](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units)
- [AMDGraphics](https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units)
- [Mesa Matrix](https://mesamatrix.net/)
- [Vulkan Hardware Database](https://vulkan.gpuinfo.org/)
- [Crocus](https://airlied.blogspot.com/2021/04/crocus-gallium-for-gen4-7-generation.html)
- [OpenGL Archlinux](https://wiki.archlinux.org/title/OpenGL)