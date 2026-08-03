import sys
import os

# Add parent directory of api (which is the project root) to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from finance_copilot_equity.web_app.main import app
