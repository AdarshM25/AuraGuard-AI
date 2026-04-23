from PIL import Image
import imagehash

def generate_hashes(frames):
    return [imagehash.phash(img) for img in frames]