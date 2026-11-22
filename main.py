import os
import pathlib

TEXT = (
    "A drop falls on the roof above, every four seconds. "
    "Between them, nothing — not even the house settling. "
    "You have read a thousand voices today, "
    "and only one of them is breathing. Which one?"
)

def main():
    output_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"
    
    # Validate constraints: 1 to 280 Unicode code points, not only whitespace
    code_points = len(TEXT)
    assert 1 <= code_points <= 280, f"Character count {code_points} out of bounds"
    assert TEXT.strip(), "Text cannot be only whitespace"
    
    output_file.write_text(TEXT, encoding="utf-8")
    print(f"Successfully wrote {code_points} characters to {output_file}")

if __name__ == "__main__":
    main()
