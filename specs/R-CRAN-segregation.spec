%global packname  segregation
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Entropy-Based Segregation Indices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-data.table 

%description
Computes entropy-based segregation indices, as developed by Theil (1971)
<isbn:978-0471858454>, with a focus on the Mutual Information Index (M)
and Theil's Information Index (H). The M, further described by Mora and
Ruiz-Castillo (2011) <doi:10.1111/j.1467-9531.2011.01237.x> and Frankel
and Volij (2011) <doi:10.1016/j.jet.2010.10.008>, is a measure of
segregation that is highly decomposable. The package provides tools to
decompose the index by units and groups (local segregation), and by within
and between terms. The package also provides a method to decompose
differences in segregation as described by Elbers (2021)
<doi:10.1177/0049124121986204> Includes standard error estimation by
bootstrapping.

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
