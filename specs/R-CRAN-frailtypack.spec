%global packname  frailtypack
%global packver   3.0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3.2
Release:          1%{?dist}
Summary:          General Frailty Models: Shared, Joint and Nested Frailty Modelswith Prediction; Evaluation of Failure-Time Surrogate Endpoints

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-survival 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-survC1 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-nlme 
Requires:         R-survival 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-CRAN-survC1 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-statmod 
Requires:         R-nlme 

%description
The following several classes of frailty models using a penalized
likelihood estimation on the hazard function but also a parametric
estimation can be fit using this R package: 1) A shared frailty model
(with gamma or log-normal frailty distribution) and Cox proportional
hazard model. Clustered and recurrent survival times can be studied. 2)
Additive frailty models for proportional hazard models with two correlated
random effects (intercept random effect with random slope). 3) Nested
frailty models for hierarchically clustered data (with 2 levels of
clustering) by including two iid gamma random effects. 4) Joint frailty
models in the context of the joint modelling for recurrent events with
terminal event for clustered data or not. A joint frailty model for two
semi-competing risks and clustered data is also proposed. 5) Joint general
frailty models in the context of the joint modelling for recurrent events
with terminal event data with two independent frailty terms. 6) Joint
Nested frailty models in the context of the joint modelling for recurrent
events with terminal event, for hierarchically clustered data (with two
levels of clustering) by including two iid gamma random effects. 7)
Multivariate joint frailty models for two types of recurrent events and a
terminal event. 8) Joint models for longitudinal data and a terminal
event. 9) Trivariate joint models for longitudinal data, recurrent events
and a terminal event. 10) Joint frailty models for the validation of
surrogate endpoints in multiple randomized clinical trials with
failure-time endpoints Prediction values are available (for a terminal
event or for a new recurrent event). Left-truncated (not for Joint model),
right-censored data, interval-censored data (only for Cox proportional
hazard and shared frailty model) and strata are allowed. In each model,
the random effects have the gamma or normal distribution. Now, you can
also consider time-varying covariates effects in Cox, shared and joint
frailty models (1-5). The package includes concordance measures for Cox
proportional hazards models and for shared frailty models.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
