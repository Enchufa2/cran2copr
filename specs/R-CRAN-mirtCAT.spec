%global packname  mirtCAT
%global packver   1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Computerized Adaptive Testing with Multidimensional ItemResponse Theory

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mirt >= 1.25
BuildRequires:    R-CRAN-shiny >= 1.0.1
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mirt >= 1.25
Requires:         R-CRAN-shiny >= 1.0.1
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-lpSolve 

%description
Provides tools to generate an HTML interface for creating adaptive and
non-adaptive educational and psychological tests using the shiny package
(Chalmers (2016) <doi:10.18637/jss.v071.i05>). Suitable for applying
unidimensional and multidimensional computerized adaptive tests (CAT)
using item response theory methodology and for creating simple
questionnaires forms to collect response data directly in R. Additionally,
optimal test designs (e.g., "shadow testing") are supported for tests
which contain a large number of item selection constraints. Finally,
package contains tools useful for performing Monte Carlo simulations for
studying the behavior of computerized adaptive test banks.

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
