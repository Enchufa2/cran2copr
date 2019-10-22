%global packname  LUCIDus
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Latent Unknown Clustering with Integrated Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-lbfgs 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nnet 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-glasso 
Requires:         R-Matrix 
Requires:         R-CRAN-lbfgs 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
An implementation for the 'LUCID' method to jointly estimate latent
unknown clusters/subgroups with integrated data. An EM algorithm is used
to obtain the latent cluster assignment and model parameter estimates.
Feature selection is achieved by applying the regularization method.

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
