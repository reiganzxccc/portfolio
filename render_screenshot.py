import subprocess
import os
import time

html_file = r"c:\Users\NITRO\PROFE7\hifi_wireframe_board.html"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

out_png_workspace = r"c:\Users\NITRO\PROFE7\hifi_wireframe_jeron_opjer.png"
out_png_artifact = r"C:\Users\NITRO\.gemini\antigravity-ide\brain\6be15b9e-35b8-446a-93fe-83cb646ff231\hifi_wireframe_jeron_opjer.png"

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=1.5",
    "--window-size=1080,1280",
    f"--screenshot={out_png_workspace}",
    f"file:///{html_file.replace(chr(92), '/')}"
]

print("Running command...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Returncode:", res.returncode)

if os.path.exists(out_png_workspace):
    size = os.path.getsize(out_png_workspace)
    print(f"Success! Generated {out_png_workspace} ({size} bytes)")
    import shutil
    shutil.copyfile(out_png_workspace, out_png_artifact)
    print(f"Copied to artifact path: {out_png_artifact}")
else:
    print("Screenshot failed, stdout:", res.stdout, "stderr:", res.stderr)
