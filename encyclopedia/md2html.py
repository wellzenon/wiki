import re

class Md2html:
    def __init__(self, file):
        self.file = file
        with open(self.file, 'r') as file:
            self.content = file.read()
        self.convert_content()

    def convert_content(self):
        self.content = list_conversion(self.content)

        lines = self.content.splitlines()
        self.content = ''
        for line in lines:
            self.content += line_conversion(line)

def list_conversion(text):
    #convert text to <ul> html tag

    text = text.splitlines()
    result = ''
    il = 0
    for line in text:
        res = re.match('\s*' + r'(\* |\+ |- )', line)
        if res:
            if il+2 == res.span()[1]:
                result += '<ul>' + '\n'
                result += line.replace(res.group(),'<li> ', 1) + ' </li>' + '\n'
                il += 2
            elif il > res.span()[1]:
                result += '</ul>' + '\n'
                result += line.replace(res.group(),'<li> ', 1) + ' </li>' + '\n'
                il -= 2
            else:
                result += line.replace(res.group(),'<li> ', 1) + ' </li>' + '\n'
        else:
            if il > 0:
                for i in range(0, il, 2): result += '</ul>' + '\n'
                result += line + '\n'
                il = 0
            else:
                result += line + '\n'                
    return result

def line_conversion(line):
    # convert text line to html

    line = heading_conversion(line)
    line = link_conversion(line)
    line = text_conversion(line)
    return line


def heading_conversion(line):
    #convert to <h> html tag

    res = re.match('#{1,6} ', line)
    if res : 
        tag = 'h' + str(res.span(0)[1] - 1)
        return line.replace(res.group(), f'<{tag}> ', 1) + f' </{tag}> ' 
    else:
        return line

def link_conversion(line):
    #convert to <a> html tag

    res = re.search('\[.*?\]\(.*?\)', line)
    while res :
        href = re.search('\(.*?\)', line)
        anchor = re.search('\[.*?\]', line)
        line = line.replace(res.group(0), f'<a href ="{href.group(0)[1:-1]}"> {anchor.group(0)[1:-1]} </a>', 1)
        res = re.search('\[.*?\]\(.*?\)', line)
    return line
    

def text_conversion(line):
    #convert to <strong> and <em> html tag

    res = re.search('(\*\*|__)[^\*].*?(\*\*|__)', line)
    while res :
        line =  line.replace(res.group(0), f'<strong> {res.group(0)[2:-2]} </strong>', 1)
        res = re.search('(\*\*|__)[^\*].*?(\*\*|__)', line)

    res = re.search(' (\*|_)[^\*].*?(\*|_) ', line) 
    while res :
        line =  line.replace(res.group(0), f'<em> {res.group(0)[2:-2]} </em>', 1) 
        res = re.search(' (\*|_)[^\*].*?(\*|_) ', line)           
    if not line.startswith('<'): line = f'<p> {line} </p>' 
    return line