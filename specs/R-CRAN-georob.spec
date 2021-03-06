%global packname  georob
%global packver   0.3-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.13
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Geostatistical Analysis of Spatial Data

License:          GPL (>= 2) | LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RandomFields >= 3.3.6
BuildRequires:    R-CRAN-robustbase >= 0.90.2
BuildRequires:    R-CRAN-sp >= 0.9.60
BuildRequires:    R-CRAN-constrainedKriging >= 0.2.1
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-methods 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-RandomFields >= 3.3.6
Requires:         R-CRAN-robustbase >= 0.90.2
Requires:         R-CRAN-sp >= 0.9.60
Requires:         R-CRAN-constrainedKriging >= 0.2.1
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-snowfall 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-lmtest 
Requires:         R-methods 
Requires:         R-nlme 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-quantreg 

%description
Provides functions for efficiently fitting linear models with spatially
correlated errors by robust and Gaussian (Restricted) Maximum Likelihood
and for computing robust and customary point and block external-drift
Kriging predictions, along with utility functions for variogram modelling
in ad hoc geostatistical analyses, model building, model evaluation by
cross-validation, (conditional) simulation of Gaussian processes, unbiased
back-transformation of Kriging predictions of log-transformed data.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
