%global packname  rstatix
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Pipe-Friendly Framework for Basic Statistical Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.1
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.1
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-car 

%description
Provides a simple and intuitive pipe-friendly framework, coherent with the
'tidyverse' design philosophy, for performing basic statistical tests,
including t-test, Wilcoxon test, ANOVA, Kruskal-Wallis and correlation
analyses. The output of each test is automatically transformed into a tidy
data frame to facilitate visualization. Additional functions are available
for reshaping, reordering, manipulating and visualizing correlation
matrix. Functions are also included to facilitate the analysis of
factorial experiments, including purely 'within-Ss' designs (repeated
measures), purely 'between-Ss' designs, and mixed 'within-and-between-Ss'
designs. It's also possible to compute several effect size metrics,
including "eta squared" for ANOVA, "Cohen's d" for t-test and 'Cramer V'
for the association between categorical variables. The package contains
helper functions for identifying univariate and multivariate outliers,
assessing normality and homogeneity of variances.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
