# first, install a python package. This one is called "markovify"
# https://github.com/jsvine/markovify

!pip install markovify
!pip install weasyprint

import markovify
from weasyprint import HTML


novel = ''
with open("twilightchristmas.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

##for i in range(5000):
  ##  novel += str(text_model.make_sentence()) + " "

for i in range(1000):

  novel += str(text_model.make_sentence()) 
  novel += str(text_model.make_sentence()) + " <br>\n "
  novel += str(text_model.make_sentence()) 
  novel += str(text_model.make_sentence()) + " <br>\n "
  novel += str(text_model.make_sentence()) 
  

html_template = f"""
<html>
  <head>
  <title>A Bloodsucker's Christmas</title>
  </head>
  <body>
  {novel}
  </body>
</html>
"""

# Finally, this line saves that template as a PDF using the HTML module of WeasyPrint
HTML(string=html_template).write_pdf("twilight_christmas_novel.pdf")
