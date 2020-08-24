from bs4 import BeautifulSoup
import csv
import os


windows = True #set to 'True' only if using Windows
keep_in_folder = False #decide if you want all output CSVs to be placed in their respective chat directories, or in the same folder as this script


def read_file(filename):
    with open(filename, 'r', encoding='utf8') as file:
        raw = file.read().replace('\n', '')
        return raw

def get_text(class_name, column_name):
    html_objects = soup.findAll('div', {'class': class_name})
    objects = [column_name]
    for html_object in html_objects:
        object = html_object.text
        if(object==''):
            object = '<media>'
        if(column_name!='time'):
            object = '\''+object+'\''
        objects.append(object)
    return objects

def write_file(filename, content):
    with open(filename, 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        for row in content:
            writer.writerow(row)
        print(filename+' created')


dir = os.getcwd()
for subdir, dirs, files in os.walk(dir):
	for file in files:
		if(file[len(file)-5:] == '.html'):
			dir_char = '/'
			if(windows):
				dir_char = '\\'

			foldername = subdir[subdir.rfind(dir_char)+1:]
			html = read_file(foldername+dir_char+file) 
			soup = BeautifulSoup(html, 'html.parser')

			names = get_text('_3-96 _2pio _2lek _2lel', 'name')
			messages = get_text('_3-96 _2let', 'message')
			datetimes = get_text('_3-94 _2lem', 'time')
			datetimes.pop(1)
		    
			html_str = str(html)
			chatname = html_str[html_str.find('<title>')+7:html_str.find('</title>')]
			chatname_list = ['chat']
			for x in range(len(messages)):
				chatname_list.append(chatname)

			data = zip(chatname_list, datetimes, names, messages)
			output_filename = foldername+'_'+file[:-5]+'.csv'
			if (keep_in_folder):
				output_filename = subdir+dir_char+output_filename
			write_file(output_filename, data)

print('conversion complete')
