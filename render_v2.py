import subprocess
import os
import shutil
from PIL import Image

html_file = r"c:\Users\NITRO\PROFE7\hifi_wireframe_board_v2.html"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

out_png = r"c:\Users\NITRO\PROFE7\hifi_wireframe_jeron_opjer_v2.png"
art_path = r"C:\Users\NITRO\.gemini\antigravity-ide\brain\6be15b9e-35b8-446a-93fe-83cb646ff231\hifi_wireframe_jeron_opjer_v2.png"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=1.5",
    "--window-size=1100,1520",
    f"--screenshot={out_png}",
    f"file:///{html_file.replace(chr(92), '/')}"
]

print("Rendering v2...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Returncode:", res.returncode)

if os.path.exists(out_png):
    im = Image.open(out_png)
    w, h = im.size
    print("Raw size:", w, h)
    bg = im.getpixel((5, 5))
    bottom = h - 1
    for y in range(h - 1, -1, -1):
        if any(abs(im.getpixel((x, y))[0] - bg[0]) > 20 or abs(im.getpixel((x, y))[1] - bg[1]) > 20 for x in range(0, w, 10)):
            bottom = y
            break
    print("Bottom of content:", bottom)
    cropped = im.crop((0, 0, w, min(h, bottom + 40)))
    cropped.save(out_png, "PNG", optimize=True)
    shutil.copyfile(out_png, art_path)
    print("Saved cropped size:", cropped.size)
