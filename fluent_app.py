"""
Cai Install - Fluent Design 版本
使用 PyQt-Fluent-Widgets 框架
"""
import sys
import asyncio
from pathlib import Path
from typing import Optional
from PyQt6.QtCore import Qt, QSize, pyqtSignal, QThread, pyqtSlot, QUrl, QLocale, QTranslator
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from qfluentwidgets import (
    FluentIcon, NavigationItemPosition, MessageBox,
    setTheme, Theme, setThemeColor, isDarkTheme,
    MSFluentWindow, NavigationAvatarWidget,
    SubtitleLabel, BodyLabel, PushButton, LineEdit,
    ComboBox, SwitchButton, ProgressRing, InfoBar,
    InfoBarPosition, CardWidget, ScrollArea, CaptionLabel,
    TransparentToolButton, IconWidget, FlowLayout, SearchLineEdit,
    PrimaryPushButton, CheckBox
)

# 导入后端
from backend import CaiBackend


# 语言配置
LANGUAGES = {
    "zh_CN": {
        "name": "简体中文",
        "locale": QLocale(QLocale.Language.Chinese, QLocale.Country.China)
    },
    "en_US": {
        "name": "English",
        "locale": QLocale(QLocale.Language.English, QLocale.Country.UnitedStates)
    }
}

def load_theme_config():
    """加载主题配置"""
    try:
        config_path = Path.cwd() / 'config.json'
        if config_path.exists():
            import json
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return {
                "theme_mode": config.get("theme_mode", "auto"),
                "theme_color": config.get("theme_color", "#0078d4")
            }
    except:
        pass
    return {"theme_mode": "auto", "theme_color": "#0078d4"}


def load_language_config():
    """加载语言配置"""
    try:
        config_path = Path.cwd() / 'config.json'
        if config_path.exists():
            import json
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config.get("language", "zh_CN")
    except:
        pass
    return "zh_CN"


# Simple text translation mapping
TEXTS = {
    "zh_CN": {
        "app_title": "Cai Install - Fluent",
        "home": "主页",
        "search": "搜索入库",
        "settings": "设置",
        "restart_steam": "重启 Steam",
        "installed_games": "已入库的游戏",
        "search_placeholder": "搜索游戏名称或 AppID",
        "loading": "加载中...",
        "no_games": "暂无游戏",
        "delete": "删除",
        "confirm_delete": "确认删除",
        "delete_message": "确定要删除 AppID {0} 吗？\n\n此操作不可撤销。",
        "deleting": "正在删除",
        "delete_success": "删除成功",
        "delete_failed": "删除失败",
        "search_and_add": "搜索并入库游戏",
        "game_name_or_appid": "输入游戏名称或 AppID / Steam 链接",
        "search_button": "搜索",
        "add_options": "入库选项",
        "add_all_dlc": "添加所有 DLC",
        "patch_depot_key": "修补 Depot Key",
        "manifest_source": "清单源:",
        "add_game": "入库游戏",
        "steam_path": "Steam 路径",
        "github_token": "GitHub Personal Token",
        "appearance": "外观",
        "theme_mode": "主题模式",
        "theme_color": "主题色",
        "language": "语言",
        "save_settings": "保存设置",
        "about": "关于",
        "thanks": "鸣谢",
        "restart_required": "需要重启",
        "language_changed": "语言已更改为 {0}\n\n是否立即重启应用以应用更改？",
        "restart_steam_confirm": "重启 Steam",
        "restart_steam_message": "确定要重启 Steam 吗？\n\n这将关闭当前运行的 Steam 并重新启动。",
        "total_games": "共 {0} 个游戏 | SteamTools: {1} | GreenLuma: {2}",
        "load_failed": "加载失败: {0}",
        "reset_settings": "重置设置",
        "reset_settings_message": "确定要将所有设置重置为默认值吗？\n\n此操作不可撤销。",
        "reset_success": "重置成功",
        "reset_success_message": "配置已重置为默认值，请重新加载页面",
        "reset_failed": "重置失败",
        "restarting": "正在重启",
        "restarting_message": "正在重启 Steam，请稍候...",
        "restart_success": "重启成功",
        "restart_success_message": "Steam 已重启",
        "restart_failed": "重启失败",
        "restart_failed_message": "重启 Steam 失败，请手动重启",
        "restart_error_message": "重启 Steam 时出错: {0}",
        "application_config": "应用程序配置",
        "debug_mode": "调试模式",
        "enable_debug_log": "启用详细的调试日志输出",
        "save_log_files": "保存日志文件",
        "save_logs_to_file": "将日志保存到文件中",
        "unlocker_mode": "解锁工具模式",
        "auto_detect": "自动检测",
        "force_steamtools": "强制 SteamTools",
        "force_greenluma": "强制 GreenLuma",
        "force_unlocker_hint": "强制使用指定的解锁工具",
        "light_theme": "浅色",
        "dark_theme": "深色",
        "follow_system": "跟随系统",
        "default_blue": "默认蓝 (#0078d4)",
        "purple": "紫色 (#9b4dca)",
        "green": "绿色 (#10893e)",
        "orange": "橙色 (#ff8c00)",
        "red": "红色 (#e81123)",
        "pink": "粉色 (#e3008c)",
        "tip_source_fail": "提示: 如果某个源失败，请尝试其他源",
        "auto_search_github": "自动搜索GitHub (推荐)",
        "swa_v2": "SWA V2",
        "cysaw": "Cysaw",
        "furcate": "Furcate",
        "walftech": "Walftech",
        "steamdatabase": "steamdatabase",
        "steamautocracks_v2": "SteamAutoCracks V2 (仅密钥)",
        "sudama": "Sudama库 (仅密钥)",
        "buqiuren": "清单不求人库 (仅清单)",
        "github_auiowu": "GitHub (Auiowu)",
        "github_sac": "GitHub (SAC)",
        "restart_steam_title": "重启 Steam",
        "restart_steam_confirm_message": "确定要重启 Steam 吗？\n\n这将关闭当前运行的 Steam 并重新启动。",
    },
    "en_US": {
        "app_title": "Cai Install - Fluent",
        "home": "Home",
        "search": "Search & Add",
        "settings": "Settings",
        "restart_steam": "Restart Steam",
        "installed_games": "Installed Games",
        "search_placeholder": "Search game name or AppID",
        "loading": "Loading...",
        "no_games": "No games",
        "delete": "Delete",
        "confirm_delete": "Confirm Delete",
        "delete_message": "Are you sure you want to delete AppID {0}?\n\nThis action cannot be undone.",
        "deleting": "Deleting",
        "delete_success": "Delete Success",
        "delete_failed": "Delete Failed",
        "search_and_add": "Search and Add Games",
        "game_name_or_appid": "Enter game name or AppID / Steam link",
        "search_button": "Search",
        "add_options": "Add Options",
        "add_all_dlc": "Add All DLC",
        "patch_depot_key": "Patch Depot Key",
        "manifest_source": "Manifest Source:",
        "add_game": "Add Game",
        "steam_path": "Steam Path",
        "github_token": "GitHub Personal Token",
        "appearance": "Appearance",
        "theme_mode": "Theme Mode",
        "theme_color": "Theme Color",
        "language": "Language",
        "save_settings": "Save Settings",
        "about": "About",
        "thanks": "Credits",
        "restart_required": "Restart Required",
        "language_changed": "Language changed to {0}\n\nRestart the application now to apply changes?",
        "restart_steam_confirm": "Restart Steam",
        "restart_steam_message": "Are you sure you want to restart Steam?\n\nThis will close the currently running Steam and restart it.",
        "total_games": "Total: {0} games | SteamTools: {1} | GreenLuma: {2}",
        "load_failed": "Load failed: {0}",
        "reset_settings": "Reset Settings",
        "reset_settings_message": "Are you sure you want to reset all settings to default?\n\nThis action cannot be undone.",
        "reset_success": "Reset Successful",
        "reset_success_message": "Settings have been reset to default, please reload the page",
        "reset_failed": "Reset Failed",
        "restarting": "Restarting",
        "restarting_message": "Restarting Steam, please wait...",
        "restart_success": "Restart Successful",
        "restart_success_message": "Steam has been restarted",
        "restart_failed": "Restart Failed",
        "restart_failed_message": "Failed to restart Steam, please restart manually",
        "restart_error_message": "Error restarting Steam: {0}",
        "application_config": "Application Configuration",
        "debug_mode": "Debug Mode",
        "enable_debug_log": "Enable detailed debug log output",
        "save_log_files": "Save Log Files",
        "save_logs_to_file": "Save logs to file",
        "unlocker_mode": "Unlocker Mode",
        "auto_detect": "Auto Detect",
        "force_steamtools": "Force SteamTools",
        "force_greenluma": "Force GreenLuma",
        "force_unlocker_hint": "Force use of specified unlocker",
        "light_theme": "Light",
        "dark_theme": "Dark",
        "follow_system": "Follow System",
        "default_blue": "Default Blue (#0078d4)",
        "purple": "Purple (#9b4dca)",
        "green": "Green (#10893e)",
        "orange": "Orange (#ff8c00)",
        "red": "Red (#e81123)",
        "pink": "Pink (#e3008c)",
        "tip_source_fail": "Tip: If one source fails, try another",
        "auto_search_github": "Auto Search GitHub (Recommended)",
        "swa_v2": "SWA V2",
        "cysaw": "Cysaw",
        "furcate": "Furcate",
        "walftech": "Walftech",
        "steamdatabase": "steamdatabase",
        "steamautocracks_v2": "SteamAutoCracks V2 (Keys Only)",
        "sudama": "Sudama Library (Keys Only)",
        "buqiuren": "Manifest Helper Library (Manifest Only)",
        "github_auiowu": "GitHub (Auiowu)",
        "github_sac": "GitHub (SAC)",
        "restart_steam_title": "Restart Steam",
        "restart_steam_confirm_message": "Are you sure you want to restart Steam?\n\nThis will close the currently running Steam and restart it.",
    }
}

