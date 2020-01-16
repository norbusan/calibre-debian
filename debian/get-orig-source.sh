#!/bin/sh

set -eu

# Downloads the current upstream release according to debian/changelog, removes
# some bundled software copies, non-free image and replaces the non-free prs500
# TTFs with symlinks to their free liberation fonts counterparts. This also
# updates the unpacked source tree to the new upstream version and adds the
# original non-minimized javascript source for some minified JavaScript.

V=$(dpkg-parsechangelog --show-field=Version | cut --delimiter=+ --field=1)

c_dir=calibre-${V}
c_file=calibre-${V}.tar.xz

mkdir -p debian/orig
cd debian/orig

case ${V} in
    4\.99*) url=https://download.calibre-ebook.com/betas/${c_file} ;;
    *)      url=https://download.calibre-ebook.com/${V}/${c_file} ;;
esac
wget -O ${c_file} ${url}

tar -Jxf ${c_file}

rm -f ${c_dir}/src/odf/thumbnail.py
rm -r ${c_dir}/resources/mathjax
tar --use-compress-program="xz -9" --sort=name --owner=0 --group=0 --numeric-owner -cf ../../../calibre_${V}+dfsg.orig.tar.xz ${c_dir}

cd ../..
rm -r debian/orig
