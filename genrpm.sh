#!/bin/bash
# Usage: ./genrpm.sh <version>

version=$1
name=listen-trailicon
SPEC_DIR=packaging

# generate source tar
mkdir -p ./build/${name}-${version}/
cp -r ./icons/ ./build/${name}-${version}/
cp -r ./packaging ./build/${name}-${version}/
cp -r ./listen.py ./build/${name}-${version}/
cp -r ./speech ./build/${name}-${version}/

cd build && tar -cvzf ${name}-${version}.tar.gz ${name}-${version}/*
# copy it where rpmbuild specs it
mv ${name}-${version}.tar.gz ~/rpmbuild/SOURCES/  && cd ..

# generate rpm package
rpmbuild -ba $SPEC_DIR/${name}.spec
