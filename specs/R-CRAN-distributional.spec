%global packname  distributional
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Vectorised Probability Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-farver 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ellipsis 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-farver 
Requires:         R-CRAN-digest 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 

%description
Vectorised distribution objects with tools for manipulating, visualising,
and using probability distributions. Designed to allow model prediction
outputs to return distributions rather than their parameters, allowing
users to directly interact with predictive distributions in a
data-oriented workflow. In addition to providing generic replacements for
p/d/q/r functions, other useful statistics can be computed including
means, variances, intervals, and highest density regions.

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
