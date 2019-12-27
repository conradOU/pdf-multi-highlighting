import fitz
import os
import subprocess
from time import sleep

# READ IN PDF
doc = fitz.open(os.path.join(
    os.path.expanduser('~'), 'Downloads')+"\\MyPDF.PDF")
pos = 510
text_instances = []


def _highlight(items_to_highlight):
    for item in items_to_highlight:
        for page in doc:
            text_instances.extend(page.searchFor(
                item, hit_max=42, quads=True))  # 42 because that the maximum number of rooms
            # HIGHLIGHT

            for inst in text_instances:
                inst.ll.x -= pos
                inst.ul.x -= pos
                inst.lr.x = inst.ll.x+25
                inst.ur.x = inst.ul.x+25
                highlight = page.addHighlightAnnot(inst)


if os.getlogin() == "User":  # if YP PC
    items_to_highlight = {"ADV"}
    _highlight(items_to_highlight)


# OUTPUT
doc.save(os.path.join(os.path.expanduser('~'), 'Downloads') +
         "\\output.pdf", garbage=4, deflate=True, clean=True)
