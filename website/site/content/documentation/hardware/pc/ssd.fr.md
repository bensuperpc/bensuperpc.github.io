+++
title = "Comparison of SSDs"
description = "Comparison of SSDs"
date = 2025-02-23T00:00:00Z
draft = false
aliases = ["fr/documentation/hardware/pc/ssd/"]

[taxonomies]
tags = ["Features","SSD","NVMe","PCIe"]
categories = ["Hardware"]
[extra]
keywords = "SSD, NVMe, PCIe, Samsung, Western Digital"
toc = true
series = "Features"
+++

# Introduction

Une comparaison des SSDs de différentes marques et modèles.

## Samsung SSD NVMe

| **Modèle**           | **Release** | **NVMe** | **PCIe**      | **Consumption** | **Perfs R/W**    | **IOPS (R/W)** | **Capacity**    | **Memory type** | **TBW (1TB)** | **Memory**      |
| -------------------- | ----------- | -------- | ------------- | --------------- | ---------------- | -------------- | --------------- | --------------- | ------------- | --------------- |
| Samsung 950 Pro      | 2015        | 1.1      | 3.0 x4        | 5,7w / 0,03w    | 2.5 / 1.5 GB/s   | 300K / 110K    | 256 GB - 512 GB | MLC             | 800 TBW       | 0.5 GB LPDDR3   |
| Samsung 960 Evo      | 2016        | 1.2      | 3.0 x4        | 5,7w / 0,04w    | 3.2 / 1.9 GB/s   | 380K / 360K    | 256 GB - 1 To   | TLC             | 400 TBW       | 0.5-1 GB LPDDR3 |
| Samsung 960 Pro      | 2016        | 1.3      | 3.0 x4        | 5,7w / 0,04w    | 3.5 / 2.1 GB/s   | 500K / 450K    | 512 GB - 2 To   | MLC             | 800 TBW       | 0.5-2 GB LPDDR3 |
| Samsung 970 Evo      | 2018        | 1.3      | 3.0 x4        | 6w / 0,05w      | 3.5 / 2.5 GB/s   | 500K / 480K    | 256 GB - 2 TB   | TLC             | 600 TBW       | 0.5-2 GB LPDDR3 |
| Samsung 970 Evo Plus | 2021        | 1.3      | 3.0 x4        | 6w / 0,05w      | 3.5 / 3.3 GB/s   | 620K / 560K    | 256 GB - 2 TB   | TLC             | 600 TBW       | 0.5-2 GB LPDDR3 |
| Samsung 970 Pro      | 2018        | 1.3      | 3.0 x4        | 5,7w / 0,05w    | 3.5 / 3.3 GB/s   | 500K / 450K    | 512 GB - 1 TB   | MLC             | 1200 TBW      | 0.5-1 GB LPDDR3 |
| Samsung 980          | 2021        | 1.4      | 3.0 x4        | 4,6w / 0,05w    | 3.5 / 3.0 GB/s   | 500K / 480K    | 256 GB - 1 TB   | TLC             | 600 TBW       | -               |
| Samsung 980 Pro      | 2021        | 1.4      | 4.0 x4        | 6,2w / 0,05w    | 7.0 / 5.1 GB/s   | 1000K / 1000K  | 256 GB - 2 TB   | TLC             | 600 TBW       | 0.5-2 GB LPDDR3 |
| Samsung 990 Evo      | 2023        | 2.0      | 4.0 x4/5.0 x2 | 5,5w  / 0,05w   | 5.0 / 4.2 GB/s   | 700K / 800K    | 1 TB - 2 TB     | TLC             | 600 TBW       | -               |
| Samsung 990 Evo Plus | 2024        | 2.0      | 4.0 x4/5.0 x2 | 5,5w  / 0,05w   | 7.1 / 6.3 GB/s   | 850K / 1350K   | 1 TB - 4 TB     | TLC             | 600 TBW       | -               |
| Samsung 990 Pro      | 2022        | 2.0      | 4.0 x4        | 5,5w  / 0,05w   | 7.4 / 6.9 GB/s   | 1400K / 1500K  | 1 TB - 2 TB     | TLC             | 600 TBW       | 1-2 GB LPDDR4   |
| Samsung 9100 Pro     | 2025        | 2.0      | 5.0 x4        | 9w / 0.05w      | 14.8 / 13.4 GB/s | 2200K / 2600K  | 1 TB - 8 TB     | TLC             | 600 TBW       | 1-4 GB LPDDR4   |

