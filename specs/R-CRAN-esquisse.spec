%global packname  esquisse
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Explore and Visualize Your Data Interactively

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-shiny >= 1.0.0
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.1
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-shiny >= 1.0.0
Requires:         R-CRAN-shinyWidgets >= 0.4.1
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringi 
Requires:         R-grDevices 

%description
A 'shiny' gadget to create 'ggplot2' charts interactively with
drag-and-drop to map your variables. You can quickly visualize your data
accordingly to their type, export to 'PNG' or 'PowerPoint', and retrieve
the code to reproduce the chart.

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
%doc %{rlibdir}/%{packname}/assets
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/geomIcon
%doc %{rlibdir}/%{packname}/modules-examples
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
