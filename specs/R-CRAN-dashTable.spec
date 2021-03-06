%global packname  dashTable
%global packver   4.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7.0
Release:          3%{?dist}%{?buildtag}
Summary:          Core Interactive Table Component for 'dash'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch

%description
An interactive table component designed for editing and exploring large
datasets, 'dashDataTable' is rendered with standard, semantic HTML
<table/> markup, which makes it accessible, responsive, and easy to style.
This component was written from scratch in 'React.js' specifically for the
'dash' community. Its API was designed to be ergonomic and its behaviour
is completely customizable through its properties.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/deps
%{rlibdir}/%{packname}/INDEX
