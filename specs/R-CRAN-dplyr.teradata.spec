%global packname  dplyr.teradata
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          A 'Teradata' Backend for 'dplyr'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dbplyr >= 1.4.0
BuildRequires:    R-CRAN-odbc >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-DBI >= 0.8
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-methods 
Requires:         R-CRAN-dbplyr >= 1.4.0
Requires:         R-CRAN-odbc >= 1.1.6
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-DBI >= 0.8
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-bit64 
Requires:         R-methods 

%description
A 'Teradata' backend for 'dplyr'. It makes it possible to operate
'Teradata' database
<https://www.teradata.com/products-and-services/teradata-database/> in the
same way as manipulating data frames with 'dplyr'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
