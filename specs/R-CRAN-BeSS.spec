%global packname  BeSS
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          2%{?dist}%{?buildtag}
Summary:          Best Subset Selection in Linear, Logistic and CoxPH Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix >= 1.2.6
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-CRAN-glmnet 
Requires:         R-survival 

%description
An implementation of best subset selection in generalized linear model and
Cox proportional hazard model via the primal dual active set algorithm
proposed by Wen, C., Zhang, A., Quan, S. and Wang, X. (2020)
<doi:10.18637/jss.v094.i04>The algorithm formulates coefficient parameters
and residuals as primal and dual variables and utilizes efficient active
set selection strategies based on the complementarity of the primal and
dual variables.

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
