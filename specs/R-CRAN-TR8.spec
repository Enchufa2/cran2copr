%global packname  TR8
%global packver   0.9.22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.22
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for Downloading Functional Traits Data for Plant Species

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-taxize 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-taxize 

%description
Plant ecologists often need to collect "traits" data about plant species
which are often scattered among various databases: TR8 contains a set of
tools which take care of automatically retrieving some of those functional
traits data for plant species from publicly available databases (Biolflor,
The Ecological Flora of the British Isles, LEDA traitbase, Ellenberg
values for Italian Flora, Mycorrhizal intensity databases, Catminat, BROT,
PLANTS, Jepson Flora Project). The TR8 name, inspired by "car plates"
jokes, was chosen since it both reminds of the main object of the package
and is extremely short to type.

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
