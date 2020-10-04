%global packname  ldsep
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linkage Disequilibrium Shrinkage Estimation for Polyploids

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ashr 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ashr 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-lpSolve 

%description
Estimate gametic or composite pairwise linkage disequilibrium (LD) in
polyploids, using either genotypes or genotype likelihoods. Support is
provided to estimate the popular measures of LD: the LD coefficient D, the
standardized LD coefficient D', and the Pearson correlation coefficient r.
All estimates are returned with corresponding standard errors. These
estimates and standard errors can then be used for shrinkage estimation.
The main functions are ldest(), mldest(), sldest(), plot.lddf(),
format_lddf(), and ldshrink().

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
