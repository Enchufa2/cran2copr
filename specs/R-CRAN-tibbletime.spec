%global packname  tibbletime
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Time Aware Tibbles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-zoo >= 1.8.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-tibble >= 1.4.1
BuildRequires:    R-CRAN-glue >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-hms >= 0.4
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-rlang >= 0.1.6
Requires:         R-CRAN-zoo >= 1.8.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-tibble >= 1.4.1
Requires:         R-CRAN-glue >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-hms >= 0.4
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-rlang >= 0.1.6

%description
Built on top of the 'tibble' package, 'tibbletime' is an extension that
allows for the creation of time aware tibbles. Some immediate advantages
of this include: the ability to perform time-based subsetting on tibbles,
quickly summarising and aggregating results by time periods, and creating
columns that can be used as 'dplyr' time-based groups.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs