+++
title = "A guide to SFF PCs (Draft)"
description = "A guide to SFF PCs"
date = 2025-02-19T00:00:00Z
draft = false

[taxonomies]
tags = ["Features","SFF","Tiny","Thinkcentre"]
categories = ["Hardware"]
[extra]
keywords = "SFF, Tiny, Embed, Embedded, Streamable"
toc = true
series = "Features"
+++

## A Guide to SFF PCs

Welcome to the guide to SFF PCs.

## Introduction to SFF PCs

In this section, we will explore different aspects of SFF PCs, including their components and software, with a focus on **Linux** and **open-source** solutions.

### What is an SFF PC?

An SFF PC is a **Small Form Factor PC**. It is usually very compact, power-efficient, and can be used for various purposes. They are commonly found in schools, offices, and home servers.

### Why should I choose an SFF PC?

There are many reasons to choose an SFF PC:

- **Compact**: SFF PCs are very small and can fit almost anywhere (~1-3 liters).
- **Power-efficient**: They consume less power, especially models with T or U series processors.
- **Affordable**: SFF PCs are often cheaper than traditional desktop PCs, especially on the second-hand market.

### Why shouldn't I choose an SFF PC?

There are also some drawbacks to consider:

- **Limited upgradeability**: Many SFF PCs have limited upgrade options, and some components are not replaceable.
- **Fewer ports**: Compared to larger desktops, SFF PCs typically have fewer connectivity options.
- **Performance constraints**: Due to their small size and thermal limitations, performance may be lower than full-sized PCs.
- **Proprietary components**: Some models use proprietary parts, making repairs and upgrades more difficult.

### What are some examples of SFF PCs?

Here are some well-known brands and models:

- **Lenovo ThinkCentre**: M73 Tiny, M710q, M720q, M70q G1, M75q G1, M90q G3, etc.
- **Dell OptiPlex**: 3040, 3050, 3060, 3070, 5040, 5050, 5060, 5070, etc.
- **HP EliteDesk**: 800 G1 Mini, 800 G2 Mini, etc.
- **Intel NUC**: NUC6i3SYH, NUC6i5SYH, NUC6i7KYK, NUC7i3BNH, NUC7i5BNH, NUC7i7BNH, etc.
- **Zotac ZBOX**: CI660 Nano, CI640 Nano, CI620 Nano, CI540 Nano, CI520 Nano, CI327 Nano, etc.
- **Asus VivoMini**: UN65, UN65U, UN65U-M023M, UN65U-M021M, UN65U-M022M, UN65U-M020M, etc.

Many other brands and models are available on the market.

For second-hand options, I recommend **Lenovo, Dell, and HP**. These brands offer plenty of affordable models that are often upgradable (RAM, SSD, CPU, PSU).

### ARM SFF PCs

SFF PCs are usually x86-based, but ARM-based SFF PCs have been gaining popularity in recent years. They are generally cheaper and more power-efficient but come with limitations:

- **Limited software compatibility**: They are not compatible with traditional x86/PC software.
- **Limited upgrade options**: Components are often soldered and non-replaceable.
- **Lower performance**: Compared to x86 counterparts, ARM-based SFF PCs may struggle with demanding tasks.

In this guide, we will focus on x86 SFF PCs and the Raspberry Pi.

## SFF PC Components

In this section, we will look at the key components of SFF PCs.

### CPU (Central Processing Unit)

I recommend using **socketed CPUs**, as they allow for future upgrades to more powerful models (within the same TDP range). For example, you can upgrade from an **Intel Celeron G4900T** to an **Intel i9-9900T** without any issues.

Most SFF PCs come with **35W or 65W CPUs**. **I strongly recommend avoiding CPUs with a higher TDP than what the system supports**, as this can cause overheating and potentially damage the motherboard or PSU.

Most modern software utilizes **AVX and AVX2** instructions, which can significantly boost performance in tasks like video encoding/decoding, compression, encryption, etc. Every CPU since **Intel Haswell** and **AMD Zen** supports AVX2, except for some low-end models like **Intel Celeron/Pentium** and **AMD Athlon**.

