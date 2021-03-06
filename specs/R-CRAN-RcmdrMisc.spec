%global packname  RcmdrMisc
%global packver   2.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander Miscellaneous Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.1.0
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-readstata13 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-lattice 
Requires:         R-CRAN-Hmisc >= 4.1.0
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-utils 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-colorspace 
Requires:         R-MASS 
Requires:         R-CRAN-e1071 
Requires:         R-foreign 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-readstata13 
Requires:         R-CRAN-readxl 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-nortest 
Requires:         R-lattice 

%description
Various statistical, graphics, and data-management functions used by the
Rcmdr package in the R Commander GUI for R.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
