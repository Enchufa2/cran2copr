%global packname  arulesCBA
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Classification Based on Association Rules

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-glmnet >= 2.0.16
BuildRequires:    R-CRAN-arules >= 1.6.2
BuildRequires:    R-Matrix >= 1.2.0
BuildRequires:    R-CRAN-discretization >= 1.0.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-glmnet >= 2.0.16
Requires:         R-CRAN-arules >= 1.6.2
Requires:         R-Matrix >= 1.2.0
Requires:         R-CRAN-discretization >= 1.0.1
Requires:         R-methods 
Requires:         R-CRAN-testthat 

%description
Provides a function to build an association rule-based classifier for data
frames, and to classify incoming data frames using such a classifier.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
