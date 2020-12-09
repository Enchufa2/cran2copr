%global packname  mlpack
%global packver   3.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          'Rcpp' Integration for the 'mlpack' Library

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-BH >= 1.58
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.400.0
BuildRequires:    R-CRAN-RcppEnsmallen >= 0.2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-Rcpp >= 0.12.12

%description
A fast, flexible machine learning library, written in C++, that aims to
provide fast, extensible implementations of cutting-edge machine learning
algorithms.  See also Curtin et al. (2018) <doi:10.21105/joss.00726>.

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
