+++
title = "Benchmarking Webp format (WIP)"
description = "Benchmarking Webp format"
date = 2025-02-16T00:00:00Z
draft = false
aliases = ["fr/benchmark/webp"]

[taxonomies]
tags = ["Features","Benchmarking","avif","webp","png","jpegxl","Format"]
categories = ["Software"]
[extra]
keywords = "Webp, Benchmarking, avif, webp, png, jpegxl"
toc = true
series = "Features"
+++

# Introduction

Webp is a image format created by Google in early 2010's, in this article, we will benchmark it against others lossless formats like avif, png, jpegxl.

The benchmark is done using the **PNG** format as input, and the output formats are **Webp**, **Avif**, and **JpegXL**.

## Setup

| Specification |                                                      Value                                                       |
| :-----------: | :--------------------------------------------------------------------------------------------------------------: |
|      CPU      |                                   AMD Ryzen 7 5700X 8c16t (3.4 GHz / 4.6 GHz)                                    |
|      GPU      |                                       NVIDIA GeForce RTX 3060 Ti 8GB GDDR6                                       |
|      RAM      |                                                64GB DDR4 3200MHz                                                 |
|      OS       |                                                     Manjaro                                                      |
|   Compiler    |                                                    GCC 14.2.1                                                    |
|     cwebp     |                          [1.5.0](https://archlinux.org/packages/extra/x86_64/libwebp/)                           |
|    avifenc    |                          [1.2.1](https://archlinux.org/packages/extra/x86_64/libavif/)                           |
|     cjxl      |                          [0.11.1](https://archlinux.org/packages/extra/x86_64/libjxl/)                           |
|    ffmpeg     |                           [7.1.1](https://archlinux.org/packages/extra/x86_64/ffmpeg/)                           |
| Docker Image  | [docker.io/bensuperpc/multimedia:1.0.0-archlinux-base-20250507](https://github.com/bensuperpc/docker-multimedia) |

## Lossless compression

The dataset for the **lossless** benchmark is:

- ~9940 screenshots (32'257 Mo) from Minecraft (720p to 1440p, some 2160p).
- ~10313 screenshots (42'247 Mo) from Fortnite, Battlefield, 7 Days to Die, and GTA V etc... (1080p to 1440p, some 2160p).
- ~5485 screenshots (2'572 Mo) from desktop applications (240p to 1440p).

The PNG to Webp lossless compression command is:

```bash
cwebp -quiet -metadata all -lossless -exact -z <Compression> <Input> -o <Output>
```

The options are:

- `-quiet`: Quiet mode.
- `-metadata all`: Copy all metadata.
- `-lossless`: Lossless compression.
- `-exact`: Use exact mode, keep invisible pixels.
- `-z <Compression>`: Compression level, from 0 to 9, 9 best compression.
- `-mt`: Use multi-threading (we don't use it for the benchmark, gnu parallel is used).
- `<Input>`: Input PNG file.
- `<Output>`: Output Webp file.

For PNG to Avif lossless compression:

```bash
avifenc --jobs 1 --lossless --speed <Compression> --codec <codec> <Input> --output <Output>
```

The options are:

- `--lossless`: Lossless compression.
- `--speed <Compression>`: Compression level, from 0 to 9, 9 best compression.
- `--jobs 1`: Number of jobs.
- `--codec`: Use the *aom* codec, only codec available for lossless compression (11-2024).
- `<Input>`: Input PNG file.
- `<Output>`: Output Avif file.

For PNG to JPGXL lossless compression:

```bash
cjxl --num_threads 1 --quiet --effort <Compression> --distance 0.0 --brotli_effort 11 <Input> <Output>
```

The options are:

- `--quiet`: Quiet mode.
- `--num_threads 1`: Number of threads.
- `--effort <Compression>`: Compression level, from 0 to 9, 9 best compression.
- `--distance 0.0`: The quality, 0.0 is "mathematically lossless".
- `--brotli_effort 11`: Brotli compression level, 11 best compression.
- `<Input>`: Input PNG file.
- `<Output>`: Output JPGXL file.

## Results

Desktop applications (901 Mo):

| Format | Compression | Size (Mo) | Ratio (%) | Time (s) |
| :----: | :---------: | :-------: | :-------: | :------: |
|  png   |      -      |    901    |   100.0   |    -     |
|  webp  |      0      |    879    |   97.5    |   150    |
|  webp  |      1      |    660    |   72.2    |   176    |
|  webp  |      2      |    637    |   70.7    |   178    |
|  webp  |      3      |    602    |   66.8    |   181    |
|  webp  |      4      |    601    |   66.7    |   185    |
|  webp  |      5      |    598    |   66.3    |   198    |
|  webp  |      6      |    588    |   65.2    |   206    |
|  webp  |      7      |    585    |   64.9    |   211    |
|  webp  |      8      |    575    |   63.8    |   283    |
|  webp  |      9      |    560    |   62.1    |   1017   |
| jpegxl |      1      |    956    |   106.1   |   215    |
| jpegxl |      2      |    900    |   99.8    |   261    |
| jpegxl |      3      |    848    |   94.1    |   492    |
| jpegxl |      4      |    778    |   86.3    |   735    |
| jpegxl |      5      |    659    |   73.1    |   713    |
| jpegxl |      6      |    640    |   71.0    |   762    |
| jpegxl |      7      |    604    |   67.0    |   780    |
| jpegxl |      8      |    579    |   64.2    |   1407   |
| jpegxl |      9      |    569    |   63.1    |   2450   |

## Cleanup

```bash
find . -type f -name "*.webp" -delete
```

## Sources

- [cWebp](https://developers.google.com/speed/webp/docs/cwebp)
- [Avif](https://aomediacodec.github.io/av1-avif/)
- [JpegXL](https://jpegxl.info/)
