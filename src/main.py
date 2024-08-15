import os
import shutil
from markdown_input import *


def get_files(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    if not os.path.exists(src):
        raise Exception(f"Wrong path in get_files: {src}")

    directirys = os.listdir(path = src)
    for directory in directirys:
        src_pointer = os.path.join(src, directory)
        dst_pointer = os.path.join(dst, directory)
        if os.path.isfile(src_pointer):
            shutil.copy(src_pointer, dst_pointer)
        else:
            get_files(src_pointer, dst_pointer)

def extract_title(html_in):
    for html in html_in:
        if html.tag == "h1":
            return html.value
    raise Exception("No header 1:(main/extract_title)")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html = markdown_to_html(markdown)
    html_str = ""
    for node in html:
        html_str = f"{html_str}\n{node.to_html()}"
    title = extract_title(html)
    new_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_str)
    with open(dest_path, 'w') as f:
        f.write(new_html)

def main():
    if True:
        get_files(os.path.join('.', 'static'), os.path.join('.', 'public'))
        generate_page(os.path.join('.', 'content/index.md'), os.path.join('.', 'template.html'), os.path.join('.', 'public/index.html'))


if __name__ == "__main__":
    main()
