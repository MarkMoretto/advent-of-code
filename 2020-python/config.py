
import platform

# Check if Python version is 3.4.x or better.
if int("".join(platform.python_version_tuple()[:2])) < 34:
    print("please upgrade Python to version 3.4.x or better before running!")

import os
from pathlib import Path

PROJECT_FOLDER = Path(os.path.dirname(os.path.abspath(__file__)))
PARENT_FOLDER = PROJECT_FOLDER.parent
DATA_FOLDER = PARENT_FOLDER.joinpath(r"data")
