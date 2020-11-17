docker build --tag obj-exporter .
cd ..
docker run -d -v /model_files --name obj-ex obj-exporter
docker cp model_files obj-ex:/
docker exec -it obj-ex sh -c "python /usr/local/lib/python2.7/site-packages/btb_obj_exporter/model_converter.py /model_files/"
docker cp obj-ex:/model_files model_files/done