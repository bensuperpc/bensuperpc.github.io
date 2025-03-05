+++
title = "CAN bus under Linux (WIP)"
description = "CAN bus"
date = 2025-02-01T00:00:00Z
draft = false
aliases = ["fr/tutorial/canbus"]

[taxonomies]
tags = ["Features","CAN", "bus"]
categories = ["Software", "Hardware"]
[extra]
keywords = "CAN, bus"
toc = true
series = "Features"
+++

# CAN bus

This page provides a brief overview of the CAN bus protocol and how to use it under Linux.

## Install tools for CAN bus

On debian/ubuntu based systems:

```bash
sudo apt install can-utils
```

On arch based systems (AUR package):

```bash
yay -S can-utils
```

From source: [can-utils](https://github.com/linux-can/can-utils)

## Setup virtual interfaces

Create a virtual CAN interface:

```bash
sudo ip link add can0 type vcan
```

Enable standard CAN interface:

```bash
sudo ip link set up can0
```

Enable CAN FD interface:

```bash
sudo ip link set up can0 mtu 72
```

## Setup hardware interfaces

Enable hardware CAN interface:

```bash
sudo ip link set up can0
```

Set standard CAN interface:

```bash
sudo ip link set can0 type can bitrate 125000
```

Set CAN FD interface:

```bash
sudo ip link set can0 type can bitrate 125000 dbitrate 5000000 fd on
```

## Remove hardware interfaces

To remove the hardware CAN interface:

```bash
sudo ip link set down can0
```

## Receiving data

To read received data from a CAN interface:

```bash
candump -cexdtA any
```

## Sending data

To send data to a CAN interface:

```bash
cansend can0 217#1234567890ABCDEF
```

For CAN FD frames:

```bash
cansend can0 112##01234567890ABCDEF
```

Or with extended data:

```bash
cansend can0 112##01234567890ABCDEF1234567890ABCDEF
```

For CAN FD and BRS (Baud Rate Switch):

```bash
cansend can0 112##11234567890ABCDEF
```

## Sources

- [CAN bus](https://en.wikipedia.org/wiki/CAN_bus)
- [can-util](https://github.com/linux-can/can-utils)
- [SocketCAN](https://en.wikipedia.org/wiki/SocketCAN)
- [CAN FD](https://en.wikipedia.org/wiki/CAN_FD)
- [SocketCAN on Linux](https://www.kernel.org/doc/html/latest/networking/can.html)