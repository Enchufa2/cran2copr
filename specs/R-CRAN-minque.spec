%global packname  minque
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          An R Package for Linear Mixed Model Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-klaR 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-Matrix 

%description
This package offers three important components: (1) to construct a
use-defined linear mixed model, (2) to employ one of linear mixed model
approaches: minimum norm quadratic unbiased estimation (MINQUE) (Rao,
1971) for variance component estimation and random effect prediction; and
(3) to employ a jackknife resampling technique to conduct various
statistical tests. In addition, this package provides the function for
model or data evaluations.This R package offers fast computations for
large data sets analyses for various irregular data structures.

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
%{rlibdir}/%{packname}/INDEX