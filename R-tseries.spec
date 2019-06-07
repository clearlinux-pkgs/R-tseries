#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tseries
Version  : 0.10.47
Release  : 43
URL      : https://cran.r-project.org/src/contrib/tseries_0.10-47.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tseries_0.10-47.tar.gz
Summary  : Time Series Analysis and Computational Finance
Group    : Development/Tools
License  : GPL-2.0
Requires: R-tseries-lib = %{version}-%{release}
Requires: R-quadprog
Requires: R-quantmod
Requires: R-zoo
BuildRequires : R-quadprog
BuildRequires : R-quantmod
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
Package for time series analysis and computational finance
Authors:
A. Trapletti
B. LeBaron (./src/bdstest.c)
D. M. Gay (./src/dsumsl.f)

%package lib
Summary: lib components for the R-tseries package.
Group: Libraries

%description lib
lib components for the R-tseries package.


%prep
%setup -q -c -n tseries

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559897736

%install
export SOURCE_DATE_EPOCH=1559897736
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tseries
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tseries
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tseries
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tseries || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tseries/CITATION
/usr/lib64/R/library/tseries/DESCRIPTION
/usr/lib64/R/library/tseries/INDEX
/usr/lib64/R/library/tseries/Meta/Rd.rds
/usr/lib64/R/library/tseries/Meta/data.rds
/usr/lib64/R/library/tseries/Meta/features.rds
/usr/lib64/R/library/tseries/Meta/hsearch.rds
/usr/lib64/R/library/tseries/Meta/links.rds
/usr/lib64/R/library/tseries/Meta/nsInfo.rds
/usr/lib64/R/library/tseries/Meta/package.rds
/usr/lib64/R/library/tseries/NAMESPACE
/usr/lib64/R/library/tseries/R/tseries
/usr/lib64/R/library/tseries/R/tseries.rdb
/usr/lib64/R/library/tseries/R/tseries.rdx
/usr/lib64/R/library/tseries/data/NelPlo.rda
/usr/lib64/R/library/tseries/data/USeconomic.rda
/usr/lib64/R/library/tseries/data/bev.rda
/usr/lib64/R/library/tseries/data/camp.rda
/usr/lib64/R/library/tseries/data/ice.river.rda
/usr/lib64/R/library/tseries/data/nino.rda
/usr/lib64/R/library/tseries/data/tcm.rda
/usr/lib64/R/library/tseries/data/tcmd.rda
/usr/lib64/R/library/tseries/help/AnIndex
/usr/lib64/R/library/tseries/help/aliases.rds
/usr/lib64/R/library/tseries/help/paths.rds
/usr/lib64/R/library/tseries/help/tseries.rdb
/usr/lib64/R/library/tseries/help/tseries.rdx
/usr/lib64/R/library/tseries/html/00Index.html
/usr/lib64/R/library/tseries/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tseries/libs/tseries.so
/usr/lib64/R/library/tseries/libs/tseries.so.avx2
/usr/lib64/R/library/tseries/libs/tseries.so.avx512
