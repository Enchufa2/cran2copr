%global packname  SDLfilter
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          2%{?dist}
Summary:          Filtering and Assessing Sample Size of Tracking Data

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotKML 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-trip 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggsn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotKML 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-trip 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggsn 
Requires:         R-stats 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-dplyr 

%description
Functions to filter GPS and/or Argos locations, as well as assessing
sample sizes for the analysis of animal distributions. The filters remove
temporal and spatial duplicates, fixes located at a given height from
estimated high tide line, and locations with high error as described in
Shimada et al. (2012) <doi:10.3354/meps09747> and Shimada et al. (2016)
<doi:10.1007/s00227-015-2771-0>. Sample sizes for the analysis of animal
distributions can be assessed by the conventional area-based approach or
the alternative probability-based approach as described in Shimada et al.
(in prep).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
