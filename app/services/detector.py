import random

def detect_symbols_mock(file_bytes: bytes, filename: str):
    # Seed based on file content + name so different images produce different outputs
    seed = len(file_bytes) + sum(ord(c) for c in filename)
    random.seed(seed)

    names = ["valve", "pump", "diffuser", "damper"]
    symbols = []

    count = random.randint(2, 6)  # different number of symbols per file

    for i in range(1, count + 1):
        w = random.randint(20, 120)   # width varies
        h = random.randint(20, 120)   # height varies

        symbols.append({
            "id": i,
            "name": random.choice(names),
            "confidence": round(random.uniform(0.75, 0.99), 2),
            "bbox": [
                random.randint(0, 1200),  # x
                random.randint(0, 800),   # y
                w,                        # width
                h                         # height
            ]
        })

    return symbols
