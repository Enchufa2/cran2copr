%global packname  quantities
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Quantity Calculus for R Vectors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-units >= 0.6.1
BuildRequires:    R-CRAN-errors >= 0.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-utils 
Requires:         R-CRAN-units >= 0.6.1
Requires:         R-CRAN-errors >= 0.3.0
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-utils 

%description
Integration of the 'units' and 'errors' packages for a complete quantity
calculus system for R vectors, matrices and arrays, with automatic
propagation, conversion, derivation and simplification of magnitudes and
uncertainties.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs