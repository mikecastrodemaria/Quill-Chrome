"""Fit screenshots to the Chrome Web Store format: 1280x800, 24-bit PNG, no alpha.

Usage (from the repo root):
    python store/fit_screenshot.py "C:/path/capture1.png" "C:/path/capture2.png"

Each image is scaled to fit (never cropped), centered on the Quill navy
background, and saved as store/screenshot-<n>-1280x800.png.
"""
import sys
from pathlib import Path
from PIL import Image

W, H = 1280, 800
BG = (27, 54, 88)
out_dir = Path(__file__).resolve().parent
for n, src in enumerate(sys.argv[1:], 1):
    im = Image.open(src).convert("RGBA")
    scale = min(W / im.width, H / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), BG)
    canvas.paste(im, ((W - im.width) // 2, (H - im.height) // 2), im)
    dest = out_dir / f"screenshot-{n}-1280x800.png"
    canvas.save(dest)
    print(dest)
