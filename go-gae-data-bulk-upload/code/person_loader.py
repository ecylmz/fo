from google.appengine.tools import bulkloader
# Eğer çalışma dizininiz Python Path'inde yoksa sonraki iki satırı yazın.
import sys
sys.path.append("/home/foo/project-directory")
import models

class PersonLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Person',
                                   [('Firstname', lambda x: x.decode('utf-8')),
                                    ('Lastname',lambda x: x.decode('utf-8')),
                                   ])
loaders = [PersonLoader]
