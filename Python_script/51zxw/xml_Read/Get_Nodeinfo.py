from xml.dom import minidom

#打开xml文件
dom = minidom.parse('Class_info.xml')

root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
