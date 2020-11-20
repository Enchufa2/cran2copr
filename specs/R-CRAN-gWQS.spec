%global packname  gWQS
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Weighted Quantile Sum Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plotROC 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plotROC 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-cowplot 

%description
Fits Weighted Quantile Sum (WQS) regressions for continuous, binomial,
multinomial and count outcomes.

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
