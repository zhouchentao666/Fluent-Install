# Cai Install - Fluent Design

A modern installation tool based on Fluent Design, providing a beautiful user interface and convenient operation experience.

Pictures

截图

![](https://pub-141831e61e69445289222976a15b6fb3.r2.dev/Image_to_url_V2/-----2026-03-08-205522-imagetourl.cloud-1772974532411-ol1cg2.png)

![](https://pub-141831e61e69445289222976a15b6fb3.r2.dev/Image_to_url_V2/-----2026-03-08-205522-imagetourl.cloud-1772974601928-3higep.png)

![https//pub141831e61e69445289222976a15b6fb3r2dev/ImagetourlV2/20260308205522imagetourlcloud17729746473580kx1jepng](https://pub-141831e61e69445289222976a15b6fb3.r2.dev/Image_to_url_V2/-----2026-03-08-205522-imagetourl.cloud-1772974647358-0kx1je.png)

## Features

- ✨ Modern Fluent Design interface
- 🚀 Quick installation and configuration
- 🌍 Support for China mirror acceleration
- 🛠️ Built-in conflict package cleanup function
- 📦 One-click program launch

## System Requirements

- Windows 10/11 operating system
- Python 3.8 or higher
- Internet connection (for downloading dependencies)

## Quick Start

### 1. Install Dependencies

Run the `cai_install_fluent.bat` script and select the installation method that suits you:

- **Standard Source**: For users with good network environment
- **China Mirror**: For users in mainland China, using Tsinghua University mirror for acceleration

### 2. Run the Program

After installation, select the "Run Program" option in the same script to start the Fluent Design version of the installation tool.

## Usage Guide

### Main Menu Options

1. **Install Dependencies (Standard Source)** - Install dependencies using default PyPI source
2. **Install Dependencies (China Mirror)** - Install dependencies using Tsinghua University mirror, suitable for users in mainland China
3. **Cleanup Conflict Packages** - Clean up possible conflicting Fluent Widgets packages
4. **Run Program** - Start the Fluent Design version of the installation tool
5. **Exit** - Exit the script

### Common Issues

#### Python Not Found

- Please download and install Python 3.8 or higher
- Download address: https://www.python.org/downloads/
- Please check the "Add Python to PATH" option during installation

#### Installation Failed

- Check if the network connection is normal
- Try using the "China Mirror" installation option
- Manually install dependencies: `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt6 PyQt6-Fluent-Widgets qasync`

#### Program Startup Failed

- Ensure all dependencies are correctly installed
- Check if the Python environment is normal
- Try using the "Cleanup Conflict Packages" function and then reinstall

## Project Structure

```
Cai-install-Fluent/
├── static/         # Static resource files
├── templates/      # HTML template files
├── app.py          # Main application
├── backend.py      # Backend logic
├── fluent_app.py   # Fluent version entry
├── requirements_fluent.txt  # Dependency file
└── cai_install_fluent.bat   # Comprehensive tool script
```

## Technology Stack

- Python 3.8+
- PyQt6
- PyQt6-Fluent-Widgets
- qasync
- Other dependencies are detailed in requirements_fluent.txt

## Contribution

Welcome to submit Issues and Pull Requests to improve this project.

## License

This project is licensed under the MIT License.

---

**Note**: This tool is for learning and development purposes only. Please comply with the terms of use of related software.
