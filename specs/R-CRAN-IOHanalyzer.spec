%global packname  IOHanalyzer
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Data Analysis Part of 'IOHprofiler'

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-bsplus 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-PlayerRatings 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-bsplus 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-PlayerRatings 

%description
The data analysis module for the Iterative Optimization Heuristics
Profiler ('IOHprofiler'). This module provides statistical analysis
methods for the benchmark data generated by optimization heuristics, which
can be visualized through a web-based interface. The benchmark data is
usually generated by the experimentation module, called 'IOHexperimenter'.
'IOHanalyzer' also supports the widely used 'COCO' (Comparing Continuous
Optimisers) data format for benchmarking.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny-server
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
