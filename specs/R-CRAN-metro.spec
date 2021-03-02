%global packname  metro
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Washington Metropolitan Area Transit Authority API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.4
BuildRequires:    R-CRAN-jsonlite >= 1.7.1
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-hms >= 1.0.0
BuildRequires:    R-CRAN-geodist >= 0.0.6
Requires:         R-CRAN-tibble >= 3.0.4
Requires:         R-CRAN-jsonlite >= 1.7.1
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-hms >= 1.0.0
Requires:         R-CRAN-geodist >= 0.0.6

%description
The Washington Metropolitan Area Transit Authority is a government agency
operating light rail and passenger buses in the Washington D.C. area. With
a free developer account, access their 'Metro Transparent Data Sets API'
<https://developer.wmata.com/> to return data frames of transit data for
easy analysis.

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
