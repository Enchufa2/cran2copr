%global packname  pdynmc
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          Moment Condition Based Estimation of Linear Dynamic Panel Data Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.4
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-optimx >= 2018.07.10
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-qlcMatrix >= 0.9.7
BuildRequires:    R-CRAN-Rdpack >= 0.11
Requires:         R-CRAN-MASS >= 7.3.51.4
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-optimx >= 2018.07.10
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-qlcMatrix >= 0.9.7
Requires:         R-CRAN-Rdpack >= 0.11

%description
Linear dynamic panel data modeling based on linear and nonlinear moment
conditions as proposed by Holtz-Eakin, Newey, and Rosen (1988)
<doi:10.2307/1913103>, Ahn and Schmidt (1995)
<doi:10.1016/0304-4076(94)01641-C>, and Arellano and Bover (1995)
<doi:10.1016/0304-4076(94)01642-D>. Estimation of the model parameters
relies on numerical optimization and the computation of closed form
solutions. For inference and specification testing, Windmeijer (2005)
<doi:10.1016/j.jeconom.2004.02.005> corrected standard errors, serial
correlation tests, tests for overidentification, and Wald tests are
available.

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
