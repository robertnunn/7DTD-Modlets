import os
import shutil

current_alpha = 18
folder_path = f'Alpha {str(current_alpha)}'
folder_scan = os.scandir(folder_path)
folder_list = []

for i in folder_scan:
    if i.name.startswith('A18 - ') and i.is_dir():
        # print(i.name)
        folder_list.append(i.name)

for i in folder_list:
    shutil.make_archive(f'{folder_path}/{i}', 'zip', folder_path, i)
    shutil.move(f'{folder_path}/{i}.zip', f'{folder_path}/{i}/{i}.zip')
# print(folder_list)
    

# (the path+name of the new file[minus ext], file extension/format, parent folder, folder to zip)
# shutil.make_archive('Alpha 18/A18 - test2', 'zip', 'Alpha 18', 'A18 - Entrenching Tool')

# zip_path = 'A18 - Entrenching Tool'
# zip_path = 'Alpha 18/A18 - test2'
# source = folder_path+'A18 - Entrenching Tool'
# destination = folder_path+'A18 - test.zip'
# print('source: ', source)
# print('dest: ', destination)

# def make_archive(source, destination):
#         base = os.path.basename(destination)
#         print('base: ',base)
#         name = base.split('.')[0]
#         print('name: ',name)
#         format = base.split('.')[1]
#         print('format: ', format)
#         archive_from = os.path.dirname(source)
#         print('archive_from: ', archive_from)
#         archive_to = os.path.basename(source.strip(os.sep))
#         print('archive_to: ', archive_to)
#         shutil.make_archive(name, format, archive_from, archive_to)
#         shutil.move('%s.%s'%(name,format), destination)

# make_archive(source, destination)
