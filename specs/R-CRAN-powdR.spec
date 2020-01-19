%global packname  powdR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Full Pattern Summation of X-Ray Powder Diffraction Data

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-nnls >= 1.4
BuildRequires:    R-CRAN-baseline >= 1.2
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-memisc >= 0.99.17
BuildRequires:    R-CRAN-reshape >= 0.8.6
BuildRequires:    R-CRAN-tidyr >= 0.8
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.3
BuildRequires:    R-CRAN-ggpubr >= 0.1.7
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-stats >= 3.4.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-nnls >= 1.4
Requires:         R-CRAN-baseline >= 1.2
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-memisc >= 0.99.17
Requires:         R-CRAN-reshape >= 0.8.6
Requires:         R-CRAN-tidyr >= 0.8
Requires:         R-CRAN-shinyWidgets >= 0.4.3
Requires:         R-CRAN-ggpubr >= 0.1.7

%description
Full pattern summation of X-ray powder diffraction data as described in
Chipera and Bish (2002) <doi:10.1107/S0021889802017405>. Derives
quantitative estimates of crystalline and amorphous phase concentrations
in complex mixtures.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX