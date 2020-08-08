%global debug_package %{nil}
%global packname  BANOVA
%global packver   1.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          1%{?dist}
Summary:          Hierarchical Bayesian ANOVA Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-rjags >= 3.13
BuildRequires:    R-CRAN-rstan >= 2.15.1
BuildRequires:    R-CRAN-runjags >= 1.2.1.0
BuildRequires:    R-CRAN-coda >= 0.16.1
BuildRequires:    R-methods 
Requires:         R-CRAN-rjags >= 3.13
Requires:         R-CRAN-rstan >= 2.15.1
Requires:         R-CRAN-runjags >= 1.2.1.0
Requires:         R-CRAN-coda >= 0.16.1
Requires:         R-methods 

%description
It covers several Bayesian Analysis of Variance (BANOVA) models used in
analysis of experimental designs in which both within- and between-
subjects factors are manipulated. They can be applied to data that are
common in the behavioral and social sciences. The package includes:
Hierarchical Bayes ANOVA models with normal response, t response, Binomial
(Bernoulli) response, Poisson response, ordered multinomial response and
multinomial response variables. All models accommodate unobserved
heterogeneity by including a normal distribution of the parameters across
individuals. Outputs of the package include tables of sums of squares,
effect sizes and p-values, and tables of predictions, which are easily
interpretable for behavioral and social researchers. The floodlight
analysis and mediation analysis based on these models are also provided.
BANOVA uses 'Stan' and 'JAGS' as the computational platform.

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
