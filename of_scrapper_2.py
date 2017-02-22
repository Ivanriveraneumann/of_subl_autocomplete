from lxml import html
import requests
import os

#loading content
url='http://openframeworks.cc/documentation/'
page = requests.get(url)
tree = html.fromstring(page.content)
module_urls = tree.xpath('//li/a[@class="documentation_class_link"]/@href')
module_names = tree.xpath('//li/a[@class="documentation_class_link"]/strong/text()')


for i in xrange(len(module_urls)):

	#creating folders
	newpath = r'openframeworks/'+module_names[i]
	if not os.path.exists(newpath):
	    os.makedirs(newpath) 

	#scrapping function names inside module
	module_page=requests.get(url+module_urls[i])
	module_tree=html.fromstring(module_page.content)
	funcs = module_tree.xpath('//div/h2/text()')

	for void in funcs:
		func_name = void.replace("void ","")
		tab_trigger = func_name.split("(")[0]
		file_path =newpath+'/'+tab_trigger

		snippet_file = open(file_path+".sublime-snippet","w")

		#formating the snippet
		snippet = """
		<snippet>
			<content><![CDATA["""+func_name+"""]]></content>
			<tabTrigger>"""+tab_trigger+"""</tabTrigger>
			<!-- <scope>source.python</scope> -->
		</snippet>
		"""

		#writting the file
		snippet_file.write(snippet)

		#closing the file
		snippet_file.close()

	print "done!"
	


