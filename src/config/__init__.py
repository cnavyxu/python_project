"""
配置模块

提供配置管理功能
"""

import os
import yaml
from typing import Any, Dict


class Config:
    """配置管理类"""
    
    def __init__(self, config_path: str = None):
        self.config: Dict[str, Any] = {}
        if config_path and os.path.exists(config_path):
            self.load_from_file(config_path)
    
    def load_from_file(self, config_path: str):
        """从文件加载配置"""
        with open(config_path, 'r', encoding='utf-8') as f:
            if config_path.endswith('.yaml') or config_path.endswith('.yml'):
                self.config = yaml.safe_load(f)
            else:
                raise ValueError("不支持的配置文件格式")
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置项"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any):
        """设置配置项"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
    
    def save_to_file(self, config_path: str):
        """保存配置到文件"""
        with open(config_path, 'w', encoding='utf-8') as f:
            if config_path.endswith('.yaml') or config_path.endswith('.yml'):
                yaml.dump(self.config, f, default_flow_style=False)
            else:
                raise ValueError("不支持的配置文件格式")


__all__ = [
    "Config",
]