# 全局语言变量
current_language = "zh_CN"

def tr(key, *args):
    """翻译函数"""
    text = TEXTS.get(current_language, TEXTS["zh_CN"]).get(key, key)
    if args:
        text = text.format(*args)
    return text

def set_language(lang):
    """设置当前语言"""
    global current_language
    if lang in TEXTS:
        current_language = lang


class GameCard(CardWidget):
    """游戏卡片组件"""
    
    def __init__(self, appid, game_name, source_type, parent=None):
        super().__init__(parent)
        self.appid = appid
        self.game_name = game_name
        self.source_type = source_type  # 'st' 或 'gl'
        
        # 网络管理器（先初始化）
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.on_cover_loaded)
        
        # 创建布局
        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()
        
        # 游戏封面
        self.coverLabel = QLabel(self)
        self.coverLabel.setFixedSize(120, 56)
        self.coverLabel.setScaledContents(True)
        self.coverLabel.setStyleSheet("border-radius: 4px; background: #2a2a2a;")
        
        # 游戏标题
        self.titleLabel = BodyLabel(game_name if game_name != "加载中..." else f"AppID: {appid}", self)
        self.titleLabel.setWordWrap(False)
        
        # AppID 和来源
        source_text = "SteamTools" if source_type == "st" else "GreenLuma"
        self.infoLabel = CaptionLabel(f"AppID: {appid} | {source_text}", self)
        self.infoLabel.setTextColor("#606060", "#d2d2d2")
        
        # 删除按钮
        self.deleteButton = TransparentToolButton(FluentIcon.DELETE, self)
        self.deleteButton.setFixedSize(32, 32)
        self.deleteButton.setToolTip(tr("delete"))
        self.deleteButton.clicked.connect(self.on_delete_clicked)
        
        # 设置布局
        self.setFixedHeight(80)
        self.hBoxLayout.setContentsMargins(15, 12, 15, 12)
        self.hBoxLayout.setSpacing(15)
        
        self.hBoxLayout.addWidget(self.coverLabel)
        
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(4)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignVCenter)
        self.vBoxLayout.addWidget(self.infoLabel, 0, Qt.AlignmentFlag.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        self.hBoxLayout.addLayout(self.vBoxLayout)
        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.deleteButton, 0, Qt.AlignmentFlag.AlignRight)
        
        # 加载封面（最后执行）
        self.load_cover()
    
    def load_cover(self):
        """加载游戏封面"""
        # Steam 封面 URL
        cover_url = f"https://cdn.akamai.steamstatic.com/steam/apps/{self.appid}/header.jpg"
        request = QNetworkRequest(QUrl(cover_url))
        self.network_manager.get(request)
    
    @pyqtSlot(QNetworkReply)
    def on_cover_loaded(self, reply):
        """封面加载完成"""
        if reply.error() == QNetworkReply.NetworkError.NoError:
            data = reply.readAll()
            pixmap = QPixmap()
            if pixmap.loadFromData(data):
                self.coverLabel.setPixmap(pixmap)
        reply.deleteLater()
    
    def on_delete_clicked(self):
        """删除按钮点击"""
        # 发送信号给父页面
        if self.parent():
            parent = self.parent()
            while parent and not isinstance(parent, HomePage):
                parent = parent.parent()
            if parent:
                parent.delete_game(self.appid, self.source_type)


class AsyncWorker(QThread):
    """异步工作线程"""
    finished = pyqtSignal(object)
    error = pyqtSignal(str)
    
    def __init__(self, coro):
        super().__init__()
        self.coro = coro
    
    def run(self):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(self.coro)
            loop.close()
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))

class HomePage(ScrollArea):
    """已入库的游戏页面（主页）"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("homePage")
        self.setWidgetResizable(True)
        
        # 主容器
        container = QWidget()
        container.setObjectName("homeContainer")
        self.setWidget(container)
        
        self.mainLayout = QVBoxLayout(container)
        self.mainLayout.setContentsMargins(30, 30, 30, 30)
        self.mainLayout.setSpacing(20)
        
        # 标题和统计
        header_layout = QHBoxLayout()
        self.title = SubtitleLabel(tr("installed_games"), self)
        self.stats_label = CaptionLabel(tr("loading"), self)
        self.stats_label.setTextColor("#606060", "#d2d2d2")
        header_layout.addWidget(self.title)
        header_layout.addStretch(1)
        header_layout.addWidget(self.stats_label)
        self.mainLayout.addLayout(header_layout)
        
        # 搜索框
        search_layout = QHBoxLayout()
        self.filter_input = SearchLineEdit(self)
        self.filter_input.setPlaceholderText(tr("search_placeholder"))
        self.filter_input.setFixedHeight(35)
        self.filter_input.textChanged.connect(self.on_filter_changed)
        self.filter_input.searchSignal.connect(self.on_filter_changed)
        self.filter_input.clearSignal.connect(self.on_filter_cleared)
        search_layout.addWidget(self.filter_input)
        self.mainLayout.addLayout(search_layout)
        
        # 游戏卡片容器
        self.card_container = QWidget(self)
        self.card_layout = QVBoxLayout(self.card_container)
        self.card_layout.setContentsMargins(0, 0, 0, 0)
        self.card_layout.setSpacing(10)
        
        self.mainLayout.addWidget(self.card_container)
        self.mainLayout.addStretch(1)
        
        # 设置透明背景
        self.setStyleSheet("HomePage { background: transparent; }")
        container.setStyleSheet("QWidget#homeContainer { background: transparent; }")
        
        # 标记需要加载游戏列表
        self._games_loaded = False
        self.worker = None
        self.game_cards = []
        self.all_games_data = []  # 存储所有游戏数据用于过滤
    
    def showEvent(self, event):
        """页面显示时加载游戏列表"""
        super().showEvent(event)
        if not self._games_loaded:
            self._games_loaded = True
            self.load_games()
    
    def load_games(self):
        """加载游戏列表"""
        async def _load():
            async with CaiBackend() as backend:
                await backend.initialize()
                files_data = await backend.get_managed_files()
                return files_data
        
        self.worker = AsyncWorker(_load())
        self.worker.finished.connect(self.on_games_loaded)
        self.worker.error.connect(self.on_load_error)
        self.worker.start()
    
    @pyqtSlot(object)
    def on_games_loaded(self, files_data):
        """游戏加载完成"""
        try:
            # 清空现有卡片
            for card in self.game_cards:
                card.deleteLater()
            self.game_cards.clear()
            
            # 统计游戏数量
            st_games = files_data.get('st', [])
            gl_games = files_data.get('gl', [])
            total = len(st_games) + len(gl_games)
            
            self.stats_label.setText(tr("total_games", total, len(st_games), len(gl_games)))
            
            # 创建游戏数据列表
            self.all_games_data = []
            for game in st_games:
                if game.get('status') != 'core_file':  # 跳过核心文件
                    self.all_games_data.append(('st', game))
            for game in gl_games:
                self.all_games_data.append(('gl', game))
            
            # 按 AppID 排序（降序）
            self.all_games_data.sort(key=lambda x: int(x[1].get('appid', '0')) if x[1].get('appid', '0').isdigit() else 0, reverse=True)
            
            # 显示所有游戏
            self.display_games(self.all_games_data)
                
        except Exception as e:
            self.stats_label.setText(f"处理数据失败: {str(e)}")
    
    def display_games(self, games_data):
        """显示游戏列表"""
        # 清空现有卡片
        for card in self.game_cards:
            card.deleteLater()
        self.game_cards.clear()
        
        # 添加卡片
        for source_type, game in games_data:
            appid = game.get('appid', 'N/A')
            game_name = game.get('game_name', '未知游戏')
            
            card = GameCard(appid, game_name, source_type, self)
            self.card_layout.addWidget(card)
            self.game_cards.append(card)
        
        if not games_data:
            empty_label = BodyLabel(tr("no_games"), self)
            empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.card_layout.addWidget(empty_label)
            self.game_cards.append(empty_label)
    
    def on_filter_changed(self):
        """搜索过滤"""
        query = self.filter_input.text().strip().lower()
        
        if not query:
            # 显示所有游戏
            self.display_games(self.all_games_data)
            return
        
        # 过滤游戏
        filtered_games = []
        for source_type, game in self.all_games_data:
            appid = game.get('appid', '')
            game_name = game.get('game_name', '').lower()
            
            # 匹配 AppID 或游戏名称
            if query in appid or query in game_name:
                filtered_games.append((source_type, game))
        
        self.display_games(filtered_games)
    
    def on_filter_cleared(self):
        """清除搜索"""
        self.display_games(self.all_games_data)
    
    def delete_game(self, appid, source_type):
        """删除游戏"""
        # 显示确认对话框
        dialog = MessageBox(
            tr("confirm_delete"),
            tr("delete_message", appid),
            self
        )
        
        if dialog.exec():
            # 用户确认删除
            async def _delete():
                async with CaiBackend() as backend:
                    await backend.initialize()
                    
                    # 构造删除项
                    items = [{
                        'appid': appid,
                        'filename': f'{appid}.lua' if source_type == 'st' else f'{appid}.txt'
                    }]
                    
                    result = backend.delete_managed_files(source_type, items)
                    return result
            
            self.delete_worker = AsyncWorker(_delete())
            self.delete_worker.finished.connect(lambda result: self.on_delete_complete(result, appid))
            self.delete_worker.error.connect(self.on_delete_error)
            self.delete_worker.start()
            
            InfoBar.info(
                title=tr("deleting"),
                content=f"{tr('deleting')} AppID {appid}...",
                parent=self,
                position=InfoBarPosition.TOP
            )
    
    @pyqtSlot(object)
    def on_delete_complete(self, result, appid):
        """删除完成"""
        if result.get('success'):
            InfoBar.success(
                title=tr("delete_success"),
                content=f"AppID {appid} {tr('delete_success')}",
                parent=self,
                position=InfoBarPosition.TOP
            )
            # 重新加载游戏列表
            self._games_loaded = False
            self.load_games()
        else:
            InfoBar.error(
                title=tr("delete_failed"),
                content=result.get('message', '未知错误'),
                parent=self,
                position=InfoBarPosition.TOP
            )
    
    @pyqtSlot(str)
    def on_delete_error(self, error):
        """删除失败"""
        InfoBar.error(
            title=tr("delete_failed"),
            content=error,
            parent=self,
            position=InfoBarPosition.TOP
        )
    
    @pyqtSlot(str)
    def on_load_error(self, error):
        """加载失败"""
        self.stats_label.setText(tr("load_failed", error))


class SearchPage(ScrollArea):
    """搜索和入库页面"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("searchPage")
        self.setWidgetResizable(True)
        
        # 主容器
        container = QWidget()
        container.setObjectName("searchContainer")
        self.setWidget(container)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # 标题
        title = SubtitleLabel(tr("search_and_add"), self)
        layout.addWidget(title)
        
        # 搜索卡片
        search_card = CardWidget(self)
        search_layout = QVBoxLayout(search_card)
        search_layout.setContentsMargins(20, 20, 20, 20)
        search_layout.setSpacing(15)
        
        # 搜索输入框和按钮
        input_layout = QHBoxLayout()
        self.search_input = SearchLineEdit(self)
        self.search_input.setPlaceholderText(tr("game_name_or_appid"))
        self.search_input.setFixedHeight(40)
        self.search_input.searchSignal.connect(self.on_search)
        input_layout.addWidget(self.search_input)
        
        self.search_button = PrimaryPushButton(tr("search_button"), self)
        self.search_button.setFixedSize(100, 40)
        self.search_button.clicked.connect(self.on_search)
        input_layout.addWidget(self.search_button)
        
        search_layout.addLayout(input_layout)
        layout.addWidget(search_card)
        
        # 选项卡片
        options_card = CardWidget(self)
        options_layout = QVBoxLayout(options_card)
        options_layout.setContentsMargins(20, 20, 20, 20)
        options_layout.setSpacing(15)
        
        options_title = BodyLabel(tr("add_options"), self)
        options_layout.addWidget(options_title)
        
        # 选项
        check_layout = QHBoxLayout()
        self.add_dlc_check = CheckBox(tr("add_all_dlc"), self)
        self.add_dlc_check.setChecked(False)
        check_layout.addWidget(self.add_dlc_check)
        
        self.patch_key_check = CheckBox(tr("patch_depot_key"), self)
        self.patch_key_check.setChecked(False)
        check_layout.addWidget(self.patch_key_check)
        
        check_layout.addStretch(1)
        options_layout.addLayout(check_layout)
        
        # 清单源选择
        source_layout = QHBoxLayout()
        source_layout.addWidget(BodyLabel(tr("manifest_source"), self))
        self.source_combo = ComboBox(self)
        self.source_combo.addItems([
            tr("auto_search_github"),
            tr("swa_v2"),
            tr("cysaw"),
            tr("furcate"),
            tr("walftech"),
            tr("steamdatabase"),
            tr("steamautocracks_v2"),
            tr("sudama"),
            tr("buqiuren"),
            tr("github_auiowu"),
            tr("github_sac")
        ])
        self.source_combo.setCurrentIndex(0)
        self.source_combo.setFixedWidth(240)
        source_layout.addWidget(self.source_combo)
        
        # 添加提示
        source_hint = CaptionLabel(tr("tip_source_fail"), self)
        source_hint.setTextColor("#606060", "#d2d2d2")
        source_layout.addWidget(source_hint)
        
        source_layout.addStretch(1)
        options_layout.addLayout(source_layout)
        
        layout.addWidget(options_card)
        
        # 结果和操作卡片
        result_card = CardWidget(self)
        result_layout = QVBoxLayout(result_card)
        result_layout.setContentsMargins(20, 20, 20, 20)
        result_layout.setSpacing(15)
        
        self.result_label = BodyLabel(tr("game_name_or_appid"), self)
        self.result_label.setWordWrap(True)
        result_layout.addWidget(self.result_label)
        
        # 入库按钮
        action_layout = QHBoxLayout()
        self.unlock_button = PrimaryPushButton(tr("add_game"), self)
        self.unlock_button.setFixedSize(120, 40)
        self.unlock_button.clicked.connect(self.on_unlock_game)
        self.unlock_button.setEnabled(False)
        action_layout.addWidget(self.unlock_button)
        
        self.progress_ring = ProgressRing(self)
        self.progress_ring.setFixedSize(24, 24)
        self.progress_ring.hide()
        action_layout.addWidget(self.progress_ring)
        
        action_layout.addStretch(1)
        result_layout.addLayout(action_layout)
        
        layout.addWidget(result_card)
        layout.addStretch(1)
        
        # 设置透明背景
        self.setStyleSheet("SearchPage { background: transparent; }")
        container.setStyleSheet("QWidget#searchContainer { background: transparent; }")
        
        # 状态变量
        self.current_appid = None
        self.search_worker = None
        self.unlock_worker = None
    
    def on_search(self):
        """搜索游戏"""
        query = self.search_input.text().strip()
        if not query:
            InfoBar.warning(
                title="提示",
                content=tr("game_name_or_appid"),
                parent=self,
                position=InfoBarPosition.TOP
            )
            return
        
        # 显示进度
        self.progress_ring.show()
        self.search_button.setEnabled(False)
        self.unlock_button.setEnabled(False)
        self.result_label.setText(tr("loading"))
        
        async def _search():
            async with CaiBackend() as backend:
                await backend.initialize()
                
                # 尝试提取 AppID
                appid = backend.extract_app_id(query)
                if appid:
                    # 直接是 AppID
                    return {'type': 'appid', 'appid': appid}
                else:
                    # 搜索游戏名称
                    results = await backend.find_appid_by_name(query)
                    return {'type': 'search', 'results': results}
        
        self.search_worker = AsyncWorker(_search())
        self.search_worker.finished.connect(self.on_search_complete)
        self.search_worker.error.connect(self.on_search_error)
        self.search_worker.start()
    
    @pyqtSlot(object)
    def on_search_complete(self, result):
        """搜索完成"""
        self.progress_ring.hide()
        self.search_button.setEnabled(True)
        
        if result['type'] == 'appid':
            # 直接是 AppID
            self.current_appid = result['appid']
            self.unlock_button.setEnabled(True)
            self.result_label.setText(f"✓ 识别成功\nAppID: {self.current_appid}\n\n点击「入库游戏」按钮继续")
            
            InfoBar.success(
                title="识别成功",
                content=f"AppID: {self.current_appid}",
                parent=self,
                position=InfoBarPosition.TOP
            )
        else:
            # 搜索结果
            results = result['results']
            if not results:
                self.result_label.setText("✗ 未找到匹配的游戏\n请检查游戏名称或尝试使用 AppID")
                InfoBar.warning(
                    title="未找到",
                    content="未找到匹配的游戏",
                    parent=self,
                    position=InfoBarPosition.TOP
                )
                return
            
            # 显示第一个结果
            first = results[0]
            self.current_appid = first['appid']
            self.unlock_button.setEnabled(True)
            
            result_text = f"✓ 找到游戏\n\n游戏名称: {first['name']}\nAppID: {first['appid']}\n\n点击「入库游戏」按钮继续"
            if len(results) > 1:
                result_text += f"\n\n提示: 找到 {len(results)} 个结果，已选择第一个"
            
            self.result_label.setText(result_text)
            
            InfoBar.success(
                title="找到游戏",
                content=f"{first['name']} (AppID: {first['appid']})",
                parent=self,
                position=InfoBarPosition.TOP,
                duration=3000
            )
    
    @pyqtSlot(str)
    def on_search_error(self, error):
        """搜索失败"""
        self.progress_ring.hide()
        self.search_button.setEnabled(True)
        self.result_label.setText(f"✗ 搜索失败\n{error}")
        InfoBar.error(
            title="搜索失败",
            content=error,
            parent=self,
            position=InfoBarPosition.TOP
        )
    
    def on_unlock_game(self):
        """入库游戏"""
        if not self.current_appid:
            return
        
        # 获取选项
        add_all_dlc = self.add_dlc_check.isChecked()
        patch_depot_key = self.patch_key_check.isChecked()
        
        # 获取清单源
        source_map = {
            "自动搜索GitHub (推荐)": "search",
            "SWA V2": "printedwaste",
            "Cysaw": "cysaw",
            "Furcate": "furcate",
            "Walftech": "walftech",
            "steamdatabase": "steamdatabase",
            "SteamAutoCracks V2 (仅密钥)": "steamautocracks_v2",
            "Sudama库 (仅密钥)": "sudama",
            "清单不求人库 (仅清单)": "buqiuren",
            "GitHub (Auiowu)": "Auiowu/ManifestAutoUpdate",
            "GitHub (SAC)": "SteamAutoCracks/ManifestHub"
        }
        tool_type = source_map.get(self.source_combo.currentText(), "search")
        
        # 显示进度
        self.progress_ring.show()
        self.unlock_button.setEnabled(False)
        self.search_button.setEnabled(False)
        self.result_label.setText(f"{tr('loading')} AppID {self.current_appid}...\nPlease wait")
        
        async def _unlock():
            async with CaiBackend() as backend:
                unlocker_type = await backend.initialize()
                if not unlocker_type:
                    raise Exception("解锁工具类型未能确定，请检查配置或Steam路径")
                
                await backend.checkcn()
                
                # 处理清单
                if tool_type == "search":
                    results = await backend.search_all_repos_for_appid(self.current_appid)
                    if not results:
                        raise Exception(f"在所有 GitHub 仓库中都未找到 AppID {self.current_appid} 的清单")
                    # 使用第一个源
                    tool_type_actual = list(results.keys())[0]
                else:
                    tool_type_actual = tool_type
                
                # 判断是 ZIP 源还是 GitHub 源
                zip_sources = ["printedwaste", "cysaw", "furcate", "walftech", "steamdatabase", "steamautocracks_v2", "sudama", "buqiuren"]
                if tool_type_actual in zip_sources:
                    success = await backend.process_zip_source(
                        self.current_appid, tool_type_actual, unlocker_type,
                        False, add_all_dlc, patch_depot_key
                    )
                else:
                    success = await backend.process_github_manifest(
                        self.current_appid, tool_type_actual, unlocker_type,
                        False, add_all_dlc, patch_depot_key
                    )
                
                return success
        
        self.unlock_worker = AsyncWorker(_unlock())
        self.unlock_worker.finished.connect(self.on_unlock_complete)
        self.unlock_worker.error.connect(self.on_unlock_error)
        self.unlock_worker.start()
    
    @pyqtSlot(object)
    def on_unlock_complete(self, success):
        """入库完成"""
        self.progress_ring.hide()
        self.unlock_button.setEnabled(True)
        self.search_button.setEnabled(True)
        
        if success:
            self.result_label.setText(f"✓ 入库成功！\n\nAppID {self.current_appid} 已成功入库\n请重启 Steam 使更改生效")
            InfoBar.success(
                title="入库成功",
                content=f"AppID {self.current_appid} 已成功入库，重启 Steam 后生效",
                parent=self,
                position=InfoBarPosition.TOP,
                duration=3000
            )
        else:
            self.result_label.setText(f"✗ 入库失败\n处理失败，请查看日志")
            InfoBar.error(
                title="入库失败",
                content="处理失败，请查看日志",
                parent=self,
                position=InfoBarPosition.TOP
            )
    
    @pyqtSlot(str)
    def on_unlock_error(self, error):
        """入库失败"""
        self.progress_ring.hide()
        self.unlock_button.setEnabled(True)
        self.search_button.setEnabled(True)
        
        # 友好的错误提示
        if "Server disconnected" in error or "RemoteProtocolError" in error:
            error_msg = "网络连接失败，服务器断开连接\n\n可能的原因：\n1. 清单源服务器不稳定\n2. 网络连接问题\n\n建议：\n- 尝试切换其他清单源\n- 检查网络连接\n- 稍后重试"
        elif "未找到" in error or "not found" in error.lower():
            error_msg = f"未找到 AppID {self.current_appid} 的清单\n\n建议：\n- 尝试切换其他清单源\n- 使用「自动搜索GitHub」选项"
        elif "GitHub API" in error:
            error_msg = "GitHub API 请求次数已用尽\n\n建议：\n- 在设置中配置 GitHub Token\n- 使用其他清单源"
        else:
            error_msg = error
        
        self.result_label.setText(f"✗ 入库失败\n\n{error_msg}")
        
        InfoBar.error(
            title="入库失败",
            content="处理失败，请查看详细信息或尝试其他清单源",
            parent=self,
            position=InfoBarPosition.TOP,
            duration=5000
        )


