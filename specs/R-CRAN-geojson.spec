%global packname  geojson
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Classes for 'GeoJSON'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-protolite >= 1.8
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-jqr >= 1.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lazyeval 
Requires:         R-CRAN-protolite >= 1.8
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-jqr >= 1.1.0
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lazyeval 

%description
Classes for 'GeoJSON' to make working with 'GeoJSON' easier. Includes S3
classes for 'GeoJSON' classes with brief summary output, and a few methods
such as extracting and adding bounding boxes, properties, and coordinate
reference systems; working with newline delimited 'GeoJSON'; linting
through the 'geojsonlint' package; and serializing to/from 'Geobuf' binary
'GeoJSON' format.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
