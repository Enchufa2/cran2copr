%global packname  stream
%global packver   1.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Infrastructure for Data Stream Mining

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-CRAN-dbscan >= 1.0.0
BuildRequires:    R-CRAN-proxy >= 0.4.7
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-dbscan >= 1.0.0
Requires:         R-CRAN-proxy >= 0.4.7
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-methods 
Requires:         R-CRAN-clue 
Requires:         R-cluster 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-fpc 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-MASS 
Requires:         R-CRAN-mlbench 
Requires:         R-stats 
Requires:         R-utils 

%description
A framework for data stream modeling and associated data mining tasks such
as clustering and classification. The development of this package was
supported in part by NSF IIS-0948893 and NIH R21HG005912.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs