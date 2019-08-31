%global packname  LPKsample
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          LP Nonparametric High Dimensional K-Sample Comparison

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mclust 
Requires:         R-CRAN-apcluster 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mclust 

%description
LP nonparametric high-dimensional K-sample comparison method that includes
(i) confirmatory test, (ii) exploratory analysis, and (iii) options to
output a data-driven LP-transformed matrix for classification. The primary
reference is Mukhopadhyay, S. and Wang, K. (2018, Technical Report).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX