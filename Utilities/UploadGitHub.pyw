from subprocess import Popen, PIPE, STDOUT # Subprocess : Exécution du fichier Batch
import os # OS : Gestion des fichiers et répertoires

username = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split('Users/')[1].split('/')[0]
repository_path = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/").split(username)[0] + username + "/Documents/GitHub/Radio-6"

p = Popen(repository_path + "/UploadGitHub.bat", shell=True, stdout=PIPE, stderr=STDOUT)
stdout, stderr = p.communicate()