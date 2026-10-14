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

> Counts are provided for reference, follow the script's counting rules, and do not indicate that every application has been tested.

<!-- software-stats:start -->
| Platform | Essential | Optional | Total |
| --- | --- | --- | --- |
| Windows | 4 | 22 | **26** |
| Linux | 14 | 8 | **22** |
| MacOS | 0 | 0 | **0** |
| General | 11 | 25 | **36** |
| Android | 0 | 7 | **7** |
| iOS | 0 | 0 | **0** |
<!-- software-stats:end -->

> Refresh stats (all entry points require Python 3.8 or newer):
>
> - Windows: double-click `scripts/count-software.bat`
> - Python: `python scripts/count-software.py` (use `python3` on Linux/macOS)
> - Bash: `bash scripts/count-software.sh`

Counts are summed exclusively from explicit `software-count` comments. Use `--dry-run --details` to view totals and per-file details, or `--check` to validate labels and README tables; neither mode modifies files. See the [Chinese script guide](scripts/README.md) for rules, entry points, and exit codes.

## Usage

1. Clone this repository locally or use it online.
2. Install the software you need.
3. Configure your environment.
4. Start using it.

## Contribution

If you are interested in this project, feel free to contribute your own software list, configuration tips, or documentation.

### Document Templates

See the [Chinese authoring guide](文档编写约定.md) for the current file inventory, directory layout, image paths, heading anchors, and counting rules. Choose a root-level template according to the document's purpose:

| Template | Intended content |
|---|---|
| [模板-单软件说明.md](模板-单软件说明.md) | Introduction, installation, usage, and related links for one application; retain only supported platforms. |
| [模板-多软件合集.md](模板-多软件合集.md) | A collection or comparison of related applications with brief documentation. |
| [模板-分类索引.md](模板-分类索引.md) | A `README.md` navigation page for a category or an application's resources. |
| [模板-配置专题.md](模板-配置专题.md) | Configuration, migration, backup, or troubleshooting topics. |

The templates are written in Chinese. After copying one, replace placeholders, adjust relative paths, remove inapplicable sections, and update the table of contents. The default title image for application introductions is the [placeholder image](.media/占位图片.png); calculate its path from the destination document's directory and replace it with a verified application icon when needed. Application introductions, collections, and topic guides include a table of contents by default; short indexes may omit it.

### Repository File Format Specification

**Organizational Principles:**

- Content should be placed under the corresponding platform directory (`Windows/`, `Linux/`, `MacOS/`, `General/`, `Android/`, or `iOS/`), and further categorized into `Essential/` (must-have) or `Optional/` (elective) subdirectories. If a piece of software supports multiple platforms but its primary use case is concentrated on one platform, it may be categorized under that platform's directory. For example, Spacedesk's host driver only supports Windows, so it belongs under `Windows/`.

- **Standalone software**: Create a `SoftwareName.md` file directly under the category directory — no folder is needed.  
  Example: `Linux/Optional/Distrobox容器软件.md`

- **Standalone software with supplementary assets** (configuration files, screenshots, etc.): Create a folder named after the software, and place the `.md` document together with the asset files inside it.  
  Example: `General/Essential/VScode/` contains `vs-code.md`, `vscode-settings.json`, etc.

- **Multiple related software** (each with substantial documentation): Create a folder named by function or purpose, with each piece of software having its own `.md` file. Such folders must include a `README.md` that lists the software covered in that category and provides navigation links to each individual document.  
  Example: `General/Optional/network-proxy/` contains `Clash-Verge.md`, `v2rayA.md`, etc., along with a `README.md` serving as the index.

- **Multiple related software** (each with brief documentation): They may be combined into a single Markdown file for comparative introduction. In this case, name the file by function or purpose (e.g., `FileEditing.md`, `RemoteConnection.md`) — again, no folder is needed.

- Application introductions are recommended to include the following; category indexes and configuration topics use their respective templates without requiring installation sections:
  - An opening table of contents matching the document's headings
  - A brief introduction to the software
  - Installation instructions
  - Usage (a brief explanation is sufficient)
  - Link to official documentation (if available)
  - Links to other related resources (tutorials, communities, etc.)
  - The default title image at `.media/占位图片.png`, with other media assets in the appropriate folder under `.media/`

- Add new documents to their category indexes and, where needed, parent `README.md` files. Update all references when moving or renaming files. Keep the Chinese and English root README bodies aligned; separate English copies of the templates are not required.

- Every application document must contain one `<!-- software-count: N -->` comment within its first 20 lines, preferably on the first line: use `1` for one application, the actual count for a collection, and `0` for configuration or non-application topics. The script does not infer counts from images, headings, or filenames. Unlabeled documents are not counted and block updates. `scripts/count-software.py` updates the section between the `software-stats` markers; do not edit the numbers manually.

- These templates establish conventions for new documents; existing documents are not reformatted in bulk. Preserve existing encoding and line endings where practical, and ignore `.obsidian/` in all operations.

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
