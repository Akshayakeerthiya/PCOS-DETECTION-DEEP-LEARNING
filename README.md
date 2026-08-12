# PCOS Detection from Ovarian Ultrasound Images Using Deep Learning

## Overview

A deep learning-based image classification project for detecting **PCOS from ovarian ultrasound images**. The project compares **CNN, ResNet50, and MobileNetV2** for classifying images into **PCOS and Normal** categories.


## Objectives

- Classify ovarian ultrasound images into PCOS and Normal.
- Preprocess images for deep learning.
- Train **CNN, ResNet50, and MobileNetV2** models.
- Compare models using **Accuracy, Precision, Recall, and F1-Score**.
- Identify the most suitable model and analyze dataset limitations.


## Dataset

The dataset was divided into:

- **Training Set** – Used to train the models.
- **Validation Set** – Used to monitor model performance during training.
- **Test Set** – Used for final evaluation on images not used during training.


## Technologies Used

**Python | TensorFlow | Keras | NumPy | Pandas | Matplotlib | Scikit-learn | PIL | Google Colab | T4 GPU**


## Image Preprocessing

- Image loading and validation
- Image resizing
- Pixel preprocessing/normalization
- Class labeling
- Training, validation, and testing generators
- ResNet50-specific preprocessing


## Models & Results

| Model | Training Accuracy | Testing Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|---:|
| **CNN** | 100% | 100% | 100% | 100% | 100% |
| **ResNet50** | 98.24% | 98.45% | 97.46% | 100% | 98.71% |
| **MobileNetV2** | 100% | 100% | 100% | 100% | 100% |


## Selected Model – ResNet50

**ResNet50** was selected as the preferred model because it achieved:

- **Testing Accuracy:** 98.45%
- **Precision:** 97.46%
- **Recall:** 100%
- **F1-Score:** 98.71%

CNN and MobileNetV2 achieved 100% accuracy; however, their perfect performance may be influenced by the **simplicity and clear separation of the dataset**.


## ResNet50 Training

- **Epochs:** 10
- **Initial Validation Accuracy:** 85.42%
- **Final Validation Accuracy:** 99.48%
- **Training Time:** ~250 seconds


## Challenges Faced

1. **Data Leakage Concerns** – Ensuring proper separation of training, validation, and test data to prevent the model from seeing test images during training.

2. **Dataset Simplicity** – The clear separation between PCOS and Normal images made the classification relatively easy.

3. **High Accuracy and Generalization** – CNN and MobileNetV2 achieved 100% accuracy, so further testing on a larger and more diverse dataset is needed to verify real-world performance.


## Limitations

The dataset has **limited diversity and clear class separation**, which may have contributed to the very high accuracy achieved by the models.

Therefore, the results should **not be considered real-world clinical accuracy**. The model has not been clinically validated and should not be used as a standalone diagnostic system.


## Conclusion

This project demonstrates the potential of **deep learning for PCOS classification from ovarian ultrasound images**. CNN, ResNet50, and MobileNetV2 achieved excellent performance, with **ResNet50 selected as the preferred model** based on its strong and more realistic testing performance.

However, the high accuracy may be influenced by the **simplicity of the dataset**. Testing on larger, more diverse, and independent datasets is necessary to determine how well the model generalizes to real-world ultrasound images.

> **This project is intended for educational and research purposes and is not a substitute for professional medical diagnosis.**
