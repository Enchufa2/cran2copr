%global packname  spNetwork
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Analysis on Network

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-raster >= 3.0.12
BuildRequires:    R-CRAN-cubature >= 2.0.4.1
BuildRequires:    R-methods >= 1.7.1
BuildRequires:    R-CRAN-future.apply >= 1.4.0
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-igraph >= 1.2.4.2
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-spdep >= 1.1.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-maptools >= 0.9.5
BuildRequires:    R-CRAN-sf >= 0.9.0
BuildRequires:    R-CRAN-rgeos >= 0.5.2
BuildRequires:    R-CRAN-SearchTrees >= 0.5.2
BuildRequires:    R-CRAN-progressr >= 0.4.0
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-raster >= 3.0.12
Requires:         R-CRAN-cubature >= 2.0.4.1
Requires:         R-methods >= 1.7.1
Requires:         R-CRAN-future.apply >= 1.4.0
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-igraph >= 1.2.4.2
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-spdep >= 1.1.2
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-maptools >= 0.9.5
Requires:         R-CRAN-sf >= 0.9.0
Requires:         R-CRAN-rgeos >= 0.5.2
Requires:         R-CRAN-SearchTrees >= 0.5.2
Requires:         R-CRAN-progressr >= 0.4.0

%description
Perform spatial analysis on network. Allow to calculate Network Kernel
Density Estimate, and to build spatial matrices ('listw' objects like in
'spdep' package) to conduct any kind of traditional spatial analysis with
spatial weights based on reticular distances. K functions on network are
also available but still experimental. References: Okabe et al (2019)
<doi:10.1080/13658810802475491>; Okabe et al (2012,
ISBN:978-0470770818);Baddeley el al (2015, ISBN:9781482210200).

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