| Brand | CPU arch     | CPU Gen     | Socket  | RAM Type  | Max RAM | Year      | Exemple of SSF PC | Remarks                                                                   |
| ----- | ------------ | ----------- | ------- | --------- | ------- | --------- | ----------------- | ------------------------------------------------------------------------- |
| intel | Merom        | Core 2      | LGA775  | DDR2-DDR3 | 8GB     | 2006-2007 |                   | Huge performance improvement over Netburst                                |
| intel | Penryn       | Core 2      | LGA775  | DDR2-DDR3 | 8GB     | 2007-2008 |                   | Better perf efficiency                                                    |
| intel | Nehalem      | 1st Gen     | LGA1156 | DDR3      | 16GB    | 2008-2009 |                   | SMT, Memory controller on CPU and monolithic quad-core                    |
| intel | Westmere     | 1st Gen     | LGA1156 | DDR3      | 16GB    | 2010-2011 |                   | Better perf efficiency                                                    |
| intel | Sandy Bridge | 2nd Gen     | LGA1155 | DDR3      | 32GB    | 2011-2012 | M72 tiny          | Add AVX support, good iGPU and greatly improve perf                       |
| intel | Ivy Bridge   | 3rd Gen     | LGA1155 | DDR3      | 32GB    | 2012-2013 | M72 tiny          | Better perf efficiency                                                    |
| intel | Haswell      | 4th Gen     | LGA1150 | DDR3      | 32GB    | 2013-2014 | M73 tiny          | Support AVX2 and FMA3, improve perf                                       |
| intel | Broadwell    | 5th Gen     | LGA1150 | DDR3      | 32GB    | 2014-2015 |                   | Better perf efficiency                                                    |
| intel | Skylake      | 6th Gen     | LGA1151 | DDR3-DDR4 | 64GB    | 2015-2016 | M710q             | HEVC/VP9 8-bit hardware enc/dec, iGPU vulkan and NVMe support             |
| intel | Kaby Lake    | 7th Gen     | LGA1151 | DDR4      | 64GB    | 2016-2017 | M710q             | HEVC/VP9 10-bit hardware enc/dec support                                  |
| intel | Coffee Lake  | 8-9th Gen   | LGA1151 | DDR4      | 64GB    | 2017-2019 | M720q             | Increase core count and remove hyperthreading on 9th gen CPUs             |
| intel | Comet Lake   | 10th Gen    | LGA1200 | DDR4      | 128GB   | 2020-2021 | M70G gen 1        | Re-add hyperthreading on most CPUs                                        |
| intel | Rocket Lake  | 11th Gen    | LGA1200 | DDR4      | 128GB   | 2021-2022 | M70G gen 2        | Add AVX-512 support and better perf                                       |
| intel | Alder Lake   | 12th Gen    | LGA1700 | DDR4-DDR5 | 256GB   | 2021-2022 | M70G gen 3        | Remove AVX-512, Pcore and ECore, AV1 hardware dec support and improve IPC |
| intel | Raptor Lake  | 13-14th Gen | LGA1700 | DDR5      | 256GB   | 2022-2023 | M70G gen 4        |                                                                           |
| intel | Arrow Lake   | 15th Gen    | LGA1700 | DDR5      | 256GB   | 2023-2024 | M70G gen 5        | Remove SMT and greatly improve efficiency                                 |
| AMD   | Excavator    | 4th Gen     | AM4     | DDR4      | 32GB    | 2015-2016 |                   |                                                                           |
| AMD   | Zen          | 1st Gen     | AM4     | DDR4      | 64GB    | 2017-2018 | M715Q             | Huge performance improvement and on pair with intel Haswell CPUs          |
| AMD   | Zen+         | 2nd Gen     | AM4     | DDR4      | 64GB    | 2018-2019 |                   |                                                                           |
| AMD   | Zen 2        | 3rd Gen     | AM4     | DDR4      | 128GB   | 2019-2020 |                   | On pair with intel Skylake CPUs and fix most of the issues of Zen         |
| AMD   | Zen 3        | 4th Gen     | AM4     | DDR4      | 128GB   | 2020-2021 |                   | Improve IPC and power efficiency                                          |
| AMD   | Zen 4        | 5th Gen     | AM5     | DDR5      | 256GB   | 2021-2022 |                   | Add AVX-512 support, better IPC and RDNA iGPU                             |
| AMD   | Zen 5        | 6th Gen     | AM5     | DDR5      | 256GB   | 2022-2023 |                   | Slightly improve IPC                                                      |

## SFF PC Components

In this section, we will look at the key components of SFF PCs.

### CPU (Central Processing Unit)

I recommend using **Intel Coffee Lake**, **AMD Zen 2**, or newer CPUs, as they offer good performance and support modern features like NVMe, iGPU Vulkan, HEVC/VP9 10-bit hardware encoding/decoding, AVX2, etc. However, if you’re on a budget, **Haswell** or **Skylake** remains a good option due to the low price of the CPUs, DDR3 1600 MHz/DDR4 2400 MHz RAM, and relatively good performance.

### GPU (Graphics Processing Unit)

Most SFF PCs have only an integrated GPU. They are generally sufficient for light GPU tasks and consume very little power, making them great for home servers or office PCs.

Some SFF PCs can accommodate a dedicated GPU (such as the M720Q/M920Q). These are mostly low-profile and use PCIe x4/x8 lanes, which can be useful for light gaming, networking, etc. Ensure the PSU and motherboard can support the PCIe card's power consumption.

### RAM (Random Access Memory)

SFF PCs typically have **two RAM slots**, supporting DDR3, DDR4, or DDR5 RAM **depending on the CPU and motherboard**. The maximum capacity usually ranges from 16GB to 128GB. I recommend using **two identical RAM sticks**, as this improves stability and performance (dual-channel, doubling the bandwidth). You can use higher-frequency RAM than what the CPU officially supports; the RAM will simply downclock to the CPU-supported frequency.

Most SSF PCs support **SO-DIMM** (RAM in Laptop), which is smaller than standard DIMM RAM, but they have similar performances.

I recommend using **DDR4** or **DDR5** RAM, as it is the most common, well-supported, and cost-effective option. Here are some general recommendations (in 2025):

- **4GB**: Barebones Linux server, light applications (small website hosting, router, NAS)  
- **8GB**: Light to medium applications (web browsing, office work, small servers)  
- **16GB**: Recommended for most use cases (gaming, basic game server, CI build server, light development)  
- **32GB+**: Optimal for multitasking (AAA gaming, video/photo editing, rendering)  
- **64GB+**: Heavy multitasking (virtualization, machine learning, scientific computing, CAD)  

### Storage

SFF PCs have **four main storage options** (depending on the model):

- **M.2 NVMe SSD**: Very fast and present in most SFF PCs since 2015; the best choice.
- **M.2 SATA SSD**: Uses the same connector as NVMe but operates at SATA speeds (e.g., ThinkCentre M700).
- **2.5" SATA SSD**: Slower than M.2 NVMe but a good alternative if M.2 is unavailable.
- **2.5" SATA HDD**: Very slow and generally not recommended, but can be replaced with an SSD.
- **Onboard eMMC**: Soldered storage on the motherboard **avoid it** as it is slow, limited, and non-replaceable if it fails.

I recommend using **M.2 NVMe SSDs**. Be mindful of the size (2242, 2260, 2280), connector type (B, M, B+M), and whether it's single- or double-sided.

### Ports

All SFF PCs have a limited number of ports. Ensure that your chosen SFF PC has enough ports for your needs. Some models support expansion cards for additional ports (e.g., the M720Q).

### PSU (Power Supply Unit)

Most SFF PCs use an **external power supply**, often with a proprietary connector. Here are general guidelines:

- **65W**: Sufficient for a 35W CPU.
- **90W**: Sufficient for a 65W CPU.
- **135W**: Required for a 65W CPU + 45W GPU.

Ensure the PSU can handle the total power consumption of the CPU and any expansion cards.

### Motherboard

Like the PSU, most SFF PCs have a **proprietary motherboard**. Sometimes, you can replace it with another model from the same brand (e.g., an M920Q motherboard in an M720Q). However, in most cases, it is best to stick with the original motherboard model.

## Lenovo thinkcentre SSF PCs

In this section, we will see the different models of Lenovo thinkcentre SSF PCs.

