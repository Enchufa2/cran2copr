%global packname  carat
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Covariate-Adaptive Randomization for Clinical Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-methods 

%description
Provides functions and command-line user interface to generate allocation
sequence by covariate-adaptive randomization for clinical trials. The
package currently supports six covariate-adaptive randomization
procedures. Three hypothesis testing methods that are valid and robust
under covariate-adaptive randomization are also available in the package
to facilitate the inference for treatment effect under the included
randomization procedures. Additionally, the package provides comprehensive
and efficient tools to allow one to evaluate and compare the performance
of randomization procedures and tests based on various criteria.

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
