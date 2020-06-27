%global packname  qtl2
%global packver   0.22-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.22.8
Release:          1%{?dist}
Summary:          Quantitative Trait Locus Mapping in Experimental Crosses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-yaml >= 2.1.13
BuildRequires:    R-CRAN-data.table >= 1.10.4.3
BuildRequires:    R-CRAN-jsonlite >= 0.9.17
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-yaml >= 2.1.13
Requires:         R-CRAN-data.table >= 1.10.4.3
Requires:         R-CRAN-jsonlite >= 0.9.17
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-RSQLite 

%description
Provides a set of tools to perform quantitative trait locus (QTL) analysis
in experimental crosses. It is a reimplementation of the 'R/qtl' package
to better handle high-dimensional data and complex cross designs. Broman
et al. (2018) <doi:10.1534/genetics.118.301595>.

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
