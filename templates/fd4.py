from bs4 import BeautifulSoup

html = """
<html>
<head>
    <title>Example</title>
</head>
<body>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)
