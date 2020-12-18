# btb-obj-exporter

Converts various 3d model types to obj. These include:
* fbx to obj

## How to use

- To create a new docker image- in project directory:
  docker build --tag obj-exporter .

- Run the container (issues seem to exist with volume mounts in windows, so perform a copy instead) - in directory with model_files in it.
  docker run -d --name obj-ex obj-exporter
  docker cp model_files obj-ex:/
  docker exec -it obj-ex sh -c "python /usr/local/lib/python2.7/site-packages/btb_obj_exporter/model_converter.py /model_files/"

- copy out obj, mtl, and texture files
  docker cp obj-ex:/model_files model_files/done