| Model      | CPU               | Chipset     | SODIMM RAM           | PCIe          | Drive                     | Remarks |
| ---------- | ----------------- | ----------- | -------------------- | ------------- | ------------------------- | ------- |
| M72 tiny   | ivy bridge        | Intel H61   | 2x 8GB 1600MHz DDR3  | No            | 1x 2.5" SATA              |         |
| M92 tiny   | ivy bridge        | Intel Q77   | 2x 8GB 1600MHz DDR3  | No            | 1x 2.5" SATA              |         |
| M73 tiny   | Haswell           | Intel H81   | 2x 8GB 1600MHz DDR3  | No            | 1x 2.5" SATA              |         |
| M83 tiny   | Haswell           | Intel Q85   | 2x 8GB 1600MHz DDR3  | No            | 1x 2.5" SATA              |         |
| M700q      | Skylake           | Intel B150  | 2x 32GB 2133MHz DDR4 | No            | 1x m.2 SATA, 1x 2.5" SATA |         |
| M900q      | Skylake           | Intel Q170  | 2x 32GB 2133MHz DDR4 | No            | 1x m.2 ?, 1x 2.5" SATA    |         |
| M710q      | Skylake/Kaby Lake | Intel B250  | 2x 32GB 2400MHz DDR4 | No            | 1x m.2 NVMe, 1x 2.5" SATA |         |
| M910q      | Skylake/Kaby Lake | Intel Q270  | 2x 32GB 2400MHz DDR4 | No            | 2x m.2 NVMe, 1x 2.5" SATA |         |
| M720q      | Coffee Lake       | Intel B360  | 2x 32GB 2666MHz DDR4 | PCIe x8 Gen 3 | 1x m.2 NVMe, 1x 2.5" SATA |         |
| M920q      | Coffee Lake       | Intel Q370  | 2x 32GB 2666MHz DDR4 | PCIe x8 Gen 3 | 1x m.2 NVMe, 1x 2.5" SATA |         |
| M920x      | Coffee Lake       | Intel Q370  | 2x 32GB 2666MHz DDR4 | PCIe x8 Gen 3 | 2x m.2 NVMe, 1x 2.5" SATA |         |
| P330       | Coffee Lake       | Intel Q370  | 2x 32GB 2666MHz DDR4 | PCIe x8 Gen 3 | 2x m.2 NVMe, 1x 2.5" SATA |         |
| M75q       | AMD Zen 2         | AMD Pro 500 | 2x 32GB 2933MHz DDR4 | No            | 1x m.2 NVMe, 1x 2.5" SATA |         |
| M75q Gen 2 | AMD Zen 3         | AMD Pro 500 | 2x 32GB 3200MHz DDR4 | No            | 1x m.2, 1x 2.5" SATA      |         |
| M70q       | Comet Lake        | Intel H470  | 2x 32GB 2933MHz DDR4 | No            | 1x m.2 NVMe, 1x 2.5" SATA |         |
| M80q       | Comet Lake        | Intel Q470  | 2x 32GB 2933MHz DDR4 | No            | 1x m.2 NVMe, 1x 2.5" SATA |         |
| M90q       | Comet Lake        | Intel Q470  | 2x 32GB 2933MHz DDR4 | PCIe x8 Gen 3 | 2x m.2 NVMe, 1x 2.5" SATA |         |
| P340       | Comet Lake        | Intel Q470  | 2x 32GB 2933MHz DDR4 | PCIe x8 Gen 3 | 2x m.2 NVMe, 1x 2.5" SATA |         |
| M70q Gen 2 | Rocket Lake       | Intel B560  | 2x 32GB 3200MHz DDR4 | No            | 1x m.2 NVMe, 1x 2.5" SATA |         |
| M90q Gen 2 | Rocket Lake       | Intel Q570  | 2x 32GB 3200MHz DDR4 | PCIe x8 Gen 3 | 2x m.2 NVMe, 1x 2.5" SATA |         |
| P350       | Rocket Lake       | Intel Q570  | 2x 32GB 3200MHz DDR4 | PCIe x8 Gen 3 | 2x m.2 NVMe, 1x 2.5" SATA |         |
| M80q Gen 3 | Alder Lake        | Intel Q670  | 2x 32GB 4800MHz DDR5 | No            | 2x m.2 NVMe, 1x 2.5" SATA |         |
| M90q Gen 3 | Alder Lake        | Intel Q670  | 2x 32GB 4800MHz DDR5 | PCIe x8 Gen 4 | 2x m.2 NVMe, 1x 2.5" SATA |         |
| P360       | Alder Lake        | Intel Q670  | 2x 32GB 4800MHz DDR5 | PCIe x8 Gen 4 | 2x m.2 NVMe, 1x 2.5" SATA |         |
| M70q Gen 3 | Alder Lake        | Intel Q670  | 2x 32GB 3200MHz DDR4 | No            | 2x m.2 NVMe, 1x 2.5" SATA |         |
| M75q Gen 5 | AMD Zen 4         | AMD Pro 600 | 2x 32GB 5200MHz DDR5 | No            | 1x m.2 NVMe, 1x 2.5" SATA |         |

## Sources

- [Project TinyMiniMicro](https://forums.servethehome.com/index.php?threads/lenovo-thinkcentre-thinkstation-tiny-project-tinyminimicro-reference-thread.34925/)
- [Tiny/Mini/Micro PC experiences](https://forums.servethehome.com/index.php?threads/tiny-mini-micro-pc-experiences.30230/)
- [Wikipedia](https://en.wikipedia.org/wiki/Small_form_factor)
- [cpu-world](https://www.cpu-world.com/)