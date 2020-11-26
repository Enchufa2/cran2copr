%global packname  concorR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          CONCOR and Supplemental Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-sna 
Requires:         R-stats 
Requires:         R-graphics 

%description
Contains the CONCOR (CONvergence of iterated CORrelations) algorithm and a
series of supplemental functions for easy running, plotting, and
blockmodeling. The CONCOR algorithm is used on social network data to
identify network positions based off a definition of structural
equivalence; see Breiger, Boorman, and Arabie (1975)
<doi:10.1016/0022-2496(75)90028-0> and Wasserman and Faust's book Social
Network Analysis: Methods and Applications (1994). This version allows
multiple relationships for the same set of nodes and uses both incoming
and outgoing ties to find positions.

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
