"""솔커트 캐릭터 누끼를 원하는 배경 위에 세워 1080x1920 이미지를 만든다.
    python compose.py 배경.jpg 결과.png [--cx 285] [--top 610] [--feet 1820]
기본값 = 억새밭 기준 이미지 구도 (캐릭터 왼쪽, 스틱 윗단 y610, 발끝 y1820).
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
p = argparse.ArgumentParser()
p.add_argument("bg"); p.add_argument("out")
p.add_argument("--cx", type=int, default=285)
p.add_argument("--top", type=int, default=610)
p.add_argument("--feet", type=int, default=1820)
a = p.parse_args()
W, H = 1080, 1920

ch = Image.open(os.path.join(HERE, "이미지", "솔커트캐릭터_누끼.png")).convert("RGBA")
k = (a.feet - a.top) / ch.height
ch = ch.resize((round(ch.width * k), round(ch.height * k)), Image.LANCZOS)
m = ch.split()[3].filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))

bg = Image.open(a.bg).convert("RGB")
s = max(W / bg.width, H / bg.height)
bg = bg.resize((round(bg.width * s), round(bg.height * s)), Image.LANCZOS)
l, t = (bg.width - W) // 2, (bg.height - H) // 2
bg = bg.crop((l, t, l + W, t + H))

px = a.cx - ch.width // 2
sh = Image.new("L", (W, H), 0)
ImageDraw.Draw(sh).ellipse((px + ch.width * 0.18, a.feet - 26, px + ch.width * 0.82, a.feet + 22), fill=150)
sh = sh.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.55))
bg = Image.composite(Image.new("RGB", (W, H), (40, 28, 15)), bg, sh)
bg.paste(ch.convert("RGB"), (px, a.top), m)
bg.save(a.out)
print(a.out)
