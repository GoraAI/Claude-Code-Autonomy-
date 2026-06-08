import cv2
import numpy as np
import os
import glob
from pathlib import Path

INPUT_DIR = '/home/user/Claude-Code-Autonomy-/gallery-download/images'
OUTPUT_DIR = '/home/user/Claude-Code-Autonomy-/gallery-clean/images'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def detect_watermark_mask(img):
    """
    Detect Pixieset semi-transparent watermark.
    It appears as a lighter circular overlay in the center of the image.
    """
    h, w = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Pixieset watermark is semi-transparent white/light text in center
    # Detect by looking for near-white pixels that form the logo pattern
    # Convert to float for processing
    img_f = img.astype(np.float32)

    # The watermark adds brightness - look for areas that are unusually bright
    # relative to their local surroundings
    blur = cv2.GaussianBlur(gray, (31, 31), 0)
    diff = gray.astype(np.float32) - blur.astype(np.float32)

    # Watermark pixels are brighter than their surroundings
    # Focus on center region where Pixieset places its watermark
    mask = np.zeros((h, w), dtype=np.uint8)
    center_y, center_x = h // 2, w // 2

    # Pixieset watermark covers roughly center 50% of image
    roi_y1 = int(h * 0.2)
    roi_y2 = int(h * 0.8)
    roi_x1 = int(w * 0.15)
    roi_x2 = int(w * 0.85)

    roi_diff = diff[roi_y1:roi_y2, roi_x1:roi_x2]

    # Threshold: areas significantly brighter than surroundings = watermark
    threshold = np.percentile(roi_diff, 85)
    bright_mask = (roi_diff > max(threshold, 8)).astype(np.uint8) * 255

    # Also catch the circular logo shape - use higher threshold in center
    center_roi_diff = diff[int(h*0.3):int(h*0.7), int(w*0.25):int(w*0.75)]
    center_threshold = np.percentile(center_roi_diff, 75)
    center_bright = (center_roi_diff > max(center_threshold, 5)).astype(np.uint8) * 255

    mask[roi_y1:roi_y2, roi_x1:roi_x2] = bright_mask
    mask[int(h*0.3):int(h*0.7), int(w*0.25):int(w*0.75)] |= center_bright

    # Morphological operations to clean up and expand mask slightly
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)

    return mask

def remove_watermark(img_path, out_path):
    img = cv2.imread(img_path)
    if img is None:
        return False

    mask = detect_watermark_mask(img)

    # Use OpenCV's Navier-Stokes inpainting
    result = cv2.inpaint(img, mask, inpaintRadius=5, flags=cv2.INPAINT_NS)

    cv2.imwrite(out_path, result, [cv2.IMWRITE_JPEG_QUALITY, 95])
    return True

# Process all jpgs in the images folder
images = glob.glob(f'{INPUT_DIR}/*.jpg')
images.sort()

# Skip already-clean large images (over 200KB - they don't have watermarks)
to_process = []
to_copy = []
for img_path in images:
    size = os.path.getsize(img_path)
    if size > 200000:
        to_copy.append(img_path)
    else:
        to_process.append(img_path)

print(f'Watermarked images to process: {len(to_process)}')
print(f'Clean images to copy: {len(to_copy)}')

# Copy clean images directly
import shutil
for img_path in to_copy:
    fname = os.path.basename(img_path)
    shutil.copy2(img_path, f'{OUTPUT_DIR}/{fname}')
    print(f'Copied (already clean): {fname}')

# Process watermarked images
for i, img_path in enumerate(to_process):
    fname = os.path.basename(img_path)
    out_path = f'{OUTPUT_DIR}/{fname}'
    success = remove_watermark(img_path, out_path)
    if success:
        print(f'[{i+1}/{len(to_process)}] Processed: {fname}')
    else:
        print(f'[{i+1}/{len(to_process)}] FAILED: {fname}')

print(f'\nDone! Clean images saved to {OUTPUT_DIR}')
