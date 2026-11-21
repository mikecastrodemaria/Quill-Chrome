"""Small promo tile (440x280) for the Chrome Web Store. Run from the repo root."""
from PIL import Image, ImageDraw, ImageFont
W, H = 440, 280
im = Image.new("RGB", (W, H), (27, 54, 88))
d = ImageDraw.Draw(im)
for y in range(H):  # subtle vertical gradient
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(27 + 10 * t), int(54 + 18 * t), int(88 + 26 * t)))
icon = Image.open("images/icon-128px.png").convert("RGBA").resize((112, 112), Image.LANCZOS)
im.paste(icon, (34, 84), icon)
f = "C:/Windows/Fonts/"
title = ImageFont.truetype(f + "segoeuib.ttf", 46)
sub = ImageFont.truetype(f + "segoeui.ttf", 19)
d.text((170, 88), "Quill", font=title, fill=(255, 255, 255))
d.text((172, 146), "AI chat in your side panel", font=sub, fill=(170, 222, 236))
d.text((172, 172), "Talk with the page you read", font=sub, fill=(253, 170, 140))
im.save("store/promo-tile-440x280.png")
