%global packname  UncertainInterval
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Uncertain Interval Methods for Three-Way Cut-Point Determinationin Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-zoo 

%description
Functions for the determination of an uncertain interval, that is, a range
of test scores that is inconclusive and does not allow a classification
other than 'Uncertain' (Reference: J.A. Landsheer (2016)
<doi:10.1371/journal.pone.0166007>).

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