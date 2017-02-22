from lxml import html
import requests
import os

#loading content
url='http://openframeworks.cc/documentation/graphics/ofGraphics/'
page = requests.get(url)
tree = html.fromstring(page.content)
funcs = tree.xpath('//div/h2/text()')
title = tree.xpath('//div[@id="docstitle"]/h1/text()')

#creating folders
newpath = title[0]
if not os.path.exists(newpath):
    os.makedirs(newpath)

funcs.insert(0,'')


for x in range(1,len(funcs),2):

	#formating function name
	snippet_args = ""
	void = funcs[x]
	void = void.replace("void ","")

	tab_trigger = void.split("(")[0]
	args = void.split("(")[1]
	args = args[:-1]
	func_args = args.split(",")

	#formating each argument
	for x in range(len(func_args)):
		func_args[x]="${"+str(x+1)+":"+func_args[x]+"},"
		snippet_args += func_args[x]

	#.sublime-snippet file
	snippet_file = open(newpath+"/"+tab_trigger+".sublime-snippet","w")

	#formating the snippet
	snippet = """
	<snippet>
		<content><![CDATA["""+tab_trigger+"("+snippet_args[:-1]+")"+"""]]></content>
		<tabTrigger>"""+tab_trigger+"""</tabTrigger>
		<scope>source.c++</scope>
	</snippet>
	"""

	#writting the file
	snippet_file.write(snippet)

	#closing the file
	snippet_file.close()
	

print "done!, Place "+newpath+"/ folder in ~/.config/sublime-text-3/Packages/User/"