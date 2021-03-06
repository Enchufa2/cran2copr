%global packname  tipr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tipping Point Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 

%description
The strength of evidence provided by epidemiological and observational
studies is inherently limited by the potential for unmeasured confounding.
We focus on three key quantities: the observed bound of the confidence
interval closest to the null, a plausible residual effect size for an
unmeasured continuous or binary confounder, and a realistic mean
difference or prevalence difference for this hypothetical confounder.
Building on the methods put forth by Lin, Psaty, & Kronmal (1998)
DOI:10.2307/2533848, we can use these quantities to assess how an
unmeasured confounder may tip our result to insignificance, rendering the
study inconclusive.

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
