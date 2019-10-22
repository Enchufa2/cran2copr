%global packname  wiqid
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Quick and Dirty Estimates for Wildlife Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-HDInterval 
Requires:         R-stats 
Requires:         R-CRAN-truncnorm 
Requires:         R-MASS 
Requires:         R-CRAN-coda 

%description
Provides simple, fast functions for maximum likelihood and Bayesian
estimates of wildlife population parameters, suitable for use with
simulated data or bootstraps. Early versions were indeed quick and dirty,
but optional error-checking routines and meaningful error messages have
been added. Includes single and multi-season occupancy, closed capture
population estimation, survival, species richness and distance measures.

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
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
