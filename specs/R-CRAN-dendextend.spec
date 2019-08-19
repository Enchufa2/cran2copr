%global packname  dendextend
%global packver   1.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Extending 'dendrogram' Functionality in R

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.0.1
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-magrittr >= 1.0.1
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-datasets 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-viridis 

%description
Offers a set of functions for extending 'dendrogram' objects in R, letting
you visualize and compare trees of 'hierarchical clusterings'. You can (1)
Adjust a tree's graphical parameters - the color, size, type, etc of its
branches, nodes and labels. (2) Visually and statistically compare
different 'dendrograms' to one another.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX