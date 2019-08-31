%global packname  buildmer
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Stepwise Elimination and Term Reordering for Mixed-EffectsRegression

License:          FreeBSD
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-mgcv 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-utils 

%description
Finds the largest possible regression model that will still converge for
various types of regression analyses (including mixed models and
generalized additive models) and then optionally performs stepwise
elimination similar to the forward and backward effect selection methods
in SAS, based on the change in log-likelihood, Akaike's Information
Criterion, or the Bayesian Information Criterion.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX