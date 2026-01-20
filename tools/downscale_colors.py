from PIL import Image
import os

# =========================
# CONFIGURACIÓN
# =========================
INPUT_DIR = "assets/colors"
OUTPUT_SIZE = (32, 32)  # cambia a (24, 24) si lo prefieres

SUPPORTED_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")

# =========================
# DOWNSCALE
# =========================
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(SUPPORTED_EXTENSIONS):
        path = os.path.join(INPUT_DIR, filename)

        with Image.open(path) as img:
            img = img.convert("RGB")
            img = img.resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)
            img.save(path, optimize=True)

        print(f"Downscaled {filename} to {OUTPUT_SIZE[0]}x{OUTPUT_SIZE[1]}")

