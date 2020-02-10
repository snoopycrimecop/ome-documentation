#!/usr/bin/env bash
set -e
set -u
set -x

# TODO
echo no linkcheck

# from the sub-script
export WORKSPACE=${WORKSPACE:-$(pwd)}
export WORKSPACE=${WORKSPACE%/}  # Remove trailing slashes
export USER=${USER:-$(whoami)}
export OMERODIR=${WORKSPACE}/OMERO.server
export DOCVENV=${DOCVENV:-$WORKSPACE/.venv3}
export PYTHON=${PYTHON:-python}

# VARIABLES #1
MESSAGE="Update auto-generated documentation"
PUSH_COMMAND="update-submodules develop --no-ask --push develop/latest/autogen"
OPEN_PR=false
export SPHINXOPTS=-W

# Responsibilities of caller, likely omero-docs-superbuild
test -e $WORKSPACE/OMERO.server
test -e $WORKSPACE/omero-install
test -e $WORKSPACE/omeroweb-install

if [ ! -e $DOCVENV ]; then
    $PYTHON -m venv $DOCVENV
    echo You may need to manually install zeroc-ice
fi

set +u # PS1 issue
. $DOCVENV/bin/activate
set -u

python -m pip install "omero-web>=5.6.0"
python -m pip install future 'ansible<2.7'
python -m pip install "django-redis>=4.4,<4.9"
python -m pip install -U PyYAML==5.1
python -m pip install scc

cd $WORKSPACE/ome-documentation/
omero/autogen_docs

# OSX compatibility for testing
MD5SUM=md5sum
type $MD5SUM || MD5SUM=md5
SHA1SUM=sha1sum
type $SHA1SUM || SHA1SUM=shasum

cd omero
run_ant(){
    ant "$@" -Dsphinx.opts="$SPHINXOPTS" -Domero.release="$OMERO_RELEASE"
}
run_ant clean html

echo "Order deny,allow
Deny from all
Allow from 134.36
Allow from 10
Satisfy Any" > _build/.htaccess
run_ant zip
for x in $WORKSPACE/ome-documentation/omero/_build/*.zip
  do
    base=`basename $x`
    dir=`dirname $x`
    pushd "$dir"
    $MD5SUM "$base" >> "$base.md5"
    $SHA1SUM "$base" >> "$base.sha1"
    popd
done
