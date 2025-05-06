# VisionTagger: Product Image Auto-Tagging

A web app that lets you **upload an image**, classifies it using a **pretrained deep learning model**, and shows a **Grad-CAM heatmap** to explain the prediction.

## 🚀 Features

- 🖼 Upload image and get top prediction
- 🔥 Visual explanation using Grad-CAM
- 📦 Uses PyTorch pretrained models like ResNet, VGG, etc.
- ⚡ Fast & interactive Streamlit UI

---

## 🧠 Tech Stack

- **PyTorch** – For inference and gradient operations
- **Streamlit** – For the web-based UI
- **Torchvision** – For pretrained models and transforms
- **OpenCV** & **PIL** – For image processing
- **NumPy** – For numerical computations

---

## 📁 Project Structure

vision-tagger-app/
├── app/
│ ├── app.py # Main Streamlit app
│ ├── explain_utils.py # Grad-CAM logic
│ └── utils.py # Image preprocessing
└── README.md # This file

---

## ⚙️ Setup & Usage

### 🔧 1. Clone and navigate
```bash
git clone https://github.com/yourusername/vision-tagger-app.git
cd vision-tagger-app
```
### 📦 2. Install dependencies
Make sure Python 3.8+ is installed.
```
pip install torch torchvision streamlit opencv-python numpy pillow
```
### ▶️ 3. Run the app
streamlit run app/app.py

🖼️ Sample Output
✅ Predicted Tag: Coat

🔍 Grad-CAM Heatmap showing which image regions influenced the decision.
![image](https://github.com/user-attachments/assets/b535e84b-8576-48fc-8d64-b0f7822af444)

![image](https://github.com/user-attachments/assets/8f2274c7-5101-4a04-a69c-76739cde6bc0)

📜 Included Models (Pretrained)
resnet18

## 📜 License
MIT License
© 2025 Vision Tagger Contributors

Made with ❤️ using PyTorch + Streamlit.
