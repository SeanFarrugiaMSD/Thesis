import shutil

file_name = "Dataset/videos/violent/cam1/test1.txt"
destination = "Dataset/videos_processed/violent/cam1/"

shutil.move(file_name, destination)