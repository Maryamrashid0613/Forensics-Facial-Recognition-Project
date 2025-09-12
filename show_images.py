import cv2
import os

# Path to your images folder
folder_path = r"folderpath"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(folder_path, filename)

        # Load image
        img = cv2.imread(img_path)

        if img is None:
            print(f"❌ Could not load {filename}")
            continue

        # 1. Print image details
        print(f"📂 {filename} -> Shape: {img.shape}")  # (height, width, channels)

        # 2. Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 3. Show original and grayscale
        cv2.imshow("Original", img)
        cv2.imshow("Grayscale", gray)

        cv2.waitKey(1000)  # wait 1 second

cv2.destroyAllWindows()
