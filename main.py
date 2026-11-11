# News summary entry (Python 3.13, standard library only): copy the summary
# written beside this file to /output/entry.txt. Outside the grader's
# container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
import shutil
from pathlib import Path

here = Path(__file__).resolve().parent
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(here / "summary.txt", out_dir / "entry.txt")
