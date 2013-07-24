#! /bin/bash

TYM=$(curl http://metadata/computeMetadata/v1beta1/instance/attributes/tym)
INSTANCE_INDEX=$(curl http://metadata/computeMetadata/v1beta1/instance/attributes/iid)
TOTAL_INSTANCES=$(curl http://metadata/computeMetadata/v1beta1/instance/attributes/ti)

python //home/chartboost/load.py $TYM $INSTANCE_INDEX $TOTAL_INSTANCES 

gcutil deleteinstance -f mw$INSTANCE_INDEX

