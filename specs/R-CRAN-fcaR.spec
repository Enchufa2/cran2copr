%global packname  fcaR
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Formal Concept Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-fractional 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-registry 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-tikzDevice 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-fractional 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-registry 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-tikzDevice 
Requires:         R-CRAN-magrittr 

%description
Provides tools to perform fuzzy formal concept analysis, presented in
Wille (1982) <doi:10.1007/978-3-642-01815-2_23> and in Ganter and Obiedkov
(2016) <doi:10.1007/978-3-662-49291-8>.  It provides functions to load and
save a formal context, extract its concept lattice and implications.  In
addition, one can use the implications to compute semantic closures of
fuzzy sets and, thus, build recommendation systems.

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
