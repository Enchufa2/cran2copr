%global packname  vctrs
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Vector Helpers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-ellipsis >= 0.2.0
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-zeallot 
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-ellipsis >= 0.2.0
Requires:         R-CRAN-backports 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-zeallot 

%description
Defines new notions of prototype and size that are used to provide tools
for consistent and well-founded type-coercion and size-recycling, and are
in turn connected to ideas of type- and size-stability useful for
analyzing function interfaces.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs