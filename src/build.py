# Very messy code.

import json
import os
import shutil
from collections import OrderedDict

with open("projects.json", "r") as f:
    blueprint = json.loads(f.read())
    blueprint = OrderedDict(sorted(blueprint.items()))  # Sort by key.

build_dir = os.path.abspath("./build")
shutil.rmtree(build_dir, ignore_errors=True)  # Delete old build.
os.mkdir(build_dir)


src_url = "http://www.dreamincode.net/forums/" \
          "topic/78802-martyr2s-mega-project-ideas-list/"
          
BASE_README = \
"""Martyr2's Mega Project List
======

Try to complete all the projects from [Martyr2's Mega Project List]({url}).

Try to solve them in any language of your choice, it's very educational!

==============================

""".format(url=src_url)

readme = "" + BASE_README

for catagory in blueprint:    
    readme_part = ""
    readme_part += catagory + "\n"
    readme_part += ("-" * len(catagory)) + "\n\n"
    
    for title, desc in blueprint[catagory].items():
        readme_part += "**{title}** - {desc}\n\n".format(title=title,
                                                         desc=desc)
    
    
    
    readme += readme_part
    
    catagory_dir = os.path.join(build_dir, catagory)
    os.mkdir(catagory_dir)  # Make catagory directory
    with open(os.path.join(catagory_dir, "README.md"), "w") as f:
        f.write(readme_part)  # Write catagory README

with open(os.path.join(build_dir, "README.md"), "w") as f:
    f.write(readme)
    