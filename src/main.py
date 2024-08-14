import os
import shutil


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

def extract_title(markdown):




def main():
    if True:
            with open("./src/markdown_input.md") as f:
                file_contents = f.read()
    get_files(os.path.join('.', 'static'), os.path.join('.', 'public'))
    extract_title(file_contents)



if __name__ == "__main__":
    main()
