%global packname  dmm
%global packver   2.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}
Summary:          Dyadic Mixed Model for Pedigree Data

License:          GPL-2 | GPL (>= 2) | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-nadiv 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-nadiv 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-pls 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Dyadic mixed model analysis with multi-trait responses and pedigree-based
partitioning of individual variation into a range of environmental and
genetic variance components for individual and maternal effects.

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
