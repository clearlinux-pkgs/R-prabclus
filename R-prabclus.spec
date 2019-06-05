#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-prabclus
Version  : 2.3.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/prabclus_2.3-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/prabclus_2.3-1.tar.gz
Summary  : Functions for Clustering and Testing of Presence-Absence,
Group    : Development/Tools
License  : GPL-2.0
Requires: R-bootstrap
Requires: R-mclust
Requires: R-spatialreg
Requires: R-spdep
BuildRequires : R-bootstrap
BuildRequires : R-mclust
BuildRequires : R-spatialreg
BuildRequires : R-spdep
BuildRequires : buildreq-R

%description
spatial neighborhood information. Some distance measures, 
  Clustering of presence-absence, abundance and multilocus genetical data 
  for species delimitation, nearest neighbor 
  based noise detection. Genetic distances between communities.
  Tests whether various distance-based regressions
  are equal. Try package?prabclus for on overview.

%prep
%setup -q -c -n prabclus

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559700696

%install
export SOURCE_DATE_EPOCH=1559700696
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prabclus
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prabclus
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library prabclus
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc prabclus || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/prabclus/DESCRIPTION
/usr/lib64/R/library/prabclus/INDEX
/usr/lib64/R/library/prabclus/Meta/Rd.rds
/usr/lib64/R/library/prabclus/Meta/data.rds
/usr/lib64/R/library/prabclus/Meta/features.rds
/usr/lib64/R/library/prabclus/Meta/hsearch.rds
/usr/lib64/R/library/prabclus/Meta/links.rds
/usr/lib64/R/library/prabclus/Meta/nsInfo.rds
/usr/lib64/R/library/prabclus/Meta/package.rds
/usr/lib64/R/library/prabclus/NAMESPACE
/usr/lib64/R/library/prabclus/R/prabclus
/usr/lib64/R/library/prabclus/R/prabclus.rdb
/usr/lib64/R/library/prabclus/R/prabclus.rdx
/usr/lib64/R/library/prabclus/data/kykladspecreg.rda
/usr/lib64/R/library/prabclus/data/kykladspecreg.txt.gz
/usr/lib64/R/library/prabclus/data/nb.rda
/usr/lib64/R/library/prabclus/data/siskiyou.rda
/usr/lib64/R/library/prabclus/data/tetragonula.rda
/usr/lib64/R/library/prabclus/data/veronica.rda
/usr/lib64/R/library/prabclus/data/waterdist.rda
/usr/lib64/R/library/prabclus/data/waterdist.txt.gz
/usr/lib64/R/library/prabclus/extdata/00Index.old
/usr/lib64/R/library/prabclus/extdata/Franck04koord.txt
/usr/lib64/R/library/prabclus/extdata/Heterotrigona_indoFO.txt
/usr/lib64/R/library/prabclus/extdata/LeiMik1.txt
/usr/lib64/R/library/prabclus/extdata/LeiMik1G.txt
/usr/lib64/R/library/prabclus/extdata/LeiMik1NB.txt
/usr/lib64/R/library/prabclus/extdata/MartinezKoord.txt
/usr/lib64/R/library/prabclus/extdata/MartinezOrtega04AFLP.txt
/usr/lib64/R/library/prabclus/extdata/nb.R
/usr/lib64/R/library/prabclus/extdata/nb.txt
/usr/lib64/R/library/prabclus/extdata/siskiyou.R
/usr/lib64/R/library/prabclus/extdata/tetragonula.R
/usr/lib64/R/library/prabclus/extdata/veronica.R
/usr/lib64/R/library/prabclus/help/AnIndex
/usr/lib64/R/library/prabclus/help/aliases.rds
/usr/lib64/R/library/prabclus/help/paths.rds
/usr/lib64/R/library/prabclus/help/prabclus.rdb
/usr/lib64/R/library/prabclus/help/prabclus.rdx
/usr/lib64/R/library/prabclus/html/00Index.html
/usr/lib64/R/library/prabclus/html/R.css
/usr/lib64/R/library/prabclus/tests/Examples/prabclus-Ex.Rout.save
/usr/lib64/R/library/prabclus/tests/donttestexamples.R
/usr/lib64/R/library/prabclus/tests/prabclustests.R
/usr/lib64/R/library/prabclus/tests/prabclustests.Rout.save
