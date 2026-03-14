@echo off
chcp 65001
title Cai Install - Fluent Design Toolkit

:menu
echo ========================================
echo     Cai Install - Fluent Design Toolkit
echo ========================================
echo.
echo [1] 安装依赖 (标准源)
echo [2] 安装依赖 (中国镜像)
echo [3] 清理冲突包
echo.
echo [4] 运行程序
echo [5] 退出
echo.
set "choice="
set /p choice=请选择操作: 

rem 移除可能的空格
set "choice=%choice: =%"

rem 检查是否为空输入
if "%choice%"=="" (
    echo 请输入数字 1-5
echo.
    goto menu
)

rem 验证输入是否为有效数字
if "%choice%"=="1" goto install_standard
if "%choice%"=="2" goto install_china
if "%choice%"=="3" goto cleanup
if "%choice%"=="4" goto run
if "%choice%"=="5" goto exit

rem 如果执行到这里，说明输入无效
echo 无效选择，请输入数字 1-5
echo.
goto menu

:install_standard
echo ========================================
echo   安装 Cai Install Fluent 依赖
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 未找到 Python，请安装 Python 3.8+
    echo.
    echo 下载地址: https://www.python.org/downloads/
    pause
    goto menu
)

echo [INFO] Python 版本:
python --version
echo.

echo [INFO] 升级 pip...
python -m pip install --upgrade pip
echo.

echo [INFO] 清理冲突的 Fluent Widgets 包...
pip uninstall -y PyQt-Fluent-Widgets PyQt5-Fluent-Widgets PySide2-Fluent-Widgets PySide6-Fluent-Widgets >nul 2>&1
echo.

echo [INFO] 安装依赖...
echo.
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [ERROR] 安装失败!
    echo.
    echo 可能的解决方案:
    echo 1. 检查网络连接
    echo 2. 使用中国镜像: pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
    echo 3. 手动安装: pip install PyQt6 PyQt6-Fluent-Widgets qasync
    pause
    goto menu
)

echo.
echo ========================================
echo   安装完成!
echo ========================================
echo.
echo 现在可以选择 [4] 运行程序
echo.
pause
goto menu

:install_china
echo ========================================
echo   安装 Cai Install Fluent 依赖
    echo   使用清华大学镜像 (中国加速)
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 未找到 Python，请安装 Python 3.8+
    echo.
    echo 下载地址: https://www.python.org/downloads/
    pause
    goto menu
)

echo [INFO] Python 版本:
python --version
echo.

echo [INFO] 升级 pip...
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
echo.

echo [INFO] 清理冲突的 Fluent Widgets 包...
pip uninstall -y PyQt-Fluent-Widgets PyQt5-Fluent-Widgets PySide2-Fluent-Widgets PySide6-Fluent-Widgets >nul 2>&1
echo.

echo [INFO] 安装依赖 (使用清华大学镜像)...
echo.
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

if errorlevel 1 (
    echo.
    echo [ERROR] 安装失败!
    echo.
    echo 尝试手动安装核心包...
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt6 PyQt6-Fluent-Widgets qasync httpx aiofiles ujson colorlog vdf
    
    if errorlevel 1 (
        echo.
        echo [ERROR] 仍然失败，请检查网络或 Python 环境
        pause
        goto menu
    )
)

echo.
echo ========================================
echo   安装完成!
echo ========================================
echo.
echo 现在可以选择 [4] 运行程序
echo.
pause
goto menu

:cleanup
echo ========================================
echo   清理 Fluent Widgets 冲突
echo ========================================
echo.
echo 警告: 这将卸载所有 Fluent Widgets 包
echo 然后重新安装正确的 PyQt6-Fluent-Widgets
echo.
pause

echo.
echo [INFO] 卸载冲突包...
echo.

pip uninstall -y PyQt-Fluent-Widgets
pip uninstall -y PyQt5-Fluent-Widgets
pip uninstall -y PyQt6-Fluent-Widgets
pip uninstall -y PySide2-Fluent-Widgets
pip uninstall -y PySide6-Fluent-Widgets

echo.
echo [INFO] 清理完成，安装正确的包...
echo.

pip install PyQt6-Fluent-Widgets

if errorlevel 1 (
    echo.
    echo [ERROR] 安装失败，尝试使用中国镜像...
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt6-Fluent-Widgets
)

echo.
echo ========================================
echo   完成!
echo ========================================
echo.
echo 现在可以选择 [4] 运行程序
echo.
pause
goto menu

:run
echo ========================================
echo   Cai Install - Fluent Design 版本
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] 未找到 Python，请安装 Python 3.8+
    pause
    goto menu
)

echo [INFO] 检查依赖...
python -c "import qasync" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] 缺少依赖，自动安装...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo [ERROR] 依赖安装失败，请手动运行: pip install -r requirements.txt
        pause
        goto menu
    )
    echo.
    echo [SUCCESS] 依赖已安装
    echo.
)

echo [INFO] 启动 Fluent Design 版本...
echo.

python fluent_app.py

if errorlevel 1 (
    echo.
    echo [ERROR] 程序发生错误
    pause
)
goto menu

:exit
echo 感谢使用 Cai Install - Fluent Design Toolkit
echo 再见!
echo.
pause
exit /b 0