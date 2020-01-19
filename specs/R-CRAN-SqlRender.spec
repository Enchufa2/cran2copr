%global packname  SqlRender
%global packver   1.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.3
Release:          1%{?dist}
Summary:          Rendering Parameterized SQL and Translation to Dialects

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-rJava 

%description
A rendering tool for parameterized SQL that also translates into different
SQL dialects.  These dialects include 'Microsoft Sql Server', 'Oracle',
'PostgreSql', 'Amazon RedShift', 'Apache Impala', 'IBM Netezza', 'Google
BigQuery', 'Microsoft PDW', and 'SQLite'.

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
%doc %{rlibdir}/%{packname}/csv
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/shinyApps
%doc %{rlibdir}/%{packname}/sql
%{rlibdir}/%{packname}/INDEX