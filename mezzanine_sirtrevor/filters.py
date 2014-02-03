import json
from django.template.loader import render_to_string
def json_html(value):
	html = []
	try:
		content = json.loads(value)
	except ValueError, e:
		return value
		pass	
	else:	
		for block in content['data']:
			template_name = 'sirtrevor/blocks/%s.html' % block['type']
			html.append(render_to_string(template_name, block['data']))
		return ''.join(html)
		pass