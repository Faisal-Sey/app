import bpy
import os
import requests
import shutil
import sys

if len(sys.argv) < 4:
    raise Exception("Sorry, please provide three arguments")
blender_file_url = sys.argv[1]
image_file_url = sys.argv[2]
folder_name = sys.argv[3]

def download_file(file_url: str, folder_name: str) -> str:
    local_filename = os.path.join(folder_name, file_url.split("/")[-1])
    if os.path.isfile(local_filename):
        local_filename = local_filename + file_url.split("/")[-1]
    with requests.get(file_url, stream=True) as r:
        with open(local_filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename

# specify path to blender file
bpy.ops.wm.open_mainfile(filepath="C:\\Users\\user\\Desktop\\projects\\blender\\bag.blend")
blend_file_name = download_file(blender_file_url, folder_name)
bpy.ops.wm.open_mainfile(filepath=blend_file_name)

# specify the folder that contains all the images to be wrapped around the blender model
TextureFolder = os.path.abspath(os.path.curdir)
TextureFolder = folder_name

os.makedirs(os.path.join(TextureFolder, "output"))

# To be called only after the blender model has been loaded
def obj_material_texture_UVunwrap(objname, filename):
@@ -73,9 +94,8 @@ def obj_material_texture_UVunwrap(objname, filename):
else:
    print("There is no object to render with")

# Iterate through all image files in the current folder and proceed with wrapping them
# around the model
for file in os.listdir():
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        print(f"Rendering with {file}")
        obj_material_texture_UVunwrap(obj_name, file)
    # Iterate through all image files in the current folder and proceed with wrapping them
    # around the model
    image_location = download_file(image_file_url, folder_name)
    obj_material_texture_UVunwrap(obj_name, image_location)