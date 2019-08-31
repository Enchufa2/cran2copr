%global packname  qtl
%global packver   1.44-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.44.9
Release:          1%{?dist}
Summary:          Tools for Analyzing QTL Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Analysis of experimental crosses to identify genes (called quantitative
trait loci, QTLs) contributing to variation in quantitative traits.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/BUGS.txt
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/contrib
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/INSTALL_ME.txt
%license %{rlibdir}/%{packname}/LICENSE.txt
%doc %{rlibdir}/%{packname}/MQM-TODO.txt
%{rlibdir}/%{packname}/sampledata
%doc %{rlibdir}/%{packname}/TODO.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs