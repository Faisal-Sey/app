from flask import Flask, request
import os
import datetime
import subprocess

app = Flask(__name__)
app.debug = True

media_folder = os.path.join(os.path.abspath("."), "media")


@app.route("/", methods=["POST"])
def main():
    data = request.get_json(force=True)
    try:
        blender_file = data["blender_file"]
        image_file = data["image_file"]
        path = os.path.join(
            media_folder, str(datetime.today().date(), blender_file.split("/")[-1])
        )
        subprocess.call(["py", "-3.7", "script.py", blender_file, image_file, path])
        return {
            "success": True,
            "error": False,
            "download_link": os.path.join(
                path, "output", image_file.split("/")[-1].split(".")[0] + ".png"
            ).replace('\\', "/"),
        }
    except:
        return {
            "error": True,
            "message": "An error occurred.\nPlease ensure that the data sent contains two entries, 'blender_file', and 'image_file'",
        }


if __name__ == "__main__":
    app.run("localhost", 8080)
