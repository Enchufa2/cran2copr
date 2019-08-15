%global packname  tidyselect
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Select from a Set of Strings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-purrr 

%description
A backend for the selecting functions of the 'tidyverse'. It makes it easy
to implement select-like functions in your own packages in a way that is
consistent with other 'tidyverse' interfaces for selection.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs