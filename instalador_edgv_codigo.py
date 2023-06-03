import shutil
import os

# Caminho da pasta a ser copiada
src_folder = './edgv_3_orto'

# Caminho da pasta de destino
dst_folder = os.path.join(os.getenv('APPDATA'), 'QGIS', 'QGIS3', 'profiles', 'default', 'processing' ,'models')

# Copia a pasta
shutil.copytree(src_folder, os.path.join(dst_folder, os.path.basename(src_folder)))

print('instalacao feita com sucesso!')