class SettingsPage(ScrollArea):
    """设置页面"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("settingsPage")
        self.setWidgetResizable(True)
        
        # 主容器
        container = QWidget()
        container.setObjectName("settingsContainer")
        self.setWidget(container)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # 标题
        title = SubtitleLabel(tr("settings"), self)
        layout.addWidget(title)
        
        # Steam 路径设置
        steam_card = CardWidget(self)
        steam_layout = QVBoxLayout(steam_card)
        steam_layout.setContentsMargins(20, 20, 20, 20)
        steam_layout.setSpacing(10)
        
        steam_label = BodyLabel(tr("steam_path"), self)
        steam_layout.addWidget(steam_label)
        
        self.steam_path_edit = LineEdit(self)
        self.steam_path_edit.setPlaceholderText("留空则自动检测")
        steam_layout.addWidget(self.steam_path_edit)
        
        layout.addWidget(steam_card)
        
        # GitHub Token 设置
        token_card = CardWidget(self)
        token_layout = QVBoxLayout(token_card)
        token_layout.setContentsMargins(20, 20, 20, 20)
        token_layout.setSpacing(10)
        
        token_label = BodyLabel(tr("github_token"), self)
        token_layout.addWidget(token_label)
        
        self.token_edit = LineEdit(self)
        self.token_edit.setPlaceholderText("可选，用于提高 API 请求限制")
        token_layout.addWidget(self.token_edit)
        
        layout.addWidget(token_card)
        
        # 应用程序配置
        app_config_card = CardWidget(self)
        app_config_layout = QVBoxLayout(app_config_card)
        app_config_layout.setContentsMargins(20, 20, 20, 20)
        app_config_layout.setSpacing(15)
        
        app_config_label = BodyLabel(tr("application_config"), self)
        app_config_layout.addWidget(app_config_label)
        
        # 调试模式
        debug_row = QHBoxLayout()
        debug_row.addWidget(BodyLabel(tr("debug_mode"), self))
        self.debug_check = CheckBox(tr("enable_debug_log"), self)
        debug_row.addWidget(self.debug_check)
        debug_row.addStretch(1)
        app_config_layout.addLayout(debug_row)
        
        # 保存日志文件
        logging_row = QHBoxLayout()
        logging_row.addWidget(BodyLabel(tr("save_log_files"), self))
        self.logging_check = CheckBox(tr("save_logs_to_file"), self)
        logging_row.addWidget(self.logging_check)
        logging_row.addStretch(1)
        app_config_layout.addLayout(logging_row)
        
        # 强制解锁工具模式
        unlocker_row = QHBoxLayout()
        unlocker_row.addWidget(BodyLabel(tr("unlocker_mode"), self))
        self.unlocker_combo = ComboBox(self)
        self.unlocker_combo.addItems([tr("auto_detect"), tr("force_steamtools"), tr("force_greenluma")])
        self.unlocker_combo.setCurrentIndex(0)
        self.unlocker_combo.setFixedWidth(180)
        unlocker_row.addWidget(self.unlocker_combo)
        unlocker_hint = CaptionLabel(tr("force_unlocker_hint"), self)
        unlocker_hint.setTextColor("#606060", "#d2d2d2")
        unlocker_row.addWidget(unlocker_hint)
        unlocker_row.addStretch(1)
        app_config_layout.addLayout(unlocker_row)
        
        layout.addWidget(app_config_card)
        
        # 外观设置
        appearance_card = CardWidget(self)
        appearance_layout = QVBoxLayout(appearance_card)
        appearance_layout.setContentsMargins(20, 20, 20, 20)
        appearance_layout.setSpacing(15)
        
        appearance_label = BodyLabel(tr("appearance"), self)
        appearance_layout.addWidget(appearance_label)
        
        # 主题模式
        theme_row = QHBoxLayout()
        theme_row.addWidget(BodyLabel(tr("theme_mode"), self))
        self.theme_combo = ComboBox(self)
        self.theme_combo.addItems([tr("light_theme"), tr("dark_theme"), tr("follow_system")])
        self.theme_combo.setCurrentIndex(2 if not isDarkTheme() else 1)
        self.theme_combo.currentIndexChanged.connect(self.on_theme_mode_changed)
        self.theme_combo.setFixedWidth(150)
        theme_row.addWidget(self.theme_combo)
        theme_row.addStretch(1)
        appearance_layout.addLayout(theme_row)
        
        # 主题色
        color_row = QHBoxLayout()
        color_row.addWidget(BodyLabel(tr("theme_color"), self))
        self.color_combo = ComboBox(self)
        self.color_combo.addItems([
            tr("default_blue"),
            tr("purple"),
            tr("green"),
            tr("orange"),
            tr("red"),
            tr("pink")
        ])
        self.color_combo.currentIndexChanged.connect(self.on_theme_color_changed)
        self.color_combo.setFixedWidth(200)
        color_row.addWidget(self.color_combo)
        color_row.addStretch(1)
        appearance_layout.addLayout(color_row)
        
        # 语言
        lang_row = QHBoxLayout()
        lang_row.addWidget(BodyLabel(tr("language"), self))
        self.lang_combo = ComboBox(self)
        self.lang_combo.addItems(["简体中文", "English"])
        self.lang_combo.setCurrentIndex(0)
        self.lang_combo.currentIndexChanged.connect(self.on_language_changed)
        self.lang_combo.setFixedWidth(150)
        lang_row.addWidget(self.lang_combo)
        lang_hint = CaptionLabel("(需要重启应用)", self)
        lang_hint.setTextColor("#606060", "#d2d2d2")
        lang_row.addWidget(lang_hint)
        lang_row.addStretch(1)
        appearance_layout.addLayout(lang_row)
        
        layout.addWidget(appearance_card)
        
        # 按钮行
        button_layout = QHBoxLayout()
        
        self.save_btn = PrimaryPushButton(tr("save_settings"), self)
        self.save_btn.clicked.connect(self.save_settings)
        self.save_btn.setFixedWidth(120)
        button_layout.addWidget(self.save_btn)
        
        self.reset_btn = PushButton("重置为默认", self)
        self.reset_btn.clicked.connect(self.reset_settings)
        self.reset_btn.setFixedWidth(120)
        button_layout.addWidget(self.reset_btn)
        
        self.about_btn = PushButton(tr("about"), self)
        self.about_btn.clicked.connect(self.show_about)
        self.about_btn.setFixedWidth(100)
        button_layout.addWidget(self.about_btn)
        
        self.thanks_btn = PushButton(tr("thanks"), self)
        self.thanks_btn.clicked.connect(self.show_thanks)
        self.thanks_btn.setFixedWidth(100)
        button_layout.addWidget(self.thanks_btn)
        
        button_layout.addStretch(1)
        layout.addLayout(button_layout)
        
        layout.addStretch(1)
        
        # 设置透明背景
        self.setStyleSheet("SettingsPage { background: transparent; }")
        container.setStyleSheet("QWidget#settingsContainer { background: transparent; }")
        
        # 标记需要加载配置
        self._config_loaded = False
        self.worker = None
    
    def showEvent(self, event):
        """页面显示时加载配置"""
        super().showEvent(event)
        if not self._config_loaded:
            self._config_loaded = True
            self.load_config()
    
    def on_theme_mode_changed(self, index):
        """主题模式切换"""
        if index == 0:  # 浅色
            setTheme(Theme.LIGHT)
        elif index == 1:  # 深色
            setTheme(Theme.DARK)
        else:  # 跟随系统
            setTheme(Theme.AUTO)
        
        # 立即保存设置
        self.save_theme_setting("theme_mode", ["light", "dark", "auto"][index])
    
    def on_theme_color_changed(self, index):
        """主题色切换"""
        colors = ["#0078d4", "#9b4dca", "#10893e", "#ff8c00", "#e81123", "#e3008c"]
        if 0 <= index < len(colors):
            setThemeColor(colors[index])
            # 立即保存设置
            self.save_theme_setting("theme_color", colors[index])
    
    def save_theme_setting(self, key, value):
        """保存单个主题设置"""
        try:
            config_path = Path.cwd() / 'config.json'
            import json
            
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            else:
                from backend import DEFAULT_CONFIG
                config = DEFAULT_CONFIG.copy()
            
            config[key] = value
            
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存主题设置失败: {e}")
    
    def on_language_changed(self, index):
        """语言切换"""
        lang_map = {0: "zh_CN", 1: "en_US"}
        selected_lang = lang_map.get(index, "zh_CN")
        lang_name = "简体中文" if index == 0 else "English"
        
        # 显示重启提示
        dialog = MessageBox(
            tr("restart_required"),
            tr("language_changed", lang_name),
            self.window()
        )
        
        if dialog.exec():
            # 保存语言设置
            self.save_language_setting(selected_lang)
            # 重启应用
            import sys
            from PyQt6.QtWidgets import QApplication
            QApplication.quit()
            import os
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            # 用户取消，恢复原来的选择
            # 读取当前保存的语言设置
            current_lang = self.load_language_setting()
            if current_lang == "zh_CN":
                self.lang_combo.setCurrentIndex(0)
            else:
                self.lang_combo.setCurrentIndex(1)
    
    def save_language_setting(self, lang):
        """保存语言设置"""
        try:
            config_path = Path.cwd() / 'config.json'
            import json
            
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            else:
                from backend import DEFAULT_CONFIG
                config = DEFAULT_CONFIG.copy()
            
            config["language"] = lang
            
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存语言设置失败: {e}")
    
    def load_language_setting(self):
        """加载语言设置"""
        try:
            config_path = Path.cwd() / 'config.json'
            if config_path.exists():
                import json
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                return config.get("language", "zh_CN")
        except:
            pass
        return "zh_CN"
    
    def show_about(self):
        """显示关于对话框"""
        about_text = """Cai Install - Fluent Design 版本

