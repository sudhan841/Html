import cv2, numpy as np, matplotlib.pyplot as plt

def display(title, img, cmap=None):
    plt.figure(figsize=(6,6))
    plt.imshow(img if cmap is None else cv2.cvtColor(img, cmap))
    plt.title(title); plt.axis('off'); plt.show()

    def edge_activity(path);
        img = cv2.imread(path)
        if img is None: return print