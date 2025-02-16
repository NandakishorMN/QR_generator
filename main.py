from io import BytesIO
import streamlit as st
import qrcode
from PIL import Image

# Generate QR Code
def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")  # This is a PIL Image

    # Convert PIL image to bytes
    img_bytes = BytesIO()
    qr_img.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()  # Get byte data

    return img_bytes

st.title("QR Code Generator")

# User input
user_input = st.text_input("Enter text or URL:")

if user_input:
    qr_bytes = generate_qr(user_input)
    st.image(qr_bytes, caption="Generated QR Code", use_column_width=False)
