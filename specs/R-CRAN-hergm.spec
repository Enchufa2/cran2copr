%global packname  hergm
%global packver   4.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Exponential-Family Random Graph Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-latentnet 
BuildRequires:    R-CRAN-mcgibbsit 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mlergm 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-latentnet 
Requires:         R-CRAN-mcgibbsit 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-methods 
Requires:         R-CRAN-mlergm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-intergraph 
Requires:         R-parallel 
Requires:         R-CRAN-stringr 

%description
Hierarchical exponential-family random graph models with local dependence.

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
