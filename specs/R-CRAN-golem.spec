%global packname  golem
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Framework for Robust Shiny Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-attempt >= 0.3.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-dockerfiler 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-attempt >= 0.3.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-config 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-dockerfiler 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-here 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-roxygen2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-usethis 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
An opinionated framework for building a production-ready 'Shiny'
application. This package contains a series of tools for building a robust
'Shiny' application from start to finish.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/manualtests
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/shinyexample
%doc %{rlibdir}/%{packname}/utils
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
