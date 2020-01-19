%global packname  timedelay
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Time Delay Estimation for Stochastic Time Series ofGravitationally Lensed Quasars

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
We provide a toolbox to estimate the time delay between the brightness
time series of gravitationally lensed quasar images via Bayesian and
profile likelihood approaches. The model is based on a state-space
representation for irregularly observed time series data generated from a
latent continuous-time Ornstein-Uhlenbeck process. Our Bayesian method
adopts scientifically motivated hyper-prior distributions and a
Metropolis-Hastings within Gibbs sampler, producing posterior samples of
the model parameters that include the time delay. A profile likelihood of
the time delay is a simple approximation to the marginal posterior
distribution of the time delay. Both Bayesian and profile likelihood
approaches complement each other, producing almost identical results; the
Bayesian way is more principled but the profile likelihood is easier to
implement.

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
%{rlibdir}/%{packname}/INDEX