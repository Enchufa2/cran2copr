%global packname  geiger
%global packver   2.0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6.2
Release:          1%{?dist}
Summary:          Analysis of Evolutionary Diversification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-CRAN-ape >= 3.0.6
BuildRequires:    R-CRAN-deSolve >= 1.7
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ncbit 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape >= 3.0.6
Requires:         R-CRAN-deSolve >= 1.7
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-subplex 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ncbit 
Requires:         R-CRAN-colorspace 
Requires:         R-methods 

%description
Methods for fitting macroevolutionary models to phylogenetic trees.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs