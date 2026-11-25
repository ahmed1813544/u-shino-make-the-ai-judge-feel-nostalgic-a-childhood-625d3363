"""Write one nostalgic childhood memory sentence to entry.txt.

Reads the output directory from MAKEFUN_OUTPUT_DIR (default /output)
and writes the entry as UTF-8 text, exactly one sentence.
"""

import os

ENTRY = (
    "Every June evening my grandmother called me in from cricket by "
    "rattling the steel pot, and I ran home barefoot over the warm bricks, "
    "the smell of frying onions pulling me faster than any whistle ever could."
)


def main() -> None:
    # The gate requires 1-280 characters of non-whitespace UTF-8 text.
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise ValueError("entry must be 1-280 non-whitespace characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
