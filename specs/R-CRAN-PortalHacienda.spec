%global packname  PortalHacienda
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Acceder Con R a Los Datos Del Portal De Hacienda

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.12
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-timetk >= 2.0
BuildRequires:    R-CRAN-zoo >= 1.8.8
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-xts >= 0.12.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-forecast >= 8.12
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-timetk >= 2.0
Requires:         R-CRAN-zoo >= 1.8.8
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-xts >= 0.12.0
Requires:         R-CRAN-httr 
Requires:         R-CRAN-curl 

%description
Obtener listado de datos, acceder y extender series del Portal de Datos de
Hacienda.Las proyecciones se realizan con forecast, Datos de Hacienda.Las
proyecciones se realizan con 'forecast', Hyndman RJ, Khandakar Y (2008)
<doi:10.18637/jss.v027.i03>. Search, download and forecast time-series
from the Ministry of Economy of Argentina. Forecasts are built with the
forecast library, of Argentina. Forecasts are built with the 'forecast'
package, Hyndman RJ, Khandakar Y (2008) <doi:10.18637/jss.v027.i03>.

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
