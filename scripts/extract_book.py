import os
import re
import json
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

BASE_URL = "http://127.0.0.1:24301/8a32ad7f916a4998/OEBPS/"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
RAW_DIR = os.path.join(OUTPUT_DIR, "raw")

class HTMLToMarkdownParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = []
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attrs_dict = dict(attrs)
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.output.append(f"\n\n{'#' * level} ")
        elif tag == 'p':
            self.output.append("\n\n")
        elif tag == 'br':
            self.output.append("\n")
        elif tag == 'li':
            self.output.append("\n- ")
        elif tag == 'hr':
            self.output.append("\n\n---\n\n")
        elif tag == 'blockquote':
            self.output.append("\n\n> ")
        elif tag == 'img':
            alt = attrs_dict.get('alt', '')
            if alt and not alt.lower().startswith('cover'):
                self.output.append(f"\n*[이미지: {alt}]*\n")

    def handle_endtag(self, tag):
        self.current_tag = None
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'blockquote']:
            self.output.append(" ")

    def handle_data(self, data):
        text = data.strip()
        if text:
            self.output.append(data)

    def get_text(self):
        raw = "".join(self.output)
        cleaned = re.sub(r'\n{3,}', '\n\n', raw).strip()
        return cleaned

def fetch_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response:
        return response.read()

def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    print("1. Fetching book metadata...")
    opf_data = fetch_url(BASE_URL + "content.opf").decode('utf-8')
    toc_data = fetch_url(BASE_URL + "toc.ncx").decode('utf-8')

    root = ET.fromstring(opf_data)
    manifest = {}
    for item in root.findall('.//{http://www.idpf.org/2007/opf}item'):
        manifest[item.attrib['id']] = item.attrib['href']

    spine = []
    for itemref in root.findall('.//{http://www.idpf.org/2007/opf}itemref'):
        idref = itemref.attrib['idref']
        if idref in manifest:
            spine.append(manifest[idref])

    toc_root = ET.fromstring(toc_data)
    toc_items = []
    for nav_point in toc_root.findall('.//{http://www.daisy.org/z3986/2005/ncx/}navPoint'):
        label = nav_point.find('{http://www.daisy.org/z3986/2005/ncx/}navLabel/{http://www.daisy.org/z3986/2005/ncx/}text')
        content = nav_point.find('{http://www.daisy.org/z3986/2005/ncx/}content')
        if label is not None and content is not None:
            toc_items.append({
                'title': label.text.strip(),
                'src': content.attrib['src']
            })

    toc_file = os.path.join(OUTPUT_DIR, "book_toc.json")
    with open(toc_file, 'w', encoding='utf-8') as f:
        json.dump({'spine': spine, 'toc': toc_items}, f, ensure_ascii=False, indent=2)
    print(f"Saved TOC and spine metadata to {toc_file}")

    print(f"2. Extracting {len(spine)} spine items...")
    for idx, href in enumerate(spine):
        file_url = BASE_URL + href
        filename = os.path.basename(href)
        base_name, _ = os.path.splitext(filename)
        output_filename = f"{idx:02d}_{base_name}.md"
        output_path = os.path.join(RAW_DIR, output_filename)

        try:
            content_bytes = fetch_url(file_url)
            html_text = content_bytes.decode('utf-8', errors='replace')
            parser = HTMLToMarkdownParser()
            parser.feed(html_text)
            md_text = parser.get_text()

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# Section: {base_name}\n\n{md_text}\n")
            print(f"  [{idx+1}/{len(spine)}] Extracted {output_filename} ({len(md_text)} chars)")
        except Exception as e:
            print(f"  Error extracting {href}: {e}")

    print("Extraction complete!")

if __name__ == '__main__':
    main()
