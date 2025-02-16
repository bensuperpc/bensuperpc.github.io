+++
title = "Benchmarking Webp format"
description = "Benchmarking Webp format"
date = 2024-11-03T00:00:00Z
draft = false

[taxonomies]
tags = ["Features","Webp","Benchmarking","Avif","JPG","JPEG","PNG","Avif","JPGXL","JPEGXL","Format"]
[extra]
keywords = "Webp, Benchmarking, Avif, JPG, JPEG, PNG, Avif, JPGXL, JPEGXL, Format"
toc = true
series = "Features"
+++


## Introduction

In this article, we will benchmark the Webp against other formats like Avif, JPG, JPEG, PNG, Avif, JPGXL, and JPEGXL.

Webp is a modern image format created by Google, it support **lossy** and **lossless** compression, we will benchmark the lossy and lossless compression against other formats.

### Setup

| Specification |                        Value                        |
| :-----------: | :-------------------------------------------------: |
|      CPU      |     AMD Ryzen 7 5700X 8c16t (3.4 GHz / 4.6 GHz)     |
|      RAM      |                  64GB DDR4 3200MHz                  |
|      OS       |                     Arch Linux                      |
|   Compiler    |                     GCC 14.2.1                      |
|     cwebp     |                        [1.5.0](https://archlinux.org/packages/extra/x86_64/libwebp/)                        |
|    ffmpeg     |                        [7.1.0](https://archlinux.org/packages/extra/x86_64/ffmpeg/)                        |
| Docker Image  | bensuperpc/multimedia:archlinux-base-1.0.0-20250216 |

## Lossless compression


The dataset for the **lossless** benchmark is:

- 9900 screenshots from Minecraft (720p to 1440p).
- 9600 screenshots from Fortnite, Battlefield, 7 Days to Die, and GTA V (1080p to 1440p, some 2160p).
- 500 screenshots from desktop applications (1080p to 1440p).

The PNG to Webp lossless compression command is:

```bash
cwebp -quiet -metadata all -lossless -exact -z <Compression> -q <Compression> <Input> -o <Output>
```

The options are:

- `-quiet`: Quiet mode.
- `-metadata all`: Copy all metadata.
- `-lossless`: Lossless compression.
- `-exact`: Use exact mode, keep invisible pixels.
- `-z <Compression>`: Compression level, from 0 to 9, 9 best compression.
- `-q <Compression>`: Compression level, from 0 to 100, 100 best compression.
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

## Sources

- [cWebp](https://developers.google.com/speed/webp/docs/cwebp)
