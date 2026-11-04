"""Validate generated HTML, local links, fragments, and required content."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,path):
        super().__init__(convert_charrefs=True); self.links=[]; self.ids=set(); self.title=False; self.h1=0; self.feed(path.read_text())
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: assert a['id'] not in self.ids, 'Duplicate ID'; self.ids.add(a['id'])
        if tag=='h1': self.h1+=1
        if tag=='title': self.title=True
        for key in ['href','src']:
            if key in a: self.links.append(a[key])
pages={p:Page(p) for p in ROOT.rglob('*.html') if '.git' not in p.parts}
count=0
for path,page in pages.items():
    assert page.h1==1 and page.title, f'Missing page heading/title: {path}'
    for url in page.links:
        parsed=urlsplit(url)
        if parsed.scheme or parsed.netloc: continue
        dest=(ROOT / unquote(parsed.path).lstrip('/')) if parsed.path.startswith('/') else path.parent / unquote(parsed.path)
        if dest.is_dir(): dest=dest/'index.html'
        if not parsed.path: dest=path
        assert dest.is_file(), f'Broken link: {path}: {url}'
        if parsed.fragment: assert unquote(parsed.fragment) in pages[dest].ids, f'Broken fragment: {url}'
        count+=1
assert len(pages)==7
research=(ROOT/'research/index.html').read_text()
assert 'not an accepted publication' in research
thesis=(ROOT/'research/thesis/index.html').read_text()
for fact in ['3.82','3.99','37.6%','33.3%','15,732','≈7.5K','unconfirmed']:
    assert fact in thesis
assert not list(ROOT.rglob('*.pdf')), 'Review PDFs before public release'
print(f'PASS: {len(pages)} pages; {count} local asset/link/fragment references; research status and thesis facts.')
