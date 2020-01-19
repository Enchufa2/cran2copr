%global packname  statsExpressions
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Expressions with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ez >= 4.4.0
BuildRequires:    R-CRAN-rcompanion >= 2.3.21
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-psych >= 1.8.12
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-boot >= 1.3.22
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-WRS2 >= 1.0.0
BuildRequires:    R-CRAN-BayesFactor >= 0.9.12.4.2
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.2
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-groupedstats >= 0.1.0
BuildRequires:    R-CRAN-broomExtra >= 0.0.6
BuildRequires:    R-stats 
Requires:         R-CRAN-ez >= 4.4.0
Requires:         R-CRAN-rcompanion >= 2.3.21
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-psych >= 1.8.12
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-boot >= 1.3.22
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-WRS2 >= 1.0.0
Requires:         R-CRAN-BayesFactor >= 0.9.12.4.2
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.2
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-groupedstats >= 0.1.0
Requires:         R-CRAN-broomExtra >= 0.0.6
Requires:         R-stats 

%description
Statistical processing backend for 'ggstatsplot', this package creates
expressions with details from statistical tests. Currently, it supports
only the most common types of statistical tests: parametric,
nonparametric, robust, and bayesian versions of t-test/anova, correlation
analyses, contingency table analysis.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX