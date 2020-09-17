%global packname  covr
%global packver   3.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Test Coverage for Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-withr >= 1.0.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rex 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-withr >= 1.0.2
Requires:         R-methods 
Requires:         R-CRAN-digest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rex 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-yaml 

%description
Track and report code coverage for your package and (optionally) upload
the results to a coverage service like 'Codecov' <https://codecov.io> or
'Coveralls' <https://coveralls.io>. Code coverage is a measure of the
amount of code being exercised by a set of tests. It is an indirect
measure of test quality and completeness. This package is compatible with
any testing methodology or framework and tracks coverage of both R code
and compiled C/C++/FORTRAN code.

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
