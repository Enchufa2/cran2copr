%global packname  asymmetry
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Multidimensional Scaling of Asymmetric Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-smacof 
Requires:         R-CRAN-gplots 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-smacof 

%description
Multidimensional scaling models and methods for the visualization for
asymmetric data <doi:10.1111/j.2044-8317.1996.tb01078.x>. An asymmetric
matrix has the same number of rows and columns, and these rows and columns
refer to the same set of objects. At least some elements in the
upper-triangle are different from the corresponding elements in the lower
triangle. An example is a student migration table, where the rows
correspond to the countries of origin of the students and the columns to
the destination countries. This package provides the slide-vector model
<doi:10.1007/BF02294474>, a scaling model with unique dimensions and the
asymscal model for asymmetric multidimensional scaling. Furthermore, a
heat map for skew-symmetric data, and the decomposition of asymmetry are
provided for the analysis of asymmetric tables.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
