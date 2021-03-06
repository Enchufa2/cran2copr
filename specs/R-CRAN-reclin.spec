%global packname  reclin
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Record Linkage Toolkit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lvec 
BuildRequires:    R-CRAN-ldat 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-lvec 
Requires:         R-CRAN-ldat 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringdist 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Rcpp 

%description
Functions to assist in performing probabilistic record linkage and
deduplication: generating pairs, comparing records, em-algorithm for
estimating m- and u-probabilities, forcing one-to-one matching. Can also
be used for pre- and post-processing for machine learning methods for
record linkage.

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
