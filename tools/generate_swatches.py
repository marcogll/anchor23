from openai import OpenAI
import base64
import os

# =========================
# CONFIGURACIÓN API
# =========================
# Set OPENAI_API_KEY as environment variable or replace below
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")
client = OpenAI(api_key=OPENAI_API_KEY)

# =========================
# CONFIGURACIÓN
# =========================
SIZE = "1024x1024"  # Tamaño válido
OUTPUT_DIR = "assets/colors"

COLORS = {
    "bone-white": "#F6F1EC",
    "soft-cream": "#EFE7DE",
    "mocha-taupe": "#B8A89A",
    "deep-earth": "#6F5E4F",
    "charcoal-brown": "#3F362E",
}

PROMPT_TEMPLATE = (
    "A flat square color swatch, solid fill, hex color {hex}. "
    "No gradients, no texture, no shadow, no border. "
    "Minimal, neutral, technical style."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

for name, hex_color in COLORS.items():
    prompt = PROMPT_TEMPLATE.format(hex=hex_color)

    result = client.images.generate(model="gpt-image-1", prompt=prompt, size=SIZE)

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    output_path = os.path.join(OUTPUT_DIR, f"{name}.png")
    with open(output_path, "wb") as f:
        f.write(image_bytes)

    print(f"Generated {output_path}")
