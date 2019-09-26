%global packname  ForestTools
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Analyzing Remotely Sensed Forest Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-APfun 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-methods 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-APfun 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgeos 
Requires:         R-methods 

%description
Provides tools for analyzing remotely sensed forest data, including
functions for detecting treetops from canopy models, outlining tree crowns
and generating spatial statistics.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX