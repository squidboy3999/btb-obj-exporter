# btb-obj-exporter

Converts various 3d model types to obj. These include:
* fbx to obj

## How to use

Run the docker container with the model files in various sub directories. When the script runs it will convert the model files into obj files and delete the orignal model files. This does not handle embeded textures at present. Ensure that all model files are backed up before proceeding as the script will delete them from the mounted directory.
