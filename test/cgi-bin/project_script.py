import os
import cgi
import json

params = cgi.FieldStorage()
proj = params.getfirst('project_id', '0')

html = ''

file_path = f'C:/Users/zelej/OneDrive/Документы/GitHub/lootbug/test/projects_script/project/text{proj}.txt'
with open(file_path, 'rt', encoding='UTF-8') as file:
    html += f'<p style="color: blue;">id_proj #{proj}</p><br>'
    html += file.read()
    html += '<br>'

print('''
<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/styles/default.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/highlight.min.js"></script>      
<meta charset="utf-8"> <title>название проекта</title>
<style>
body {
    background-color: rgb(79, 228, 123);
}
.name {
    display: inline-block;
    margin-left: 40%;
}
.projeckt {
    background-color: green;
}
.script {
    border: 3px solid black;
    border-radius: 3px;
    background-color: rgba(0, 0, 0, 0.288);
}
pre {
    display: inline-block;
    border: 3px solid black;
    border-radius: 3px;
    background-color: black;
}
</style>
</head>
<body>
<font face="Arial">
<h1 class="name">название проекта</h1> 
<div class="projeckt">''' +
html +
'''
<script>
    document.addEventListener('DOMContentLoaded', () => {
      hljs.highlightBlock(document.querySelector('pre code'));
    });
</script>
</div>
<br><br><br><br><br>
</font>
</body>
</html>
''')