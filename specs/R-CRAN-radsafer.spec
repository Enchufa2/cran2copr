%global packname  radsafer
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Radiation Safety

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RadData 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-readr 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-RadData 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 

%description
Provides functions for radiation safety, also known as "radiation
protection" and "radiological control". The science of radiation
protection is called "health physics" and its engineering functions are
called "radiological engineering". Functions in this package cover many of
the computations needed by radiation safety professionals. Examples
include: obtaining updated calibration and source check values for
radiation monitors to account for radioactive decay in a reference source,
simulating instrument readings to better understand measurement
uncertainty, correcting instrument readings for geometry and ambient
atmospheric conditions. Many of these functions are described in Johnson
and Kirby (2011, ISBN-13: 978-1609134198). Utilities are also included for
developing inputs and processing outputs with radiation transport codes,
such as MCNP, a general-purpose Monte Carlo N-Particle code that can be
used for neutron, photon, electron, or coupled neutron/photon/electron
transport (Werner et. al. (2018) <doi:10.2172/1419730>).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
