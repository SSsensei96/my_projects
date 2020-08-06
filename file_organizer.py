import os
import shutil

path = "C:\\Users\\Шиндоус\\Downloads\\"
names = os.listdir(path)
folder_name = ['archives', 'torrents', 'pictures', 'text documents', 'other files']

possible_archives = [".zip", ".rar", ".7z"]
possible_pictures = [".png", ".jpg", ".jpeg", ".bmp"]
possible_text_documents = [".pdf", ".docx", ".doc", ".txt"]
others = [possible_archives, possible_pictures, possible_text_documents]

for i in others:
    for other in i:
        pass

for i in range(0, 5):
    new_paths = os.path.join(path, folder_name[i])

    if not os.path.exists(new_paths):
        os.makedirs(new_paths)

for files in names:
    files_directory = os.path.join(path, files)

    if ".torrent" in files and not os.path.exists(path + "torrents\\" + files):
        shutil.move(files_directory, path + "torrents\\" + files)

    for archive_format in possible_archives:
        if archive_format in files and not os.path.exists(path + "\\archives\\" + files):
            shutil.move(files_directory, path + "archives\\" + files)

    for picture_format in possible_pictures:
        if picture_format in files and not os.path.exists(path + "\\pictures\\" + files):
            shutil.move(files_directory, path + "pictures\\" + files)

    for text_doc in possible_text_documents:
        if text_doc in files and not os.path.exists(path + "\\text documents\\" + files):
            shutil.move(files_directory, path + "text documents\\" + files)
    if files not in folder_name:
        if other not in files and not os.path.exists(
                path + "\\other files\\" + files):
            shutil.move(files_directory, path + "other files\\" + files)
