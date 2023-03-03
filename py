import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    def on_deleted(self, event):
        print(f"Oops! someone deleted, {event.src_path}!")
    def on_modified(self, event):
        print(f"Hey there!, {event.src_path} has been modiefied")
    def on_moved(self, event):
        print(f"Someone moved, {event.src_path}! to {event.dest_path}")

try:
    while True:
        time.sleep(2)
        print("running....")
except KeyboardInterrupt:
    print("stopped!")
    Observer.stop()