#!~/.virtualenvs/py-mdresume/bin/python
# -*- coding: utf-8 -*-

import mistune
import argparse
import http.server
import socketserver
import os
import pdfkit
from datetime import datetime
from pathlib import Path

def logit(msg, log_type="INFO"):
    try:
        print(' {} {} {}'.format(log_type, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  msg))
    except Exception as e:
        print(' ERROR logging' + e.message)

def generate(dest='dist'):
    with open(mdfile, 'r', encoding='utf-8') as f:
        text = f.read()

    md = mistune.Markdown()
    html = md(text)

    if dest == 'dist':
        with open('dist/index.html', 'w', encoding='utf-8') as f:
            css = '''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><link rel="stylesheet" href="../style/style.css">'''
            f.write('<html><head>' + css + '</head><body>' + html + '</body></html>')
    elif dest == 'docs':
        with open('docs/index.html', 'w', encoding='utf-8') as f:
            css = '''<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><link rel="stylesheet" href="style/style.css">'''
            fork_github = '''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.0/gh-fork-ribbon.min.css" />
                <!--[if lt IE 9]>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.0/gh-fork-ribbon.ie.min.css" />
                <![endif]-->'''
        
            ribbon = '''<a class="github-fork-ribbon" href="https://github.com/yiidtw/py-mdresume" title="Fork me on GitHub">Fork me on GitHub</a>'''
            f.write('<html><head>' + css + fork_github + '</head><body>' + ribbon + html + '</body></html>')

def serve(dest='dist'):
    web_dir = os.path.join(os.path.dirname(__file__), dest)
    port = 5050
    os.chdir(web_dir)
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    logit('serving at port: {}'.format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.shutdown()
        httpd.server_close()

def demo():
    generate('docs')
    serve('docs')

def dev():
    generate()
    serve()

def toPDF():
    generate()
    try:
        pdfkit.from_file('dist/index.html', 'pdf/resume.pdf')
    except Exception as e:
        logit('Convert to PDF failed!!', 'ERROR')

if __name__ == '__main__':
    func_list = [dev, demo, toPDF]
    func_name = [f.__name__ for f in func_list]
    func_dict = dict(zip(func_name, func_list))
	 
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--option', dest='option',  help='please specify the task to do', choices=func_name, required=True)
    parser.add_argument('-m', '--markdown-file', dest='mdfile', help='please specify the md file to render', default='markdown/demo.md')
    args = parser.parse_args()

    if not Path(args.mdfile).is_file():
        logit('File does not exists!!', 'ERROR')
        exit(1)

    global mdfile
    mdfile = args.mdfile

    f_exec = func_dict[args.option]
    f_exec()
