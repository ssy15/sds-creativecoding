#install markovify and weasyprint


!pip install markovify
!pip install weasyprint

import markovify
from weasyprint import HTML
novel = ''

with open("christmas.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(5000):
    novel += str(text_model.make_sentence()) + " "

html_template = f"""
<html>
  <head>
  <title>ITS CHRISTMAS!!</title>
  </head>
  <body>
  {novel}
  </body>
</html>
"""

# Finally, this line saves that template as a PDF using the HTML module of WeasyPrint
HTML(string=html_template).write_pdf("christmascarol_novel.pdf")
