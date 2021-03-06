%global packname  fflr
%global packver   0.3.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.15
Release:          1%{?dist}%{?buildtag}
Summary:          Collect ESPN Fantasy Football Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-httr >= 1.4.2

%description
Format the raw data from the ESPN fantasy football API
<https://fantasy.espn.com/apis/v3/games/ffl/> into tidy tables. Scrape
data on public leagues, rosters, athletes, and matches.

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
