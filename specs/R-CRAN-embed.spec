%global packname  embed
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Recipes for Encoding Categorical Predictors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes >= 0.1.15
BuildRequires:    R-CRAN-generics >= 0.1.0
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-rsample 
Requires:         R-CRAN-recipes >= 0.1.15
Requires:         R-CRAN-generics >= 0.1.0
Requires:         R-CRAN-rstanarm 
Requires:         R-CRAN-keras 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-rsample 

%description
Predictors can be converted to one or more numeric representations using
simple generalized linear models <arXiv:1611.09477> or nonlinear models
<arXiv:1604.06737>. Most encoding methods are supervised.

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
