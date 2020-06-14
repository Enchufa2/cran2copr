%global packname  SensusR
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          2%{?dist}
Summary:          Sensus Analytics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggmap >= 2.6.1
BuildRequires:    R-CRAN-R.utils >= 2.3.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-lubridate >= 1.3.3
BuildRequires:    R-CRAN-openssl >= 0.9.6
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-ggmap >= 2.6.1
Requires:         R-CRAN-R.utils >= 2.3.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-lubridate >= 1.3.3
Requires:         R-CRAN-openssl >= 0.9.6
Requires:         R-CRAN-jsonlite >= 0.9.16

%description
Provides access and analytic functions for Sensus data.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
