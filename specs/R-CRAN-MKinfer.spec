%global packname  MKinfer
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Inferential Statistics

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MKdescr 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-MKdescr 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ggplot2 

%description
Computation of various confidence intervals (Altman et al. (2000),
ISBN:978-0-727-91375-3; Hedderich and Sachs (2018),
ISBN:978-3-662-56657-2) including bootstrapped versions (Davison and
Hinkley (1997), ISBN:978-0-511-80284-3) as well as Hsu (Hedderich and
Sachs (2018), ISBN:978-3-662-56657-2), permutation (Janssen (1997),
<doi:10.1016/S0167-7152(97)00043-6>), bootstrap (Davison and Hinkley
(1997), ISBN:978-0-511-80284-3) and multiple imputation (Barnard and Rubin
(1999), <doi:10.1093/biomet/86.4.948>) t-test. Graphical visualization by
volcano plots.

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
