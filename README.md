# Cai Install - Fluent Design

一个基于 Fluent Design 的现代化安装工具，提供美观的用户界面和便捷的操作体验。

截图

![](https://pub-141831e61e69445289222976a15b6fb3.r2.dev/Image_to_url_V2/-----2026-03-08-205522-imagetourl.cloud-1772974532411-ol1cg2.png)

![](https://pub-141831e61e69445289222976a15b6fb3.r2.dev/Image_to_url_V2/-----2026-03-08-205522-imagetourl.cloud-1772974601928-3higep.png)

![https://pub-141831e61e69445289222976a15b6fb3.r2.dev/Image_to_url_V2/-----2026-03-08-205522-imagetourl.cloud-1772974647358-0kx1je.png](https://pub-141831e61e69445289222976a15b6fb3.r2.dev/Image_to_url_V2/-----2026-03-08-205522-imagetourl.cloud-1772974647358-0kx1je.png)



[English Version](./README_EN.md)

## 功能特点

- ✨ 现代化的 Fluent Design 界面
- 🚀 快速安装和配置
- 🌍 支持中国镜像加速
- 🛠️ 内置冲突包清理功能
- 📦 一键运行程序

## 系统要求

- Windows 10/11 操作系统
- Python 3.8 或更高版本
- 互联网连接（用于下载依赖）

## 快速开始

### 1. 安装依赖

运行 `cai_install_fluent.bat` 脚本，选择适合你的安装方式：

- **标准源**：适合网络环境良好的用户
- **中国镜像**：适合中国大陆用户，使用清华大学镜像加速

### 2. 运行程序

安装完成后，在同一个脚本中选择「运行程序」选项，即可启动 Fluent Design 版本的安装工具。

## 使用指南

### 主菜单选项

1. **安装依赖 (标准源)** - 使用默认 PyPI 源安装依赖
2. **安装依赖 (中国镜像)** - 使用清华大学镜像安装依赖，适合中国大陆用户
3. **清理冲突包** - 清理可能存在的 Fluent Widgets 冲突包
4. **运行程序** - 启动 Fluent Design 版本的安装工具
5. **退出** - 退出脚本

### 常见问题

#### Python 未找到

- 请下载并安装 Python 3.8 或更高版本
- 下载地址：https://www.python.org/downloads/
- 安装时请勾选「Add Python to PATH」选项

#### 安装失败

- 检查网络连接是否正常
- 尝试使用「中国镜像」安装选项
- 手动安装依赖：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt6 PyQt6-Fluent-Widgets qasync`

#### 程序启动失败

- 确保所有依赖已正确安装
- 检查 Python 环境是否正常
- 尝试使用「清理冲突包」功能后重新安装

## 项目结构

```
Cai-install-Fluent/
├── static/         # 静态资源文件
├── templates/      # HTML 模板文件
├── app.py          # 主应用程序
├── backend.py      # 后端逻辑
├── fluent_app.py   # Fluent 版本入口
├── requirements_fluent.txt  # 依赖文件
└── cai_install_fluent.bat   # 综合工具脚本
```

## 技术栈

- Python 3.8+
- PyQt6
- PyQt6-Fluent-Widgets
- qasync
- 其他依赖详见 requirements_fluent.txt

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。

## 许可证

本项目采用 MIT 许可证。

---

**注意**：本工具仅供学习和开发使用，请遵守相关软件的使用条款。
