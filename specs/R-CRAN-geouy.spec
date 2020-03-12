%global packname  geouy
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Geographic Information of Uruguay

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.2.4
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-ggsn 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-sp >= 1.2.4
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-ggsn 
Requires:         R-methods 
Requires:         R-CRAN-fs 

%description
The toolbox have functions to load and process geographic information for
Uruguay. And extra-function to get address coordinates and orthophotos
through the uruguayan 'IDE' API
<https://www.gub.uy/infraestructura-datos-espaciales/tramites-y-servicios/servicios/servicio-direcciones-geograficas>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX