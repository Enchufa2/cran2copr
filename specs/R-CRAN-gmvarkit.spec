%global packname  gmvarkit
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Gaussian Mixture Vector Autoregressive Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.0.0
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-grDevices >= 3.0.0
BuildRequires:    R-CRAN-pbapply >= 1.4.2
BuildRequires:    R-CRAN-Brobdingnag >= 1.2.4
BuildRequires:    R-CRAN-mvnfast >= 0.2.5
Requires:         R-parallel >= 3.0.0
Requires:         R-stats >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-grDevices >= 3.0.0
Requires:         R-CRAN-pbapply >= 1.4.2
Requires:         R-CRAN-Brobdingnag >= 1.2.4
Requires:         R-CRAN-mvnfast >= 0.2.5

%description
Unconstrained and constrained maximum likelihood estimation of structural
and reduced form Gaussian mixture vector autoregressive (GMVAR) model,
quantile residual tests, graphical diagnostics, simulations, forecasting,
and estimation of generalized impulse response function. Leena
Kalliovirta, Mika Meitz, Pentti Saikkonen (2016)
<doi:10.1016/j.jeconom.2016.02.012>, Savi Virolainen (2020)
<arXiv:2007.04713>.

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
