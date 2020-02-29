%global packname  neatStats
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Neat and Painless Statistical Reporting

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-Exact 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-Exact 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 

%description
User-friendly, clear and simple statistics, primarily for publication in
psychological science. The main functions are wrappers for other packages,
but there are various additions as well. Every relevant step from data
aggregation to reportable printed statistics is covered for basic
experimental designs.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
