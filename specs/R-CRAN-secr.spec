%global packname  secr
%global packver   4.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially Explicit Capture-Recapture

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-methods 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-raster 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-RcppNumerical 

%description
Functions to estimate the density and size of a spatially distributed
animal population sampled with an array of passive detectors, such as
traps, or by searching polygons or transects. Models incorporating
distance-dependent detection are fitted by maximizing the likelihood.
Tools are included for data manipulation and model selection.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
