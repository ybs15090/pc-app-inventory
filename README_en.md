# PC Software Collection
[中文说明文档](README_zh.md)
## Overview

This repository contains a curated list of recommended software and tools for PC and mobile devices.

## [Windows](Windows/README.md)

A section for essential Windows applications and productivity tools.

## [Linux](Linux/README.md)

Currently focused on Ubuntu-related software and useful Linux utilities.

## [General](General/README.md)

General software and settings that work across platforms.

## [Android](Android/README.md)

Tools and apps for the Android system.

## [iOS](iOS/README.md)

Tools and apps for the iOS / iPadOS system.

## Software Count <!-- omit in toc -->

| Platform | Essential | Optional | Total |
|----------|-----------|----------|-------|
| Windows | 3 | 7 | **10** |
| Linux | 11 | 5 | **16** |
| MacOS | 0 | 0 | **0** |
| General | 6 | 9 | **15** |
| Android | 0 | 1 | **1** |
| iOS | 0 | 0 | **0** |

> Run `bash scripts/count-software.sh` to refresh stats.

## Usage

1. Clone this repository locally or use it online.
2. Install the software you need.
3. Configure your environment.
4. Start using it.

## Contribution

If you are interested in this project, feel free to contribute your own software list, configuration tips, or documentation.

### Repository File Format Specification

**Organizational Principles:**

- Content should be placed under the corresponding platform directory (`Windows/`, `Linux/`, `Mac/`, or `General/`), and further categorized into `Essential/` (must-have) or `Optional/` (elective) subdirectories. If a piece of software supports multiple platforms but its primary use case is concentrated on one platform, it may be categorized under that platform's directory. For example, Spacedesk's host driver only supports Windows, so it belongs under `Windows/`.

- **Standalone software**: Create a `SoftwareName.md` file directly under the category directory — no folder is needed.  
  Example: `Linux/Optional/Distrobox容器软件.md`

- **Standalone software with supplementary assets** (configuration files, screenshots, etc.): Create a folder named after the software, and place the `.md` document together with the asset files inside it.  
  Example: `General/Essential/VScode/` contains `vs-code.md`, `vscode-settings.json`, etc.

- **Multiple related software** (each with substantial documentation): Create a folder named by function or purpose, with each piece of software having its own `.md` file. Such folders must include a `README.md` that lists the software covered in that category and provides navigation links to each individual document.  
  Example: `General/Optional/network-proxy/` contains `Clash-Verge.md`, `v2rayA.md`, etc., along with a `README.md` serving as the index.

- **Multiple related software** (each with brief documentation): They may be combined into a single Markdown file for comparative introduction. In this case, name the file by function or purpose (e.g., `FileEditing.md`, `RemoteConnection.md`) — again, no folder is needed.

- Each Markdown file is recommended to include the following:
  - A brief introduction to the software
  - Installation instructions
  - Usage (a brief explanation is sufficient)
  - Link to official documentation (if available)
  - Links to other related resources (tutorials, communities, etc.)
  - If you want to include icons or other media assets, please place them in the corresponding folder under `.media/`

## Disclaimer

Not all software listed in this repository has been personally used by the maintainer. Some installation steps, usage instructions, and related information are compiled from online sources and **may not be fully accurate or up-to-date**. Before using any software, please:

- Refer to official documentation for installation and configuration details
- Evaluate the security and suitability of the software yourself
- Back up important data before making significant changes

If you find errors or outdated content, feedback via Issue, PR, or email is welcome.

## Contact

If you have any questions, please contact me at:

- Email: 
  - ybs15090@outlook.com
  - ybs15090@gmail.com


### [Back to README](README.md)