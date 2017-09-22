# Problem: You want to replace HTML or XML entities such as &entity; or &#code; with their
# corresponding text. Alternatively, you need to produce text, but escape certain characters
# (e.g. <, >, or &)

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s) # Elements are written as "<tag>text</tag>".
print(html.escape(s)) # Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.

# Disable escaping of quotes
print(html.escape(s, quote=False)) # Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".

# if you're trying to emit text as ASCII and want to embed character code entities for non-ASCII characters
s = "Spicy Jalapeño"
s.encode('ascii', errors='xmlcharrefreplace')
# b'Spicy Jalape&#241;o'


s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
p.unescape(s) # 'Spicy "Jalapeño".'

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescapse
unescape(t)
'The prompt is >>>'
