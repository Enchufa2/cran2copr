%global packname  rstantools
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          2%{?dist}%{?buildtag}
Summary:          Tools for Developing R Packages Interfacing with 'Stan'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-desc 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides various tools for developers of R packages interfacing with
'Stan' <https://mc-stan.org>, including functions to set up the required
package structure, S3 generics and default methods to unify function
naming across 'Stan'-based R packages, and vignettes with recommendations
for developers.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
