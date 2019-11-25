from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler

import os
import time
import json

class Myhandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listadir(folder_to_track):
            src=folder_to_track +'/'+ filename
            new_destination=folder_destination+'/'+filename
folder_to_track='Users/Borbély/Desktop/myfolder'
folder_destination= 'Users/Borbély/Desktop/newfolder'
    
