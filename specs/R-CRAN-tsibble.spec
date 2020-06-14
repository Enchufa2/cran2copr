%global packname  tsibble
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          2%{?dist}
Summary:          Tidy Temporal Data Frames and Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-anytime >= 0.3.1
BuildRequires:    R-CRAN-ellipsis >= 0.3.0
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-purrr >= 0.2.3
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-anytime >= 0.3.1
Requires:         R-CRAN-ellipsis >= 0.3.0
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-purrr >= 0.2.3
Requires:         R-CRAN-lifecycle 

%description
Provides a 'tbl_ts' class (the 'tsibble') for temporal data in an data-
and model-oriented format. The 'tsibble' provides tools to easily
manipulate and analyse temporal data, such as filling in time gaps and
aggregating over calendar periods.

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
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
