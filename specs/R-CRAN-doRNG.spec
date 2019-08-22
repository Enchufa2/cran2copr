%global packname  doRNG
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}
Summary:          Generic Reproducible Parallel Backend for 'foreach' Loops

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rngtools >= 1.3
BuildRequires:    R-CRAN-pkgmaker >= 0.20
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-rngtools >= 1.3
Requires:         R-CRAN-pkgmaker >= 0.20
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-iterators 

%description
Provides functions to perform reproducible parallel foreach loops, using
independent random streams as generated by L'Ecuyer's combined
multiple-recursive generator [L'Ecuyer (1999),
<DOI:10.1287/opre.47.1.159>]. It enables to easily convert standard
%dopar% loops into fully reproducible loops, independently of the number
of workers, the task scheduling strategy, or the chosen parallel
environment and associated foreach backend.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
