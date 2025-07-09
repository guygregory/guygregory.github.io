import os
import re
import requests
from pathlib import Path

CDN_PATTERN = r'!\[([^\]]*)\]\((https://user-images.githubusercontent.com/[^)]+)\)'
ASSETS_DIR = Path("content/images")
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

def download_and_replace(path: Path):
    content = path.read_text(encoding='utf-8')
    updated = content
    matches = list(re.finditer(CDN_PATTERN, content))

    for i, match in enumerate(matches):
        alt_text, url = match.groups()
        ext = os.path.splitext(url)[1]
        local_name = f"{path.stem}_img{i+1}{ext}"
        local_path = ASSETS_DIR / local_name

        print(f"📥 Downloading {url} -> {local_path}")
        response = requests.get(url)
        response.raise_for_status()
        local_path.write_bytes(response.content)

        updated = updated.replace(url, str(local_path).replace('\\', '/'))

    if updated != content:
        path.write_text(updated, encoding='utf-8')
        print(f"✅ Updated {path}")

def main():
    for md_file in Path(".").rglob("*.md"):
        download_and_replace(md_file)

if __name__ == "__main__":
    main()
