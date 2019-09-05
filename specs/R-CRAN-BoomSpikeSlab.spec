%global packname  BoomSpikeSlab
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          MCMC for Spike and Slab Regression

License:          LGPL-2.1 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Boom >= 0.9.2
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-Boom >= 0.9.2
Requires:         R-CRAN-igraph 

%description
Spike and slab regression with a variety of residual error distributions
corresponding to Gaussian, Student T, probit, logit, SVM, and a few
others.  Spike and slab regression is Bayesian regression with prior
distributions containing a point mass at zero.  The posterior updates the
amount of mass on this point, leading to a posterior distribution that is
actually sparse, in the sense that if you sample from it many coefficients
are actually zeros.  Sampling from this posterior distribution is an
elegant way to handle Bayesian variable selection and model averaging.
See <DOI:10.1504/IJMMNO.2014.059942> for an explanation of the Gaussian
case.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
