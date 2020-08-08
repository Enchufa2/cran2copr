%global packname  scgwr
%global packver   0.1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2.1
Release:          1%{?dist}
Summary:          Scalable Geographically Weighted Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-spData 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-optimParallel 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-spData 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-optimParallel 

%description
Fast and regularized version of GWR for large dataset, detailed in
Murakami, Tsutsumida, Yoshida, Nakaya, and Lu (2019) <arXiv:1905.00266>.

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
