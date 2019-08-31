%global packname  tmaptools
%global packver   2.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Thematic Map Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.7.15
BuildRequires:    R-CRAN-sf >= 0.7.1
BuildRequires:    R-CRAN-units >= 0.6.1
BuildRequires:    R-CRAN-lwgeom >= 0.1.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dichromat 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-raster >= 2.7.15
Requires:         R-CRAN-sf >= 0.7.1
Requires:         R-CRAN-units >= 0.6.1
Requires:         R-CRAN-lwgeom >= 0.1.4
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-grid 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-classInt 
Requires:         R-KernSmooth 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridisLite 
Requires:         R-stats 
Requires:         R-CRAN-dichromat 
Requires:         R-CRAN-XML 

%description
Set of tools for reading and processing spatial data. The aim is to supply
the workflow to create thematic maps. This package also facilitates
'tmap', the package for visualizing thematic maps.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX