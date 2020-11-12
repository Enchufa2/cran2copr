%global packname  vitae
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Curriculum Vitae for R Markdown

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.18
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-pillar 
Requires:         R-CRAN-rmarkdown >= 1.18
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-pillar 

%description
Provides templates and functions to simplify the production and
maintenance of curriculum vitae.

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
