from gettext import install
import json
import requests

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

# print(packages_json) this is a test 

packages_name = packages_json[0]['name']

'https://formulae.brew.sh/api/formula/a2ps.json'

packages_str = json.dumps(packages_json[0], indent=2)
print(packages_str)

installs_30 = packages_json['analystics']['install_on_request']['30d'][package_name]
