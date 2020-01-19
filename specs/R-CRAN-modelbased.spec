%global packname  modelbased
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Estimation of Model-Based Predictions, Contrasts and Means

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 0.7.1
BuildRequires:    R-CRAN-bayestestR >= 0.4.0
BuildRequires:    R-CRAN-parameters >= 0.3.0
BuildRequires:    R-CRAN-effectsize >= 0.0.1
BuildRequires:    R-CRAN-emmeans 
Requires:         R-CRAN-insight >= 0.7.1
Requires:         R-CRAN-bayestestR >= 0.4.0
Requires:         R-CRAN-parameters >= 0.3.0
Requires:         R-CRAN-effectsize >= 0.0.1
Requires:         R-CRAN-emmeans 

%description
Implements a general interface for model-based estimations for a wide
variety of models (see support list of insight; Lüdecke, Waggoner &
Makowski (2019) <doi:10.21105/joss.01412>), used in the computation of
marginal means, contrast analysis and predictions.

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
%{rlibdir}/%{packname}/INDEX