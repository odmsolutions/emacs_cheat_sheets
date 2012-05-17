import json
from xml.etree import ElementTree
import sys
from xml.dom import minidom

def main():
    data = json.load(sys.stdin)
    style = """
    th  {
      padding-top: 12px;
      text-align: left;
    }

    .author {
      padding-top: 0px;
      margin-top: 0px;
      font-size: smaller;
    }
    """
    html = ElementTree.Element("html")
    head = ElementTree.SubElement(html, "head")
    ElementTree.SubElement(head, "title").text = data['title']
    ElementTree.SubElement(head, "style").text = style
    body = ElementTree.SubElement(html, "body")
    ElementTree.SubElement(body, "h1").text = data['title']
    author = ElementTree.SubElement(body, "div")
    author.text = data['Author']
    author.attrib['class'] = 'author'
    desc = ElementTree.SubElement(body, "div")
    desc.text = data['Description']
    desc.attrib['class'] = 'description'
    textcolumns = ElementTree.SubElement(ElementTree.SubElement(body, "table"), "tr")
    for columndata in data['cheats']['Columns']:
        column = ElementTree.SubElement(ElementTree.SubElement(textcolumns, "td"), "table")
        for sec_title, sec_cheats in columndata.items():
            ElementTree.SubElement(ElementTree.SubElement(column, "tr"), "th", colspan="2").text = sec_title
            for key, function in sec_cheats:
                row = ElementTree.SubElement(column, "tr")
                ElementTree.SubElement(row, "td").text = key
                ElementTree.SubElement(row, "td").text = function
    
    xml = minidom.parseString(ElementTree.tostring(html, method="html"))
    print xml.toprettyxml()

main()
