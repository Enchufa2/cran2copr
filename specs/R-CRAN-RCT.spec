%global packname  RCT
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Assign Treatments, Power Calculations, Balances, ImpactEvaluation of Experiments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-lfe 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-lfe 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 

%description
Assists in the whole process of designing and evaluating Randomized
Control Trials. Robust treatment assignment by strata/blocks, that handles
misfits; Power calculations of the minimum detectable treatment effect
Balance tables of T-test of covariates; Balance Regression: (treatment ~
all x variables) with F-test of null model; Impact_evaluation: Impact
evaluation regressions. This function gives you the option to include
control_vars, fixed effect variables, cluster variables (for robust SE),
multiple endogenous variables and multiple heterogeneous variables (to
test treatment effect heterogeneity) summary_statistics: Function that
creates a summary statistics table with statistics rank observations in n
groups: Creates a factor variable with n groups. Each group has a min and
max label attach to each category. Athey, Susan, and Guido W. Imbens
(2017) <arXiv:1607.00698>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
