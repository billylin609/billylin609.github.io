---
title: "QNX Mobility"
category: "Resume"
author: "Yuchen Lin"
date: 2025-09-14
summary: "A coaxial swerve drive prototyped in 36 hours at Hack the North, teleoperated from an IMU over MQTT and run on QNX RTOS. Won the QNX hardware prize."
location: "Hack the North 2025, Waterloo, ON"
cover: "./figs/cover.jpg"
---

## What it is

A swerve drive built in 36 hours at [Hack the North 2025](https://devpost.com/software/canqnx),
where it won the QNX hardware prize among 100+ competing teams.

![The finished swerve platform, with the QNX prize boxes](figs/cover.jpg)

## How it was built

- Prototyped a swerve drive in 36 hours and won the QNX hardware prize among 100+ competing teams.
- Integrated coaxial swerve modules with [swervepy](https://github.com/EWall25/swervepy) for inverse kinematics control.
- Implemented IMU-based teleoperation via MQTT and use QNX RTOS to enable multi-threaded motor control
  ([ODrive-CAN](https://odrive-can-roxautomation-components-9f5f4b809336bc0ecbd5b8cd8e4.gitlab.io/))
  and kinematics computation (swervepy).

![CAD of the coaxial swerve module layout](figs/shot-2.jpg)
