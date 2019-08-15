%global packname  ggplot2
%global packver   3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          1%{?dist}
Summary:          Create Elegant Data Visualisations Using the Grammar of Graphics

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-withr >= 2.0.0
BuildRequires:    R-CRAN-scales >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-gtable >= 0.1.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-withr >= 2.0.0
Requires:         R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-gtable >= 0.1.1
Requires:         R-CRAN-digest 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-lazyeval 
Requires:         R-MASS 
Requires:         R-mgcv 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-viridisLite 

%description
A system for 'declaratively' creating graphics, based on "The Grammar of
Graphics". You provide the data, tell 'ggplot2' how to map variables to
aesthetics, what graphical primitives to use, and it takes care of the
details.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX