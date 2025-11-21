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
|   Compiler    |                                                    GCC 15.2.1                                                    |
|     cwebp     |                          [1.6.0](https://archlinux.org/packages/extra/x86_64/libwebp/)                           |
|    avifenc    |                          [1.3.0](https://archlinux.org/packages/extra/x86_64/libavif/)                           |
|     cjxl      |                          [0.11.1](https://archlinux.org/packages/extra/x86_64/libjxl/)                           |
|    ffmpeg     |                           [8.0.1](https://archlinux.org/packages/extra/x86_64/ffmpeg/)                           |
| Docker Image  | [docker.io/bensuperpc/multimedia:1.0.0-archlinux-base-20260101](https://github.com/bensuperpc/docker-multimedia) |

## Lossless compression

The dataset for the **lossless** benchmark is:

- [SCD dataset](https://www.kaggle.com/datasets/awsaf49/scd-768x768-png-image-dataset) (7597 PNG images (768x768), 4.2 GB)
- [RSNA Breast Cancer dataset](https://www.kaggle.com/datasets/theoviel/rsna-breast-cancer-1024-pngs) (547000 PNG images (1024x1024), 13.62 GB)
- [CIFAR-10 dataset](https://www.kaggle.com/datasets/swaroopkml/cifar10-pngs-in-folders) (60000 PNG images (32x32), 135 MB)
- [Fashion MNIST dataset](https://www.kaggle.com/datasets/andhikawb/fashion-mnist-png) (70000 PNG images (28x28), 36 MB)

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

For the final command, we use GNU Parallel to speed up the process (for Webp):

```bash
time find . -iname "*.png" -type f -print0 | parallel --jobs 16 --null cwebp -quiet -metadata all -lossless -exact -z 9 {} -o {.}.webp
```

The CMD to get the size of the output files is:

```bash
find . -type f -iname "*.webp" -printf "%s\n" | awk '{sum+=$1} END {printf "%.2f MiB\n", sum/1024/1024}'
```

Where `{1}` is the compression level from 0 to 9.

## Results

For Ciphar-10:

| Format | Compression | Size (MiB) | Ratio (%) | Time (s) |
| :----: | :---------: | :-------: | :-------: | :------: |
|  png   |      -      |      |   100.0   |    -     |
|  webp  |      0      |        |       |   298    |
|  webp  |      1      |        |       |    299   |
|  webp  |      2      |        |       |    300   |
|  webp  |      3      |        |       |    302   |
|  webp  |      4      |        |       |    295   |
|  webp  |      5      |        |       |    291   |
|  webp  |      6      |        |       |    295   |
|  webp  |      7      |        |       |    293   |
|  webp  |      8      |        |       |   293    |
|  webp  |      9      |    103.29    |       |   286    |
| jpegxl |      1      |        |       |       |
| jpegxl |      2      |        |       |       |
| jpegxl |      3      |        |       |       |
| jpegxl |      4      |        |       |       |
| jpegxl |      5      |        |       |       |
| jpegxl |      6      |        |       |       |
| jpegxl |      7      |        |       |       |
| jpegxl |      8      |        |       |       |
| jpegxl |      9      |        |       |       |

## Cleanup

```bash
find . -type f -name "*.webp" -delete
```

## Sources

- [cWebp](https://developers.google.com/speed/webp/docs/cwebp)
- [Avif](https://aomediacodec.github.io/av1-avif/)
- [JpegXL](https://jpegxl.info/)
