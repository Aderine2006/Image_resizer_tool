# Image_resizer_tool
A Image resizer tool which is built using the streamlit framework of python language


# 📷 Streamlit Batch Image Resizer Tool

A simple and user-friendly **web app** built with **Streamlit** and **Pillow (PIL)** that allows you to:
- Upload **multiple images** at once.
- **Resize** them to a custom width and height.
- **Preview** resized images instantly.
- Download all resized images in a **ZIP file**.

---

## 🚀 Features
- 📤 Upload multiple images at once (JPG, PNG, JPEG, WEBP).
- ✏️ Set **custom width and height**.
- 🖼 Instant preview of resized images.
- 📦 Download all resized images in one **ZIP**.
- 💻 Runs locally or can be deployed on **Streamlit Cloud**.

---

## 🛠️ Tech Stack
- **Python 3**
- [Streamlit](https://streamlit.io/)
- [Pillow (PIL)](https://python-pillow.org/)

---

## 📂 Project Structure
```

streamlit\_image\_resizer/
│
├── streamlit\_image\_resizer.py  # Main Streamlit app
├── requirements.txt            # Dependencies
└── README.md                    # Documentation

````

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/streamlit-image-resizer.git
cd streamlit-image-resizer
````

2. **Create virtual environment** (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

streamlit run streamlit_image_resizer.py

The app will open in your browser at:

http://localhost:8501


## 📥 Usage

1. Upload multiple images.
2. Enter the **desired width and height**.
3. Click **Resize Images**.
4. Preview your resized images.
5. Download them all in one ZIP file.


## 📝 License

This project is licensed under the MIT License.


## 💡 Future Improvements

* Add **"Keep Aspect Ratio"** option.
* Allow **image compression** to reduce file size.
* Support **drag-and-drop** uploads.

