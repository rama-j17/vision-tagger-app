# -*- coding: utf-8 -*-
"""image_utils

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jUT4UCHxji674MFTRE3nFjmJh4dqcols
"""

import cv2
import numpy as np
from PIL import Image

def is_blurry_or_blank(pil_img, threshold_blur=100.0):
    """
    Check if image is blurry or blank.
    Returns (True/False, Reason)
    """
    img_cv = np.array(pil_img.convert("L"))  # grayscale

    # Check if blank (std dev too low)
    if np.std(img_cv) < 10:
        return True, "Image appears to be blank or too low contrast."

    # Check if blurry
    laplacian_var = cv2.Laplacian(img_cv, cv2.CV_64F).var()
    if laplacian_var < threshold_blur:
        return True, "Image is too blurry."

    return False, "Image is clear."