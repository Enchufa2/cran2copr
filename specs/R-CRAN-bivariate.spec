%global packname  bivariate
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Probability Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intoo 
BuildRequires:    R-CRAN-barsurf 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-KernSmooth 
Requires:         R-CRAN-intoo 
Requires:         R-CRAN-barsurf 
Requires:         R-CRAN-mvtnorm 
Requires:         R-KernSmooth 

%description
Convenience functions for plotting/evaluating bivariate (uniform,
binomial, Poisson, categorical, normal and bimodal) distributions,
trivariate (normal and Dirichlet) distributions, bivariate kernel density
estimates and bivariate empirical cumulative distribution functions.
Supports their probability mass functions (PMFs), probability density
functions (PDFs) and cumulative distribution functions (CDFs), generally
where applicable.

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
