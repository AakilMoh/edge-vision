import cv2
import numpy as np
import streamlit as st
from PIL import Image
from io import BytesIO

# Streamlit Page Config 
st.set_page_config(page_title="Edge Vision", layout="wide")

# Applying CSS to make the theme consistent
st.markdown("""
    <style>
    /* Keep global dark style consistent with config.toml */
    .stApp {
        background-color: #0f1117;
        color: #f5f6fa;
        font-family: monospace;
    }

    /* Adjust layout padding so banner hugs top */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 1rem;
    }

    /* Headings: subtle mint tint to match primary color */
    h1, h2, h3, h4 {
        color: #1abc9c;
    }

    /* Sidebar refinement */
    [data-testid="stSidebar"] {
        background-color: #23262d;
    }

    /* Make buttons and sliders blend naturally */
    .stButton > button {
        background-color: #1abc9c;
        color: black;
        border: none;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #17a589;
        color: white;
    }

    </style>
""", unsafe_allow_html=True)


# Logo Section
banner = Image.open("assets/logo.png")
st.image(banner, use_container_width=True)

# Title and Description
st.title("EDGE VISION — Interactive Edge Detection Visualizer")
st.markdown("""### Welcome to Edge Vision
An **interactive visual lab** for exploring classic edge detection algorithms.

Upload an image, adjust parameters in real-time, and see how **Sobel**, **Laplacian**, and **Canny** reveal image edges differently.
""")

# File Upload
uploaded_file = st.file_uploader(
    "Upload an image (JPG, PNG, BMP)", 
    type=["jpg", "jpeg", "png", "bmp"]
)

if uploaded_file:

    # Converting uploaded file to OpenCV image - RGB format
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    st.sidebar.header("Edge Detection Controls")

    # Algorithm Selection -- Canny, Sobel, Laplacian
    algo = st.sidebar.radio(
        "Select Algorithm",
        ["Canny", "Sobel", "Laplacian"]
    )

    processed = None

    # CANNY Edge Detection
    if algo == "Canny":
        st.sidebar.subheader("Canny Parameters")
        lower = st.sidebar.slider("Lower Threshold", 0, 255, 50)
        upper = st.sidebar.slider("Upper Threshold", 0, 255, 150)
        ksize = st.sidebar.selectbox("Kernel Size (odd only)", [3, 5, 7])
        sigma = st.sidebar.slider("Gaussian Sigma", 0.0, 3.0, 1.0, 0.1)

        # Convert to grayscale
        gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
        blurred = cv2.GaussianBlur(gray, (ksize, ksize), sigma)
        edges = cv2.Canny(blurred, lower, upper)
        processed = edges

    # SOBEL Edge Detection
    elif algo == "Sobel":
        st.sidebar.subheader("Sobel Parameters")
        ksize = st.sidebar.selectbox("Kernel Size (odd only)", [3, 5, 7])
        direction = st.sidebar.radio("Gradient Direction", ["X", "Y", "Both"])

        gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

        dx, dy = 0, 0
        if direction == "X":
            dx, dy = 1, 0
        elif direction == "Y":
            dx, dy = 0, 1
        else:
            dx, dy = 1, 1

        sobel = cv2.Sobel(gray, cv2.CV_64F, dx, dy, ksize=ksize)
        sobel = cv2.convertScaleAbs(sobel)
        processed = sobel

    # LAPLACIAN Edge Detection
    elif algo == "Laplacian":
        st.sidebar.subheader("Laplacian Parameters")
        ksize = st.sidebar.selectbox("Kernel Size (odd only)", [1, 3, 5, 7])

        gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
        lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
        lap = cv2.convertScaleAbs(lap)
        processed = lap

    # Displaying Original and Processed Images Side by Side
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Original Image")
        st.image(image_np, use_container_width=True)

    with col2:
        st.markdown(f"### {algo} Edge Detection Result")
        st.image(processed, use_container_width=True, clamp=True)

    # Downloading Option for Processed Image
    st.markdown("### Download Processed Image")
    result_image = Image.fromarray(processed)
    buf = BytesIO()
    result_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Download Output Image",
        data=byte_im,
        file_name=f"{algo.lower()}_edges.png",
        mime="image/png"        
    )
    # Branding
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center;'>"
        "Developed with ❤️ by <b>AKEEL</b> | <b>GCU LAHORE</b>"
        "</div>",
        unsafe_allow_html=True
    )


else:
    st.info("Upload an image to get started!")
