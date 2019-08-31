%global packname  JGR
%global packver   1.8-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.6
Release:          1%{?dist}
Summary:          Java GUI for R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.9.5
BuildRequires:    R-CRAN-JavaGD >= 0.6
Requires:         R-CRAN-rJava >= 0.9.5
Requires:         R-CRAN-JavaGD >= 0.6

%description
Java GUI for R - cross-platform, universal and unified Graphical User
Interface for R. For full functionality on Windows and Mac OS X JGR
requires a start application which depends on your OS.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/icons
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX