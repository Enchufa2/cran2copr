%global packname  MCDA
%global packver   0.0.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.20
Release:          2%{?dist}
Summary:          Support for the Multicriteria Decision Aiding Process

License:          EUPL (== 1.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-glpkAPI 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-combinat 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-glpkAPI 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-combinat 

%description
Support for the analyst in a Multicriteria Decision Aiding (MCDA) process
with algorithms, preference elicitation and data visualisation functions.
Sébastien Bigaret, Richard Hodgett, Patrick Meyer, Tatyana Mironova,
Alexandru Olteanu (2017) Supporting the multi-criteria decision aiding
process : R and the MCDA package, Euro Journal On Decision Processes,
Volume 5, Issue 1 - 4, pages 169 - 194 <doi:10.1007/s40070-017-0064-1>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/datasets
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
