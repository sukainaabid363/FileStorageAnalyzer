# File Storage Analyzer

## Project Overview
File Storage Analyzer is a simple Python-based utility that analyzes the storage usage of files inside a selected folder. It helps users understand how their storage is distributed and identify large files.

## Problem Statement
When a folder contains many files, it can be difficult to understand how much storage is being used and which file types occupy the most space. This project provides a simple solution by analyzing file sizes and generating a storage report.

## Features
- Counts the total number of files.
- Calculates total storage usage.
- Groups storage usage by file type.
- Displays the five largest files.
- Exports file details to a CSV report.
- Handles invalid folder paths.

## Technologies Used
- Python
- pathlib module
- csv module

## Requirements
- Python 3 installed on your computer.
- No external Python packages required.

## How to Run

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run the command:

```bash
python storage_analyzer.py
```

4. Enter the folder path when prompted.
5. Review the storage summary.
6. Choose whether to export a CSV report.

## Output
The program displays file details, total storage usage, storage grouped by file type, and the five largest files. It can also generate a CSV report.

## Course Relevance
This project demonstrates basic storage utilization analysis and data management concepts relevant to Information Storage and Management. It also relates to SDG 9: Industry, Innovation and Infrastructure.

## Future Enhancements
- Graphical user interface.
- Duplicate file detection.
- Storage usage charts.
- Improved report filtering.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
