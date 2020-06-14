%global packname  doBy
%global packver   4.6.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.6
Release:          2%{?dist}
Summary:          Groupwise Statistics, LSmeans, Linear Contrasts, Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbkrtest >= 0.4.8.1
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-broom 
Requires:         R-CRAN-pbkrtest >= 0.4.8.1
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-broom 

%description
Contains: 1) Facilities for working with grouped data: 'do' something to
data stratified 'by' some variables. 2) LSmeans (least-squares means),
general linear contrasts. 3) Miscellaneous other utilities.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
