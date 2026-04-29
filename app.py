import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'final project'))

from web_app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
