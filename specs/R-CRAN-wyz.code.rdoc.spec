%global packname  wyz.code.rdoc
%global packver   1.1.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.16
Release:          3%{?dist}%{?buildtag}
Summary:          Wizardry Code Offensive Programming R Documentation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-CRAN-wyz.code.offensiveProgramming >= 1.1.17
BuildRequires:    R-CRAN-digest >= 0.6.23
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-CRAN-wyz.code.offensiveProgramming >= 1.1.17
Requires:         R-CRAN-digest >= 0.6.23
Requires:         R-methods 
Requires:         R-CRAN-tidyr 

%description
Allows to generate on-demand or by batch, any R documentation file,
whatever is kind, data, function, class or package. It populates
documentation sections, either automatically or by considering your input.
Input code could be standard R code or offensive programming code.
Documentation content completeness depends on the type of code you use.
With offensive programming code, expect generated documentation to be
fully completed, from a format and content point of view. With some
standard R code, you will have to activate post processing to fill-in any
section that requires complements. Produced manual page validity is
automatically tested against R documentation compliance rules.
Documentation language proficiency, wording style, and phrasal adjustments
remains your job.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/man-generated
%doc %{rlibdir}/%{packname}/man-regenerated
%doc %{rlibdir}/%{packname}/man-samples
%doc %{rlibdir}/%{packname}/unit-testing
%{rlibdir}/%{packname}/INDEX
