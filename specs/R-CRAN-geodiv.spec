%global packname  geodiv
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Calculating Gradient Surface Metrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-spatial >= 7.3.11
BuildRequires:    R-parallel >= 3.5.0
BuildRequires:    R-CRAN-raster >= 2.8.4
BuildRequires:    R-CRAN-pracma >= 2.2.2
BuildRequires:    R-CRAN-zoo >= 1.8.5
BuildRequires:    R-CRAN-e1071 >= 1.7.0
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-rgdal >= 1.4
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-sf >= 0.7.4
BuildRequires:    R-CRAN-rgeos >= 0.4.3
BuildRequires:    R-CRAN-phonTools >= 0.2.2.1
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-spatial >= 7.3.11
Requires:         R-parallel >= 3.5.0
Requires:         R-CRAN-raster >= 2.8.4
Requires:         R-CRAN-pracma >= 2.2.2
Requires:         R-CRAN-zoo >= 1.8.5
Requires:         R-CRAN-e1071 >= 1.7.0
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-rgdal >= 1.4
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-sf >= 0.7.4
Requires:         R-CRAN-rgeos >= 0.4.3
Requires:         R-CRAN-phonTools >= 0.2.2.1

%description
Methods for calculating gradient surface metrics for continuous analysis
of landscape features.

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
