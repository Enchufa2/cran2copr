%global packname  Ecfun
%global packver   0.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for 'Ecdat'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-tis 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-BMA 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-tis 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-stringi 
Requires:         R-methods 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-BMA 
Requires:         R-CRAN-mvtnorm 

%description
Functions and vignettes to update data sets in 'Ecdat' and to create,
manipulate, plot, and analyze those and similar data sets.

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
