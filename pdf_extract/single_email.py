import re
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("sample.pdf"):
#     for element in page_layout:
#         print(element)

text = extract_text("sample.pdf")
# print(text)

pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
matches = pattern.findall(text)
print(matches)

