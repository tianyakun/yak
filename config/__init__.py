# __author__ = 'kkk'
# encoding: utf-8

import os
from default import Config
from development import DevelopmentConfig
from production import ProductionConfig


def load_config():
    """Load config."""
    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            return ProductionConfig
        else:
            return DevelopmentConfig
    except ImportError:
        return Config