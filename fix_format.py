from pathlib import Path


OUT_FOLDER = Path('out')


def searching_all_files(directory):
    dirpath = Path(directory)
    assert dirpath.is_dir()
    file_list = []
    for x in dirpath.iterdir():
        if x.is_file():
            file_list.append(x)
        elif x.is_dir():
            file_list.append(x)
            file_list.extend(searching_all_files(x))
    return file_list


def handle_hidden_file(path):
    path.unlink()


def handle_mbox_file(path):
    new_path = Path(str(path.parent).removesuffix(".sbd"))
    path.rename(new_path)
    print("mbox", path, new_path)


def handle_folder(path):
    new_path = Path(str(path) + ".sbd")
    path.rename(new_path)
    print("rename folder", path, new_path)


def handle_folder_post(path):
    new_path = Path(str(path).removesuffix(".sbd"))
    if not new_path.exists():
        new_path.touch()
        print("create empty mbox", new_path)


files = searching_all_files(OUT_FOLDER)
files.sort(reverse=True)
for e in files:
    if e.is_dir():
        handle_folder(e)

files = searching_all_files(OUT_FOLDER)
files.sort(reverse=True)
for e in files:
    if e.is_file():
        if e.name.startswith('.'):
            handle_hidden_file(e)

files = searching_all_files(OUT_FOLDER)
files.sort(reverse=True)
for e in files:
    if e.is_file():
        if e.name == 'mbox':
            handle_mbox_file(e)

files = searching_all_files(OUT_FOLDER)
files.sort(reverse=True)
for e in files:
    if e.is_dir():
        handle_folder_post(e)
