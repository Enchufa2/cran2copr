%global packname  bmgarch
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Multivariate GARCH Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rstan >= 2.21.2
BuildRequires:    R-CRAN-StanHeaders >= 2.18.1
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-rstantools >= 1.5.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-rstan >= 2.21.2
Requires:         R-CRAN-rstantools >= 1.5.1
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-Rdpack 

%description
Fit Bayesian multivariate GARCH models using 'Stan' for full Bayesian
inference. Generate (weighted) forecasts for means, variances (volatility)
and correlations. Currently DCC(P,Q), CCC(P,Q), pdBEKK(P,Q), and BEKK(P,Q)
parameterizations are implemented, based either on a multivariate gaussian
normal or student-t distribution. DCC and CCC models are based on Engle
(2002) <doi:10.1198/073500102288618487> and Bollerslev (1990)
<doi:10.2307/2109358>. The BEKK parameterization follows Engle and Kroner
(1995) <doi:10.1017/S0266466600009063> while the pdBEKK as well as the
estimation approach for this package is described in Rast et al. (2020)
<doi:10.31234/osf.io/j57pk>. The fitted models contain 'rstan' objects and
can be examined with 'rstan' functions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
