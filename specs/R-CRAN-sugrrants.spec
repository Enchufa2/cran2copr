%global packname  sugrrants
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Supporting Graphs for Analysing Time Series

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-lubridate >= 1.7.1
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rlang >= 0.2.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-lubridate >= 1.7.1
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rlang >= 0.2.0
Requires:         R-grid 
Requires:         R-CRAN-gtable 

%description
Provides 'ggplot2' graphics for analysing time series data. It aims to fit
into the 'tidyverse' and grammar of graphics framework for handling
temporal data.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX