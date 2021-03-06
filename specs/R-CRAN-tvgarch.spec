%global packname  tvgarch
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time Varying GARCH Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-garchx 
BuildRequires:    R-CRAN-hier.part 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-garchx 
Requires:         R-CRAN-hier.part 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-zoo 

%description
Simulation, estimation and inference for TV(s)-GARCH(p,q,r)-X models,
where s indicates the number and shape of the transition functions, p is
the ARCH order, q is the GARCH order, r is the asymmetry order, and 'X'
indicates that covariates can be included. The TV long-term component, as
in the multiplicative TV-GARCH model of Amado and Ter"asvirta (2013)
<doi:10.1016/j.jeconom.2013.03.006>, introduces non-stationarity in the
variance process, where the GARCH-X short-term component describes
conditional heteroscedasticity. Maximisation by parts leads to consistent
and asymptotically normal estimates.

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
