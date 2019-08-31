%global packname  adehabitatHS
%global packver   0.3.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.14
Release:          1%{?dist}
Summary:          Analysis of Habitat Selection by Animals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-adehabitatMA 
BuildRequires:    R-CRAN-adehabitatHR 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-adehabitatMA 
Requires:         R-CRAN-adehabitatHR 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
A collection of tools for the analysis of habitat selection.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs