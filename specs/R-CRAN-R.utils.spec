%global packname  R.utils
%global packver   2.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.0
Release:          1%{?dist}
Summary:          Various Programming Utilities

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.methodsS3 >= 1.7.1
BuildRequires:    R-CRAN-R.oo >= 1.22.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-R.methodsS3 >= 1.7.1
Requires:         R-CRAN-R.oo >= 1.22.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-tools 

%description
Utility functions useful when programming and developing R packages.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data-ex
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX