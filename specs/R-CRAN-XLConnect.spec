%global packname  XLConnect
%global packver   0.2-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.15
Release:          1%{?dist}
Summary:          Excel Connector for R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XLConnectJars == 0.2.15
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-XLConnectJars == 0.2.15
Requires:         R-methods 
Requires:         R-CRAN-rJava 

%description
Provides comprehensive functionality to read, write and format Excel data.

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/demoFiles
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/unitTests
%doc %{rlibdir}/%{packname}/XLConnect.R
%{rlibdir}/%{packname}/INDEX