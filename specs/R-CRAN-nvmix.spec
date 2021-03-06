%global packname  nvmix
%global packver   0.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Normal Variance Mixtures

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qrng 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-pcaPP 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-qrng 
Requires:         R-Matrix 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-pcaPP 

%description
Functions for working with (grouped) multivariate normal variance mixture
distributions (evaluation of distribution functions and densities, random
number generation and parameter estimation), including Student's t
distribution for non-integer degrees-of-freedom as well as the grouped t
distribution and copula with multiple degrees-of-freedom parameters. See
Hintz, Hofert, Lemieux (2019) <arXiv:1911.03017> for more details.

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
