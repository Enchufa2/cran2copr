%global packname  photobiology
%global packver   0.9.30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.30
Release:          1%{?dist}
Summary:          Photobiological Calculations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-zoo >= 1.8.5
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-polynom >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-splus2R >= 1.2.2
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-stats 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-zoo >= 1.8.5
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-polynom >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-splus2R >= 1.2.2
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-stats 

%description
Definitions of classes, methods, operators and functions for use in
photobiology and radiation meteorology and climatology. Calculation of
effective (weighted) and not-weighted irradiances/doses, fluence rates,
transmittance, reflectance, absorptance, absorbance and diverse ratios and
other derived quantities from spectral data. Local maxima and minima.
Conversion between energy- and photon-based units. Wavelength
interpolation. Astronomical calculations related solar angles and day
length. Colours and vision. This package is part of the 'r4photobiology'
suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX