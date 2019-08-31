%global packname  heemod
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}
Summary:          Markov Models for Health Economic Evaluations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-plyr >= 1.8.0
BuildRequires:    R-CRAN-tibble >= 1.3.0
BuildRequires:    R-CRAN-memoise >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.7.2
BuildRequires:    R-CRAN-mvnfast >= 0.2.2
BuildRequires:    R-CRAN-lazyeval >= 0.2.0
BuildRequires:    R-CRAN-pryr >= 0.1.2
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-plyr >= 1.8.0
Requires:         R-CRAN-tibble >= 1.3.0
Requires:         R-CRAN-memoise >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.7.2
Requires:         R-CRAN-mvnfast >= 0.2.2
Requires:         R-CRAN-lazyeval >= 0.2.0
Requires:         R-CRAN-pryr >= 0.1.2

%description
An implementation of the modelling and reporting features described in
reference textbook and guidelines (Briggs, Andrew, et al. Decision
Modelling for Health Economic Evaluation. Oxford Univ. Press, 2011;
Siebert, U. et al. State-Transition Modeling. Medical Decision Making 32,
690-700 (2012).): deterministic and probabilistic sensitivity analysis,
heterogeneity analysis, time dependency on state-time and model-time
(semi-Markov and non-homogeneous Markov models), etc.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/media
%doc %{rlibdir}/%{packname}/tabular
%{rlibdir}/%{packname}/INDEX