版本: 1.0.0

这是一个基于 PyQt6-Fluent-Widgets 的现代化 Steam 游戏解锁工具。

功能特性:
• Fluent Design 设计风格
• 支持多种清单源
• 游戏搜索和入库
• 已入库游戏管理
• 主题自定义

项目地址: https://github.com/zhouchentao666/Cai-install-Fluent-GUI"""
        
        dialog = MessageBox("关于", about_text, self.window())
        dialog.exec()
    
    def show_thanks(self):
        """显示鸣谢对话框"""
        thanks_text = """特别鸣谢

开发者:
• zhouchentao666 - 制作人员

开源项目:
• PyQt6 - Qt6 Python 绑定
• PyQt-Fluent-Widgets - Fluent Design 组件库
• Cai-install-Web-GUI - 原始项目作者
• httpx - 异步 HTTP 客户端

清单源提供:
• SWA V2
• Cysaw
• Furcate
• Walftech
• steamdatabase
• SteamAutoCracks
• Sudama
• 清单不求人

感谢所有为本项目做出贡献的开发者和用户！"""
        
        dialog = MessageBox("鸣谢", thanks_text, self.window())
        dialog.exec()
    
    def load_config(self):
        """加载配置"""
        async def _load():
            async with CaiBackend() as backend:
                config = await backend.load_config()
                return config
        
        self.worker = AsyncWorker(_load())
        self.worker.finished.connect(self.on_config_loaded)
        self.worker.error.connect(self.on_load_error)
        self.worker.start()
    
    @pyqtSlot(object)
    def on_config_loaded(self, config):
        """配置加载完成"""
        if config:
            self.steam_path_edit.setText(config.get("Custom_Steam_Path", ""))
            self.token_edit.setText(config.get("Github_Personal_Token", ""))
            
            # 加载应用程序配置
            self.debug_check.setChecked(config.get("debug_mode", False))
            self.logging_check.setChecked(config.get("logging_files", True))
            
            # 加载解锁工具模式
            force_unlocker = config.get("force_unlocker_type", "auto")
            if force_unlocker == "steamtools":
                self.unlocker_combo.setCurrentIndex(1)
            elif force_unlocker == "greenluma":
                self.unlocker_combo.setCurrentIndex(2)
            else:
                self.unlocker_combo.setCurrentIndex(0)
            
            # 加载语言设置
            # 先断开信号连接，避免触发 on_language_changed
            self.lang_combo.currentIndexChanged.disconnect(self.on_language_changed)
            
            lang = config.get("language", "zh_CN")
            if lang == "zh_CN":
                self.lang_combo.setCurrentIndex(0)
            else:
                self.lang_combo.setCurrentIndex(1)
            
            # 重新连接信号
            self.lang_combo.currentIndexChanged.connect(self.on_language_changed)
            
            # 加载主题模式设置
            theme_mode = config.get("theme_mode", "auto")
            if theme_mode == "light":
                self.theme_combo.setCurrentIndex(0)
            elif theme_mode == "dark":
                self.theme_combo.setCurrentIndex(1)
            else:
                self.theme_combo.setCurrentIndex(2)
            
            # 加载主题色设置
            theme_color = config.get("theme_color", "#0078d4")
            color_map = {
                "#0078d4": 0,
                "#9b4dca": 1,
                "#10893e": 2,
                "#ff8c00": 3,
                "#e81123": 4,
                "#e3008c": 5
            }
            color_index = color_map.get(theme_color, 0)
            self.color_combo.setCurrentIndex(color_index)
    
    @pyqtSlot(str)
    def on_load_error(self, error):
        """加载失败"""
        InfoBar.error(
            title="加载配置失败",
            content=error,
            parent=self,
            position=InfoBarPosition.TOP
        )
    
    def save_settings(self):
        """保存设置"""
        async def _save():
            config_path = Path.cwd() / 'config.json'
            import json
            
            # 读取现有配置
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            else:
                from backend import DEFAULT_CONFIG
                config = DEFAULT_CONFIG.copy()
            
            # 更新配置
            config["Custom_Steam_Path"] = self.steam_path_edit.text().strip()
            config["Github_Personal_Token"] = self.token_edit.text().strip()
            
            # 保存应用程序配置
            config["debug_mode"] = self.debug_check.isChecked()
            config["logging_files"] = self.logging_check.isChecked()
            
            # 保存解锁工具模式
            unlocker_map = {0: "auto", 1: "steamtools", 2: "greenluma"}
            config["force_unlocker_type"] = unlocker_map.get(self.unlocker_combo.currentIndex(), "auto")
            
            # 保存主题模式
            theme_mode_map = {0: "light", 1: "dark", 2: "auto"}
            config["theme_mode"] = theme_mode_map.get(self.theme_combo.currentIndex(), "auto")
            
            # 保存主题色
            colors = ["#0078d4", "#9b4dca", "#10893e", "#ff8c00", "#e81123", "#e3008c"]
            color_index = self.color_combo.currentIndex()
            if 0 <= color_index < len(colors):
                config["theme_color"] = colors[color_index]
            
            # 保存语言（已经在 on_language_changed 中保存了，这里也保存一次以防万一）
            lang_map = {0: "zh_CN", 1: "en_US"}
            config["language"] = lang_map.get(self.lang_combo.currentIndex(), "zh_CN")
            
            # 保存配置
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            return True
        
        self.worker = AsyncWorker(_save())
        self.worker.finished.connect(self.on_save_success)
        self.worker.error.connect(self.on_save_error)
        self.worker.start()
    
    @pyqtSlot(object)
    def on_save_success(self, result):
        """保存成功"""
        InfoBar.success(
            title="保存成功",
            content="配置已保存",
            parent=self,
            position=InfoBarPosition.TOP
        )
    
    @pyqtSlot(str)
    def on_save_error(self, error):
        """保存失败"""
        InfoBar.error(
            title="保存失败",
            content=error,
            parent=self,
            position=InfoBarPosition.TOP
        )
    
    def reset_settings(self):
        """重置设置为默认值"""
        dialog = MessageBox(
            tr("reset_settings"),
            tr("reset_settings_message"),
            self.window()
        )
        
        if dialog.exec():
            async def _reset():
                config_path = Path.cwd() / 'config.json'
                from backend import DEFAULT_CONFIG
                import json
                
                # 保留背景设置（如果有）
                existing_bg_settings = {}
                if config_path.exists():
                    try:
                        with open(config_path, 'r', encoding='utf-8') as f:
                            current_config = json.load(f)
                        bg_keys = ["background_image_path", "background_blur", "background_saturation", "background_brightness"]
                        for key in bg_keys:
                            if key in current_config:
                                existing_bg_settings[key] = current_config[key]
                    except:
                        pass
                
                # 创建新配置
                new_config = DEFAULT_CONFIG.copy()
                new_config.update(existing_bg_settings)
                
                # 保存配置
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(new_config, f, indent=2, ensure_ascii=False)
                
                return True
            
            self.worker = AsyncWorker(_reset())
            self.worker.finished.connect(self.on_reset_success)
            self.worker.error.connect(self.on_reset_error)
            self.worker.start()
    
    @pyqtSlot(object)
    def on_reset_success(self, result):
        """重置成功"""
        InfoBar.success(
            title=tr("reset_success"),
            content=tr("reset_success_message"),
            parent=self,
            position=InfoBarPosition.TOP
        )
        # 重新加载配置
        self._config_loaded = False
        self.load_config()
    
    @pyqtSlot(str)
    def on_reset_error(self, error):
        """重置失败"""
        InfoBar.error(
            title=tr("reset_failed"),
            content=error,
            parent=self,
            position=InfoBarPosition.TOP
        )


