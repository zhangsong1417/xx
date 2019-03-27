from xml.dom import minidom

dom = minidom.parse('Class_info.xml')

root = dom.documentElement

tags = root.getElementsByTagName('student')
print(tags[0].nodeName)
print(tags[0].tagName)
print(tags[0].nodeType)
print(tags[0].nodeValue)

