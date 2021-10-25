import os

root_dir = r'C:\Users\Xylon\OneDrive\Desktop\SLR\raw'
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        store_dir = r'C:\Users\Xylon\OneDrive\Desktop\SLR\mediapipe\data'
        parents = subdir.split("\\")
        dir_parent = parents[-1]
        store_parent_dir = os.path.join(store_dir, dir_parent)
        try:
            if not os.path.exists(store_parent_dir):
                os.makedirs(store_parent_dir)
        except OSError:
            print ('Error: Creating directory')

        name = file.split(".")[0]
        store_path = os.path.join(store_parent_dir, name)
        try:
            if not os.path.exists(store_path):
                os.makedirs(store_path)
        except OSError:
            print ('Error: Creating directory')

        print(store_path)
