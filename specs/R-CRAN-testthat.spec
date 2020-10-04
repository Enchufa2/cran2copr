%global packname  testthat
%global packver   2.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Unit Testing for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-withr >= 2.0.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-rlang >= 0.4.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-praise 
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-withr >= 2.0.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-rlang >= 0.4.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-praise 

%description
Software testing is important, but, in part because it is frustrating and
boring, many of us avoid it. 'testthat' is a testing framework for R that
is easy to learn and use, and integrates with your existing 'workflow'.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/resources
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
