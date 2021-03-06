%global packname  dplyr.teradata
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          A 'Teradata' Backend for 'dplyr'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 2.0.0
BuildRequires:    R-CRAN-odbc >= 1.3.0
BuildRequires:    R-CRAN-DBI >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-methods 
Requires:         R-CRAN-dbplyr >= 2.0.0
Requires:         R-CRAN-odbc >= 1.3.0
Requires:         R-CRAN-DBI >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-bit64 
Requires:         R-methods 

%description
A 'Teradata' backend for 'dplyr'. It makes it possible to operate
'Teradata' database
<https://www.teradata.com/products-and-services/teradata-database/> in the
same way as manipulating data frames with 'dplyr'.

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
