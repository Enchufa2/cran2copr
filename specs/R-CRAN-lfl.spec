%global packname  lfl
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Linguistic Fuzzy Logic

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-forecast >= 5.5
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-utils 
Requires:         R-CRAN-forecast >= 5.5
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-zoo 
Requires:         R-utils 

%description
Various algorithms related to linguistic fuzzy logic: mining for
linguistic fuzzy association rules, composition of fuzzy relations,
performing perception-based logical deduction (PbLD), and forecasting
time-series using fuzzy rule-based ensemble (FRBE) - see Burda (2015)
<doi:10.1109/FUZZ-IEEE.2015.7337826>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs