import zipfile
import xml.etree.ElementTree as ET
import json

# 解压 index.jar
with zipfile.ZipFile('index.jar', 'r') as jar:
    jar.extract('index.xml')

# 解析 index.xml
tree = ET.parse('index.xml')
root = tree.getroot()

apps = []

for app in root.findall('application'):
    app_data = {
        'id': app.find('id').text,
        'name': app.find('name').text.strip(),
        'summary': app.find('summary').text.strip(),
        'desc': app.find('desc').text.strip(),
        'marketversion': app.find('marketversion').text.strip(),
        'marketvercode': app.find('marketvercode').text.strip(),
        'versionCode': None,
        'versionName': None,
        'apkName': None
    }

    packages = app.findall('package')
    if packages:
        latest_package = packages[0]
        app_data['versionCode'] = latest_package.find('versioncode').text.strip()
        app_data['versionName'] = latest_package.find('version').text.strip()
        app_data['apkName'] = latest_package.find('apkname').text.strip()

    apps.append(app_data)

# 保存 JSON 文件
with open('index.json', 'w') as json_file:
    json.dump(apps, json_file, indent=4)