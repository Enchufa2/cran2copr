%global packname  heatmaply
%global packver   0.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.0
Release:          1%{?dist}
Summary:          Interactive Cluster Heat Maps Using 'plotly'

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.7.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-dendextend >= 1.12.0
BuildRequires:    R-CRAN-magrittr >= 1.0.1
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-plotly >= 4.7.1
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-dendextend >= 1.12.0
Requires:         R-CRAN-magrittr >= 1.0.1
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-seriation 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-assertthat 

%description
Create interactive cluster 'heatmaps' that can be saved as a stand- alone
HTML file, embedded in 'R Markdown' documents or in a 'Shiny' app, and
available in the 'RStudio' viewer pane. Hover the mouse pointer over a
cell to show details or drag a rectangle to zoom. A 'heatmap' is a popular
graphical method for visualizing high-dimensional data, in which a table
of numbers are encoded as a grid of colored cells. The rows and columns of
the matrix are ordered to highlight patterns and are often accompanied by
'dendrograms'. 'Heatmaps' are used in many fields for visualizing
observations, correlations, missing values patterns, and more. Interactive
'heatmaps' allow the inspection of specific value by hovering the mouse
over a cell, as well as zooming into a region of the 'heatmap' by dragging
a rectangle around the relevant area. This work is based on the 'ggplot2'
and 'plotly.js' engine. It produces similar 'heatmaps' as 'heatmap.2' or
'd3heatmap', with the advantage of speed ('plotly.js' is able to handle
larger size matrix), the ability to zoom from the 'dendrogram' panes, and
the placing of factor variables in the sides of the 'heatmap'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX