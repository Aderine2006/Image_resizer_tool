import streamlit as st
from PIL import Image
import io
import zipfile

# 🎨 App Title
st.title("📷 Batch Image Resizer Tool")
st.write("Resize multiple images at once with custom dimensions.")

# 📤 Upload images
uploaded_files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=True)

# 📏 Custom size input
col1, col2 = st.columns(2)
with col1:
    width = st.number_input("Enter Width", min_value=1, value=800)
with col2:
    height = st.number_input("Enter Height", min_value=1, value=800)

# 📌 Resize & Download button
if uploaded_files and st.button("Resize Images"):
    resized_images = []

    for file in uploaded_files:
        img = Image.open(file)
        resized_img = img.resize((width, height))
        
        # Save to memory
        img_bytes = io.BytesIO()
        resized_img.save(img_bytes, format=img.format)
        img_bytes.seek(0)
        
        resized_images.append((file.name, img_bytes))
        
        # Show preview
        st.image(resized_img, caption=f"Resized: {file.name}", use_column_width=True)

    # 📦 Create ZIP for download
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for name, img_bytes in resized_images:
            zip_file.writestr(name, img_bytes.getvalue())
    zip_buffer.seek(0)

    st.download_button(
        label="⬇️ Download All Resized Images (ZIP)",
        data=zip_buffer,
        file_name="resized_images.zip",
        mime="application/zip"
    )
