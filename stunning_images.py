# Creating stunning images with Stable Diffusion

from typing import Any
import boto3
import json
import base64
from PIL import Image
import io
import streamlit as st

# Define Amazon Bedrock
bedrock_runtime = boto3.client("bedrock-runtime")


# Amazon Bedrock api call to Stable Diffusion
def generate_image(text: str, style: str | None = None) -> Any:
    body: dict[str, Any] = {
        "text_prompts": [{"text": text}],
        "cfg_scale": 10,
        "seed": 0,
        "steps": 50,
        "style_preset": style,
    }

    if style == "None":
        del body["style_preset"]

    body_json: str = json.dumps(body)

    model_id: str = "stability.stable-diffusion-xl"
    accept: str = "application/json"
    content_type: str = "application/json"

    response = bedrock_runtime.invoke_model(
        body=body_json, modelId=model_id, accept=accept, contentType=content_type
    )

    response_body: Any = json.loads(response.get("body").read())

    results = response_body.get("artifacts")[0].get("base64")
    return results


# Turn base64 string to image with PIL
def base64_to_pil(base64_string: str):
    imgdata: bytes = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    return image


st.title("GenAI - Amazon Bedrock")
st.subheader("Stable Diffusion Demo")

sd_presets: list = [
    "None",
    "3d-model",
    "analog-film",
    "anime",
    "cinematic",
    "fantasy-art",
    "comic-book",
    "photographic",
    "digital-art",
    "texture",
    "lowpoly",
    "craft-clay",
    "isometric",
    "pixel-art",
    # "neonpunk",
    "enhance",
]
# select box for styles
style = st.selectbox("Select Style", sd_presets)
# text input
prompt = st.text_input("Enter prompt")

# Generate image from prompt
if st.button("Generate Image"):
    image = base64_to_pil(generate_image(prompt, style))
    st.image(image)
