import os
import subprocess
from time import sleep

import fitz

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


if os.getlogin() == "User":
    items_to_highlight = {"BARYRK", "FBWO2", "CELEBY"}  # if YP PC

elif os.getlogin() == "Ballantrae":  # if Albany left PC
    items_to_highlight = {"ADV"}

_highlight(items_to_highlight)


# OUTPUT
doc.save(os.path.join(os.path.expanduser('~'), 'Downloads') +
         "\\output.pdf", garbage=4, deflate=True, clean=True)

doc.close()  # close as otherwise you won't be able to delete it

# print the pdf with markup
# could use win32print to print silently, but it works fine as it is
os.startfile(os.path.join(os.path.expanduser('~'),
                          'Downloads') + "\\output.pdf", "print")

sleep(20)

# now make sure to close that foxit window. It works, and closes the window no matter what
subprocess.call("taskkill /f /im FoxitReader.exe", shell=True)

sleep(15)

# now delete the input file
os.remove((os.path.expanduser('~') + "\\Downloads") + "\\MyPDF.PDF")