import cv2
from PIL import Image

def extract_frames(video_path, step=10, max_frames=30):
    frames = []
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ Cannot open video:", video_path)
        return []

    count = 0

    while True:
        ret, frame = cap.read()
        if not ret or len(frames) >= max_frames:
            break

        if count % step == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 🔥 FORCE conversion
            img = Image.fromarray(frame)

            # EXTRA SAFETY (VERY IMPORTANT)
            if not isinstance(img, Image.Image):
                continue

            img = img.resize((256, 256))
            frames.append(img)

        count += 1

    cap.release()
    return frames