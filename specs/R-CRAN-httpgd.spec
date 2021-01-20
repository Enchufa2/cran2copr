%global packname  httpgd
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A 'HTTP' Server Graphics Device

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-BH >= 1.75.0
BuildRequires:    R-CRAN-later >= 1.1.0
BuildRequires:    R-CRAN-cpp11 >= 0.2.4
BuildRequires:    R-CRAN-systemfonts >= 0.2.3
Requires:         R-CRAN-later >= 1.1.0
Requires:         R-CRAN-cpp11 >= 0.2.4
Requires:         R-CRAN-systemfonts >= 0.2.3

%description
A graphics device for R that is accessible via network protocols. This
package was created to make it easier to embed live R graphics in
integrated development environments and other applications. The included
'HTML/JavaScript' client (plot viewer) aims to provide a better overall
user experience when dealing with R graphics. The device asynchronously
serves 'SVG' graphics via 'HTTP' and 'WebSockets'.

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
