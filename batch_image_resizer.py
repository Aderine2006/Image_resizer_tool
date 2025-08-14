import streamlit as st #It's a python library for creating web apps 
from PIL import Image 
import io 
import zipfile

# 🎨 App Title
st.title("📷 Batch Image Resizer Tool")
st.write("Resize multiple images at once with custom dimensions.")

# 📤 Upload images
uploaded_files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=True) #This line allows users to upload multiple image files and types of file formats

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
        img_bytes = io.BytesIO() #this line creates an in-memory bytes buffer
        resized_img.save(img_bytes, format=img.format) #this line saves the resized image to the bytes buffer
        img_bytes.seek(0) #this line moves the cursor to the beginning of the bytes buffer

        resized_images.append((file.name, img_bytes)) #this line appends the image name and bytes to the list

        # Show preview
        st.image(resized_img, caption=f"Resized: {file.name}", use_column_width=True) #this line displays the resized image

    # 📦 Create ZIP for download
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file: #this line creates a new ZIP file in memory
        for name, img_bytes in resized_images:  #this line iterates over the resized images
            zip_file.writestr(name, img_bytes.getvalue()) #this line writes the image bytes to the ZIP file
    zip_buffer.seek(0) #this line moves the cursor to the beginning of the ZIP buffer

    st.download_button( #this line creates a download button for the ZIP file
        label="⬇️ Download All Resized Images (ZIP)",
        data=zip_buffer,
        file_name="resized_images.zip",
        mime="application/zip"
    )
