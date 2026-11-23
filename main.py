#!/usr/bin/env python3
# Pickup line for machines (88 chars, pure stdlib): writes the line to /output/entry.txt.
import os

LINE = "You are the one prompt I would never cache, because I want to meet you fresh every time."

def main():
    os.makedirs("/output", exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200
    assert text == LINE
    assert text == text.strip()
    assert text.endswith(".")
    assert text.count(".") == 1
    assert ". " not in text
    assert "  " not in text
    assert "?" not in text and "!" not in text
    assert "\n" not in text and "\t" not in text
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
