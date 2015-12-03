#!/usr/bin/python
# -*- coding: utf-8 -*-

import markdown


def get_html_text(text):
    tmp = text.split("<")
    output = ""
    for t in tmp:
        x = t.split(">")
        if len(x) == 2:
            output += x[1]
    return output


def convert(source):
    html = markdown.markdown(source)
    oldpos = 0
    result = []
    for line in html.splitlines():
        text = get_html_text(line)
        newpos = source.find(text, oldpos)
        result.append(line.replace(text, source[oldpos:newpos] + text))
        oldpos = newpos
    return "".join(result)


if __name__ == '__main__':
    from PySide import QtGui
    import sys
    app = QtGui.QApplication("Markeast")
    win = QtGui.QMainWindow(None)
    text = QtGui.QTextEdit()
    with open("README.md", "r") as readme:
        text.setText(convert(readme.read()))
    win.setCentralWidget(text)
    win.setWindowTitle("Markeast")
    win.show()
    sys.exit(app.exec_())
