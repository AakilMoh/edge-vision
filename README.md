# Edge Vision — Interactive Edge Detection Visualizer

Edge Vision is a **Streamlit-based web application** that allows users to explore and visualize classic edge detection algorithms such as **Canny**, **Sobel**, and **Laplacian**.  
Users can upload any image, adjust parameters in real time, and instantly observe how edges are detected differently by each algorithm.

---

## Features
- Upload images in **JPG, PNG, or BMP** format.
- Choose between **Canny, Sobel, or Laplacian** edge detection.
- Adjust **thresholds, kernel size, and blur** dynamically.
- Real-time **side-by-side comparison** of original and processed images.
- Download processed **edge-detected images**.
- Dark modern interface themed using **Streamlit custom config**.

---

## Tech Stack

- **Python 3.x**
- **Streamlit**
- **OpenCV (cv2)**
- **NumPy**
- **Pillow (PIL)**

---

## Setup and Installation

1. **Clone the repository**:

git clone https://github.com/AakilMoh/edge-vision.git
cd edge-vision

2. **Create a virtual environment**:

python -m venv venv
#### On Windows
venv\Scripts\activate
#### On macOS/Linux
source venv/bin/activate

3. **Install dependencies:**:

pip install -r requirements.txt

---

## Running the Application

streamlit run app.py

- The app will open in your browser (default: http://localhost:8501).

- Upload an image and adjust edge detection parameters on the sidebar.

- View real-time edge detection results.

## Additional Features

- Interactive parameter adjustment using Streamlit sliders.

- Option to download processed images.

- Dark mode interface for improved visibility.

- Supports multiple edge detection algorithms simultaneously.

## Screenshots

### 1. Application Interface
![Interface 1](assets/UI%201.png)
![Interface 2](assets/UI%202.png)
*Shows the main app interface.*

### 2. Parameter Controls
![Controls](assets/Edge%20Detection%20Controls.png)
*Shows the sidebar where thresholds, kernel size, and blur are adjusted.*

### 3. Original vs Edge-Detected Images
![Output 1](assets/output%201.png)
![Output 2](assets/output%202.png)
*Side-by-side comparisons of original images and processed edge-detected images.*

## Notes

- Ensure uploaded images are in supported formats (JPG, PNG, BMP).

- Adjust thresholds, kernel size, and blur for best edge detection results.