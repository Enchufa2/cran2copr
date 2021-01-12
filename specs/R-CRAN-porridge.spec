%global packname  porridge
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ridge-Type Penalized Estimation of a Potpourri of Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 

%description
The name of the package is derived from the French, 'pour' ridge, and
provides functionality for ridge-type estimation of a potpourri of models.
Currently, this estimation concerns that of various Gaussian graphical
models from different study designs. Among others it considers the regular
Gaussian graphical model and a mixture of such models. The
porridge-package implements the estimation of the former either from i)
data with replicated observations by penalized loglikelihood maximization
using the regular ridge penalty on the parameters (van Wieringen, Chen,
2019) or ii) from non-replicated data by means of the generalized ridge
estimator that allows for both the inclusion of quantitative and
qualitative prior information on the precision matrix via element-wise
penalization and shrinkage (van Wieringen, 2019,
<doi:10.1080/10618600.2019.1604374>). Additionally, the porridge-package
facilitates the ridge penalized estimation of a mixture of Gaussian
graphical models (Aflakparast et al., 2018, <doi:10.1002/bimj.201700102>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
