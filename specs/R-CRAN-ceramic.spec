%global packname  ceramic
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Online Imagery Tiles

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fs >= 1.3.0
BuildRequires:    R-CRAN-slippymath >= 0.3.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-spex 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reproj 
Requires:         R-CRAN-fs >= 1.3.0
Requires:         R-CRAN-slippymath >= 0.3.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sp 
Requires:         R-graphics 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-spex 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-utils 
Requires:         R-CRAN-reproj 

%description
Download imagery tiles to a standard cache and load the data into raster
objects. Facilities for 'AWS' terrain
<https://aws.amazon.com/public-datasets/terrain/> terrain and 'Mapbox'
<https://www.mapbox.com/> servers are provided.

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
