%global packname  mstrio
%global packver   11.2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          11.2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface for 'MicroStrategy' REST API

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-openssl >= 1.4.1
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-openssl >= 1.4.1
Requires:         R-CRAN-crul 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shiny 

%description
Interface for creating data sets and extracting data through the
'MicroStrategy' REST API. Access the demo API at
<https://demo.microstrategy.com/MicroStrategyLibrary/api-docs/index.html>.

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
