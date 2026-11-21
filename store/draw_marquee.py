"""Marquee promo tile (1400x560) for the Chrome Web Store. Run from the repo root."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1400, 560
im = Image.new("RGB", (W, H))
d = ImageDraw.Draw(im)
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(24 + 14 * t), int(48 + 22 * t), int(80 + 30 * t)))
# screenshot of the side panel, tilted card on the right
shot = Image.open("screenshots/1-summarize.png").convert("RGB").crop((880, 84, 1280, 700))
shot = shot.resize((330, 508), Image.LANCZOS)
shadow = Image.new("RGBA", (shot.width + 60, shot.height + 60), (0, 0, 0, 0))
ImageDraw.Draw(shadow).rounded_rectangle([30, 34, 30 + shot.width, 34 + shot.height], 18, fill=(0, 0, 0, 120))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
im.paste(shadow, (980 - 30, 46 - 30), shadow)
mask = Image.new("L", shot.size, 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, shot.width - 1, shot.height - 1], 14, fill=255)
im.paste(shot, (980, 46), mask)
icon = Image.open("images/icon-128px.png").convert("RGBA").resize((150, 150), Image.LANCZOS)
im.paste(icon, (90, 120), icon)
f = "C:/Windows/Fonts/"
d.text((270, 118), "Quill", font=ImageFont.truetype(f + "segoeuib.ttf", 104), fill=(255, 255, 255))
d.text((276, 256), "AI chat in your side panel", font=ImageFont.truetype(f + "seguisb.ttf", 38), fill=(170, 222, 236))
d.text((276, 312), "Summarize, explain and translate the page you read", font=ImageFont.truetype(f + "segoeui.ttf", 28), fill=(253, 170, 140))
d.text((92, 420), "Claude  ·  OpenAI  ·  OVHcloud AI Endpoints  ·  Ollama", font=ImageFont.truetype(f + "segoeui.ttf", 26), fill=(200, 212, 228))
im.save("store/marquee-1400x560.png")
