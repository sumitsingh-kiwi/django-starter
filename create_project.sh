#!/bin/bash
ROOT=$(pwd)

cp -r $ROOT/sample-proj/$1 /tmp/$2$3
cd /tmp
mv $2$3/$1 $2$3/$2
zip -r $2$3.zip $2$3
rm -r $2$3
