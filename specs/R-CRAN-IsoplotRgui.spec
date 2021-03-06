%global packname  IsoplotRgui
%global packver   3.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Web Interface to 'IsoplotR'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.6.2
BuildRequires:    R-CRAN-IsoplotR >= 3.4
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-httpuv >= 1.5.4
BuildRequires:    R-CRAN-later >= 1.0
Requires:         R-grDevices >= 3.6.2
Requires:         R-CRAN-IsoplotR >= 3.4
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-httpuv >= 1.5.4
Requires:         R-CRAN-later >= 1.0

%description
Provides a graphical user interface to the 'IsoplotR' package for
radiometric geochronology. The GUI runs in an internet browser and can
either be used offline, or hosted on a server to provide online access to
the 'IsoplotR' toolbox.

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
