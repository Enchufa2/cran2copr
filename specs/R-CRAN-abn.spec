%global packname  abn
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}
Summary:          Modelling Multivariate Data with Additive Bayesian Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel >= 1.12
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-nnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-nnet 
Requires:         R-MASS 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-rjags 
Requires:         R-boot 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-brglm 

%description
Bayesian network analysis is a form of probabilistic graphical models
which derives from empirical data a directed acyclic graph, DAG,
describing the dependency structure between random variables. An additive
Bayesian network model consists of a form of a DAG where each node
comprises a generalized linear model, GLM. Additive Bayesian network
models are equivalent to Bayesian multivariate regression using graphical
modelling, they generalises the usual multivariable regression, GLM, to
multiple dependent variables. 'abn' provides routines to help determine
optimal Bayesian network models for a given data set, where these models
are used to identify statistical dependencies in messy, complex data. The
additive formulation of these models is equivalent to multivariate
generalised linear modelling (including mixed models with iid random
effects). The usual term to describe this model selection process is
structure discovery. The core functionality is concerned with model
selection - determining the most robust empirical model of data from
interdependent variables. Laplace approximations are used to estimate
goodness of fit metrics and model parameters, and wrappers are also
included to the INLA package which can be obtained from
<http://www.r-inla.org>. The computing library JAGS
<http://mcmc-jags.sourceforge.net> is used to simulate 'abn'-like data. A
comprehensive set of documented case studies, numerical accuracy/quality
assurance exercises, and additional documentation are available from the
'abn' website <http://r-bayesian-networks.org>.

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
