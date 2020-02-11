%global packname  summarytools
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}
Summary:          Tools to Quickly and Neatly Summarize Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-rapportools 
BuildRequires:    R-stats 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-rapportools 
Requires:         R-stats 
Requires:         R-tcltk 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Data frame summaries, cross-tabulations, weight-enabled frequency tables
and common descriptive (univariate) statistics in concise tables available
in a variety of formats (plain ASCII, Markdown and HTML). A good
point-of-entry for exploring data, both for experienced and new R users.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/includes
%{rlibdir}/%{packname}/INDEX
