%global packname  RMariaDB
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Database Interface and 'MariaDB' Driver

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    mariadb-devel
BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildRequires:    R-CRAN-DBI >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-plogr 
Requires:         R-CRAN-DBI >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-hms 
Requires:         R-methods 

%description
Implements a 'DBI'-compliant interface to 'MariaDB'
(<https://mariadb.org/>) and 'MySQL' (<https://www.mysql.com/>) databases.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs