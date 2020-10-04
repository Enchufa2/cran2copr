%global packname  AdhereR
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Adherence to Medications

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.0
BuildRequires:    R-CRAN-data.table >= 1.9
BuildRequires:    R-CRAN-lubridate >= 1.5
BuildRequires:    R-CRAN-webp >= 1.0
BuildRequires:    R-CRAN-jpeg >= 0.1
BuildRequires:    R-CRAN-png >= 0.1
Requires:         R-parallel >= 3.0
Requires:         R-CRAN-data.table >= 1.9
Requires:         R-CRAN-lubridate >= 1.5
Requires:         R-CRAN-webp >= 1.0
Requires:         R-CRAN-jpeg >= 0.1
Requires:         R-CRAN-png >= 0.1

%description
Computation of adherence to medications from Electronic Health care Data
and visualization of individual medication histories and adherence
patterns. The package implements a set of S3 classes and functions
consistent with current adherence guidelines and definitions. It allows
the computation of different measures of adherence (as defined in the
literature, but also several original ones), their publication-quality
plotting, the estimation of event duration and time to initiation, the
interactive exploration of patient medication history and the real-time
estimation of adherence given various parameter settings. It scales from
very small datasets stored in flat CSV files to very large databases and
from single-thread processing on mid-range consumer laptops to parallel
processing on large heterogeneous computing clusters. It exposes a
standardized interface allowing it to be used from other programming
languages and platforms, such as Python.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html-templates
%doc %{rlibdir}/%{packname}/specialVignettes
%doc %{rlibdir}/%{packname}/wrappers
%{rlibdir}/%{packname}/INDEX
