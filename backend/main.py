import cv2
from PIL import Image
import imagehash

# ---------------- FRAME EXTRACTION ----------------
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
            img = Image.fromarray(frame)
            img = img.resize((256, 256))  # 🔥 important for consistency
            frames.append(img)

        count += 1

    cap.release()
    return frames


# ---------------- HASHING ----------------
def generate_hashes(frames):
    return [imagehash.phash(img) for img in frames]


# ---------------- COMPARISON ----------------
def compare_hashes(hashes1, hashes2):
    similarities = []

    for h1 in hashes1:
        min_diff = min([h1 - h2 for h2 in hashes2])  # best match
        similarity = 1 - (min_diff / 64)  # normalize
        similarities.append(similarity)

    return sum(similarities) / len(similarities) * 100 if similarities else 0


# ---------------- MAIN ----------------
video1 = "original.mp4"
video2 = "edited.mp4"

frames1 = extract_frames(video1)
frames2 = extract_frames(video2)

hashes1 = generate_hashes(frames1)
hashes2 = generate_hashes(frames2)

similarity = compare_hashes(hashes1, hashes2)

print(f"\n🔥 Match Percentage: {similarity:.2f}%")

if similarity > 60:
    print("🚨 Piracy Detected")
else:
    print("✅ Safe")