from python:2.7-alpine

RUN apk update && apk add libxml2 libstdc++

RUN wget https://damassets.autodesk.net/content/dam/autodesk/www/adn/fbx/20192/fbx20192_fbxpythonsdk_linux.tar.gz -O /tmp/fbx20192_fbxpythonsdk_linux.tar.gz
RUN mkdir /python-fbx
RUN mkdir /python-fbx/install
RUN mkdir /model_files

RUN tar -zxvf /tmp/fbx20192_fbxpythonsdk_linux.tar.gz -C /python-fbx
RUN printf "yes\nn" | /python-fbx/fbx20192_fbxpythonsdk_linux /python-fbx/install

RUN cp /python-fbx/install/lib/Python27_ucs4_x64/* /usr/local/lib/python2.7/site-packages/
RUN mkdir /usr/local/lib/python2.7/site-packages/btb_obj_exporter

COPY btb_obj_exporter/* /usr/local/lib/python2.7/site-packages/btb_obj_exporter/
COPY entrypoint.sh /run/entrypoint.sh
RUN chmod +x /run/entrypoint.sh

CMD tail -f /dev/null