class MainWindow(MSFluentWindow):
    """主窗口"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(tr("app_title"))
        self.resize(1000, 700)
        
        # 设置标题栏（避免按钮重叠）
        self.titleBar.raise_()
        
        # 创建页面
        self.home_page = HomePage(self)
        self.search_page = SearchPage(self)
        self.settings_page = SettingsPage(self)
        
        # 添加导航项
        self.addSubInterface(
            self.home_page,
            FluentIcon.HOME,
            tr("home")
        )
        
        self.addSubInterface(
            self.search_page,
            FluentIcon.SEARCH,
            tr("search")
        )
        
        # 在导航栏底部添加设置
        self.addSubInterface(
            self.settings_page,
            FluentIcon.SETTING,
            tr("settings"),
            position=NavigationItemPosition.BOTTOM
        )
        
        # 在导航栏底部添加重启 Steam 按钮
        self.navigationInterface.addItem(
            routeKey="restart_steam",
            icon=FluentIcon.POWER_BUTTON,
            text=tr("restart_steam"),
            onClick=self.on_restart_steam,
            selectable=False,
            position=NavigationItemPosition.BOTTOM
        )
        
        # 设置窗口效果
        # navigationInterface 在 MSFluentWindow 中已经配置好了
        # 不需要手动设置宽度
        
        # 设置透明背景
        self.setStyleSheet("""
            MSFluentWindow {
                background: transparent;
            }
        """)
    
    def on_restart_steam(self):
        """重启 Steam"""
        dialog = MessageBox(
            tr("restart_steam_confirm"),
            tr("restart_steam_message"),
            self
        )
        
        if dialog.exec():
            # 用户点击确认
            self.restart_steam_worker = None
            
            async def _restart():
                async with CaiBackend() as backend:
                    await backend.initialize()
                    success = backend.restart_steam()
                    return success
            
            self.restart_steam_worker = AsyncWorker(_restart())
            self.restart_steam_worker.finished.connect(self.on_restart_complete)
            self.restart_steam_worker.error.connect(self.on_restart_error)
            self.restart_steam_worker.start()
            
            InfoBar.info(
                title=tr("restarting"),
                content=tr("restarting_message"),
                parent=self,
                position=InfoBarPosition.TOP
            )
    
    @pyqtSlot(object)
    def on_restart_complete(self, success):
        """重启完成"""
        if success:
            InfoBar.success(
                title=tr("restart_success"),
                content=tr("restart_success_message"),
                parent=self,
                position=InfoBarPosition.TOP
            )
        else:
            InfoBar.error(
                title=tr("restart_failed"),
                content=tr("restart_failed_message"),
                parent=self,
                position=InfoBarPosition.TOP
            )
    
    @pyqtSlot(str)
    def on_restart_error(self, error):
        """重启失败"""
        InfoBar.error(
            title=tr("restart_failed"),
            content=tr("restart_error_message", error),
            parent=self,
            position=InfoBarPosition.TOP
        )


def main():
    """主函数"""
    # 加载语言设置
    lang = load_language_config()
    set_language(lang)
    
    # 加载主题设置
    theme_config = load_theme_config()
    
    app = QApplication(sys.argv)
    
    # 设置语言环境
    if lang in LANGUAGES:
        locale = LANGUAGES[lang]["locale"]
        QLocale.setDefault(locale)
        
        # 尝试加载 Qt 翻译
        translator = QTranslator()
        if lang == "zh_CN":
            # 加载 Qt 自带的中文翻译
            if translator.load("qtbase_zh_CN", ":/translations"):
                app.installTranslator(translator)
    
    # 应用主题设置
    theme_mode = theme_config["theme_mode"]
    if theme_mode == "light":
        setTheme(Theme.LIGHT)
    elif theme_mode == "dark":
        setTheme(Theme.DARK)
    else:
        setTheme(Theme.AUTO)
    
    # 应用主题色
    setThemeColor(theme_config["theme_color"])
    
    # 创建主窗口
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()