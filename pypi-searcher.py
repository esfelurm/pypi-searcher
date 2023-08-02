import requests,time
def res(text):
    for char in text:
        print(char, end='', flush=True) 
        time.sleep(0.001)
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m','\033[01;35m'
cn,oe = '\033[00;36m', '\033[38;5;130m'
def print_title(title):
    res(f"\n{lrd}[{lgn}%{lrd}] \033[90m{title}")

def print_subtitle(subtitle):
    res(f"\n\n{lrd}[{lgn}#{lrd}] {yw}{subtitle}{be}\n")

def print_item(item):
    res(f"\n    {lrd}[{oe}+{lrd}] {cn}{item}")

def print_data(label, data):
    if data:
        res(f"\n    {lrd}[{gn}+{lrd}] {lgn}{label} {gn}{data}")
    else:
        res(f"\n{lrd}[{rd}+{lrd}] \033[90m{label} {lrd}N/A")

module_name = input(f"""
{pe} ____   __ __  ____   ____ 
|    \ |  T  T|    \ l    j
|  o  )|  |  ||  o  ) |  T 
|   _/ |  ~  ||   _/  |  |           
|  |   l___, ||  |    |  |           {rd}@Esfelurm{pe}
|  |   |     !|  |    j  l 
l__j   l____/ l__j   |____j
                           
{lrd}[{lgn}+{lrd}] {gn}Enter the module name : {cn}""")

response = requests.get(f"https://pypi.org/pypi/{module_name}/json")
if response.status_code == 200:
    data = response.json()

    if "info" in data:
        info = data["info"]

        print_title(info.get("name"))
        print_data("Version", info.get("version"))
        print_data("Summary", info.get("summary"))
        print_subtitle("Description")
        print(info.get("description"))

        print_subtitle("Additional Information")
        print_data("Author", info.get("author"))
        print_data("Author Email", info.get("author_email"))
        print_data("Maintainer", info.get("maintainer"))
        print_data("Maintainer Email", info.get("maintainer_email"))
        print_data("License", info.get("license"))
        print_data("Keywords", ", ".join(info.get("keywords", [])))
        print_data("Download URL", info.get("download_url"))

        platforms = info.get("platform")
        if platforms:
            print_subtitle("Platforms")
            for platform in platforms:
                print_item(platform)
        else:
            print_data("Platforms", "N/A")

        classifiers = info.get("classifiers")
        if classifiers:
            print_subtitle("Classifiers")
            for classifier in classifiers:
                print_item(classifier)
        else:
            print_data("Classifiers", "N/A")

        project_urls = info.get("project_urls")
        if project_urls:
            print_subtitle("Project URLs")
            for key, value in project_urls.items():
                print_data(key.capitalize(), value)
        else:
            print_data("Project URLs", "N/A")

        print_subtitle("Dependencies")
        requires_dist = info.get("requires_dist")
        if requires_dist:
            for require in requires_dist:
                print_item(require)
        else:
            print_data("Dependencies", "N/A")

        print_subtitle("Supported Python Versions")
        requires_python = info.get("requires_python")
        if requires_python:
            print_data("Python Versions", requires_python)
        else:
            print_data("Python Versions", "N/A")

        download_count = info.get("downloads")
        if download_count:
            print_data("Download Count", download_count.get("last_month", "N/A"))
        else:
            print_data("Download Count", "N/A")

        if "bugtrack_url" in info:
            print_data("Bug Tracker", info["bugtrack_url"])

        if "buy_url" in info:
            print_data("Buy URL", info["buy_url"])

        if "docs_url" in info:
            print_data("Documentation URL", info["docs_url"])

        if "home_page" in info:
            print_data("Home Page", info["home_page"])

        if "project_url" in info:
            print_data("Project URL", info["project_url"])

    else:
        print(f"\n{lrd}[{pe}+{lrd}] {cn}No information available for module : {lrd}{module_name}")
else:
    print(f"\n\n{lrd}[{rd}+{lrd}] {rd}There is no such module !")
