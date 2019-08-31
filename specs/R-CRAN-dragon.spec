%global packname  dragon
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Deep Time Redox Analysis of the Geobiology Ontology Network

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 

%description
Visualization and manipulation of the mineral-chemistry network across
deep time on earth.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dragon
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX