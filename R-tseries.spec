#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-tseries
Version  : 0.10.58
Release  : 84
URL      : https://cran.r-project.org/src/contrib/tseries_0.10-58.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tseries_0.10-58.tar.gz
Summary  : Time Series Analysis and Computational Finance
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-tseries-lib = %{version}-%{release}
Requires: R-jsonlite
Requires: R-quadprog
Requires: R-quantmod
Requires: R-zoo
BuildRequires : R-jsonlite
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
%setup -q -n tseries
pushd ..
cp -a tseries buildavx2
popd
pushd ..
cp -a tseries buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727101024

%install
export SOURCE_DATE_EPOCH=1727101024
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
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
/V3/usr/lib64/R/library/tseries/libs/tseries.so
/V4/usr/lib64/R/library/tseries/libs/tseries.so
/usr/lib64/R/library/tseries/libs/tseries.so
