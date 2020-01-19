%global debug_package %{nil}
%global packname  VGAMextra
%global packver   0.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Additions and Extensions of the 'VGAM' Package

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-VGAM 

%description
Extending the functionalities of the 'VGAM' package with additional
functions and datasets. At present, 'VGAMextra' comprises new family
functions (ffs) to estimate several time series models by maximum
likelihood using Fisher scoring, unlike popular packages in CRAN relying
on optim(), including ARMA-GARCH-like models, the Order-(p, d, q) ARIMAX
model (non- seasonal), the Order-(p) VAR model, error correction models
for cointegrated time series, and ARMA-structures with Student-t errors.
For independent data, new ffs to estimate the inverse- Weibull, the
inverse-gamma, the generalized beta of the second kind and the general
multivariate normal distributions are available. In addition, 'VGAMextra'
incorporates new VGLM-links for the mean-function, and the
quantile-function (as an alternative to ordinary quantile modelling) of
several 1-parameter distributions, that are compatible with the class of
VGLM/VGAM family functions. Currently, only fixed-effects models are
implemented. All functions are subject to change; see the NEWS for further
details on the latest changes.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX