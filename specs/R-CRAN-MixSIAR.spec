%global packname  MixSIAR
%global packver   3.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.10
Release:          1%{?dist}
Summary:          Bayesian Mixing Models in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-MCMCpack >= 1.4.2
BuildRequires:    R-CRAN-bayesplot >= 1.4.0
BuildRequires:    R-CRAN-RColorBrewer >= 1.1
BuildRequires:    R-CRAN-ggmcmc >= 1.1
BuildRequires:    R-CRAN-reshape >= 0.8.7
BuildRequires:    R-CRAN-R2jags >= 0.5.7
BuildRequires:    R-lattice >= 0.20.35
BuildRequires:    R-CRAN-coda >= 0.19.1
Requires:         R-MASS >= 7.3
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-MCMCpack >= 1.4.2
Requires:         R-CRAN-bayesplot >= 1.4.0
Requires:         R-CRAN-RColorBrewer >= 1.1
Requires:         R-CRAN-ggmcmc >= 1.1
Requires:         R-CRAN-reshape >= 0.8.7
Requires:         R-CRAN-R2jags >= 0.5.7
Requires:         R-lattice >= 0.20.35
Requires:         R-CRAN-coda >= 0.19.1

%description
Creates and runs Bayesian mixing models to analyze biological tracer data
(i.e. stable isotopes, fatty acids), which estimate the proportions of
source (prey) contributions to a mixture (consumer). 'MixSIAR' is not one
model, but a framework that allows a user to create a mixing model based
on their data structure and research questions, via options for fixed/
random effects, source data types, priors, and error terms. 'MixSIAR'
incorporates several years of advances since 'MixSIR' and 'SIAR', and
includes both GUI (graphical user interface) and script versions.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example_scripts
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/mixsiar_manual_small.pdf
%{rlibdir}/%{packname}/INDEX