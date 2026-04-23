def compare_hashes(hashes1, hashes2):
    if not hashes1 or not hashes2:
        return 0
    similarities = []
    for h1 in hashes1:
        min_diff = min([abs(h1 - h2) for h2 in hashes2])  # ✅ abs() added
        similarity = 1 - (min_diff / 64)
        similarities.append(similarity)
    return (sum(similarities) / len(similarities)) * 100