## Western Digital SSD NVMe

| **Modèle** | **Release** | **NVMe** | **PCIe** | **Consumption** | **Perfs R/W**    | **IOPS (R/W)** | **Capacity**  | **Memory type** | **TBW (1TB)** | **Memory**    |
| ---------- | ----------- | -------- | -------- | --------------- | ---------------- | -------------- | ------------- | --------------- | ------------- | ------------- |
| WD SN750   | 2019        | 1.3      | 3.0 x4   | 5.8w / ?        | 5.1 / 4.9 GB/s   | 550K / 520K    | 256 GB - 4 TB | TLC             | 600 TBW       | 0.5-4 GB DDR4 |
| WD SN770   | 2022        | 1.4      | 4.0 x4   | 4.6w / ?        | 5.1 / 4.9 GB/s   | 740K / 800K    | 256 GB - 2 TB | TLC             | 600 TBW       | -             |
| WD SN850   | 2020        | 1.4      | 4.0 x4   | 7w / ?          | 7.0 / 5.1 GB/s   | 1000K / 770K   | 512 GB - 2 TB | TLC             | 600 TBW       | 0.5-2 GB DDR4 |
| WD SN850X  | 2022        | 1.4      | 4.0 x4   | 6,8w / ?        | 7.3 / 6.6 GB/s   | 1200K / 1200K  | 1 TB - 8 TB   | TLC             | 600 TBW       | 1-2 GB DDR4   |
| WD SN8100  | 2025        | 2.0      | 5.0 x4   | 7.0w / 0,05w    | 14.9 / 14.0 GB/s | 2300K / 2400K  | 1 TB - 4 TB   | TLC             | 600 TBW       | 1-4 GB DDR4   |

## Sources/Datasheets

- [Samsung 950 Pro](https://download.semiconductor.samsung.com/resources/data-sheet/Samsung_SSD_950_PRO_Data_Sheet_Rev_1_2.pdf)
- [Samsung 960 Pro/Evo](https://download.semiconductor.samsung.com/resources/brochure/NVMe_SSD_960_PRO_EVO_Brochure_Rev_1_1.pdf)
- [Samsung 970 Pro](https://download.semiconductor.samsung.com/resources/data-sheet/Samsung_NVMe_SSD_970_PRO_Data_Sheet_Rev.1.0.pdf)
- [Samsung 970 Evo](https://download.semiconductor.samsung.com/resources/data-sheet/Samsung-NVMe-SSD-970-EVO-Data-Sheet_Rev.1.0.pdf)
- [Samsung 970 Evo Plus](https://download.semiconductor.samsung.com/resources/data-sheet/Samsung_NVMe_SSD_970_EVO_Plus_Data_Sheet_Rev.3.0.pdf)
- [Samsung 980](https://download.semiconductor.samsung.com/resources/data-sheet/Samsung_NVMe_SSD_980_Data_Sheet_Rev.1.1.pdf)
- [Samsung 980 Pro](https://download.semiconductor.samsung.com/resources/data-sheet/Samsung-NVMe-SSD-980-PRO-Data-Sheet_Rev.2.1_230509_10129505081019.pdf)
- [Samsung 990 Evo](https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_evo_datasheet_rev.1.1.pdf)
- [Samsung 990 Evo Plus](https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_evo_plus_datasheet_rev.1.0.pdf)
- [Samsung 990 Pro](https://download.semiconductor.samsung.com/resources/data-sheet/Samsung_NVMe_SSD_990_PRO_Datasheet_Rev.1.0.pdf)
- [Samsung 9100 Pro](https://download.semiconductor.samsung.com/resources/data-sheet/Samsung_NVMe_SSD_9100_PRO_Datasheet_Rev.1.0.pdf)
- [Western Digital SN770](https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/internal-drives/wd-black-ssd/product-brief-wd-black-sn770-nvme-ssd.pdf)
- [Western Digital SN850](https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/internal-drives/wd-black-ssd/data-sheet-wd-black-sn850-nvme-ssd.pdf)
- [Western Digital SN850X](https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/internal-drives/wd-black-ssd/data-sheet-wd-black-sn850x-nvme-ssd.pdf)
- [Western Digital SN8100](https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/internal-drives/wd-black-ssd/data-sheet-wd-black-sn8100-nvme-ssd.pdf)
