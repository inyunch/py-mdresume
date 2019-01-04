Py-MDResume 
===
**這是一個科技工作者 / 阿宅 / 工程師 / 程序員用的 markdown 履歷產生器**

## Overview
- This is a python-based markdown resume generator
- You can write Markdown, and render as HTML or output as PDF

[Imgur](https://i.imgur.com/IFE6cjP.png)

## Prerequisite
- [wkhtmltopdf](https://wkhtmltopdf.org/)
```
$ brew install wkhtmltopdf
```

## Usage
```
$ pip install -r requirements.txt
$ python manage.py -p dmeo
```

or
```
$ python manage.py -p dev -m /markdown/your-md-resume.md
```

output as PDF, it will save in ./pdf
```
$ python manage.py -p toPDF -m /markdown/your-md-resume.md
```

## Credit
- [麻省理工(MIT)的履歷寫作建議 Five Steps to Writing a Great Resume](https://gecd.mit.edu/jobs-and-internships/resumes-cvs-cover-letters-and-linkedin/resumes)
- [Fork me on GitHub – CSS ribbon](https://simonwhitaker.github.io/github-fork-ribbon-css/)
- [wyde/md-resume-generator: 阿宅的 Markdown 履歷產生器 demo:](https://github.com/wyde/md-resume-generator/)
- [Python Markdown Resume Generator | wyde's note](https://wyde.github.io/2017/10/03/Python-Markdown-Resume-Generator/)
