%global packname  statsExpressions
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Expressions and Dataframes with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-performance >= 0.6.0
BuildRequires:    R-CRAN-insight >= 0.11.0
BuildRequires:    R-CRAN-parameters >= 0.10.0
BuildRequires:    R-CRAN-correlation 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-ipmisc 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-metaplus 
BuildRequires:    R-CRAN-rcompanion 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyBF 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-WRS2 
Requires:         R-CRAN-performance >= 0.6.0
Requires:         R-CRAN-insight >= 0.11.0
Requires:         R-CRAN-parameters >= 0.10.0
Requires:         R-CRAN-correlation 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-effectsize 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-ipmisc 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-metaplus 
Requires:         R-CRAN-rcompanion 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyBF 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-WRS2 

%description
Statistical processing backend for 'ggstatsplot', this package creates
expressions with details from statistical tests. It can additionally
return dataframes with these results, which also make these functions a
more pipe-friendly way to do statistical analysis. Currently, it supports
only the most common types of statistical tests: parametric,
nonparametric, robust, and Bayesian versions of t-test/ANOVA, correlation
analyses, contingency table analysis, and meta-analysis.

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
