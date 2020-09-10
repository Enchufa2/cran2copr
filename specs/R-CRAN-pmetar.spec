%global packname  pmetar
%global packver   0.2.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Processing METAR Weather Reports

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 

%description
Allows to download current and historical METAR weather reports extract
and parse basic parameters and present main weather information. Current
reports are downloaded from Aviation Weather Center
<https://www.aviationweather.gov/metar> and historical reports from Iowa
Environmental Mesonet web page of Iowa State University ASOS-AWOS-METAR
<http://mesonet.agron.iastate.edu/AWOS/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
