%global packname  BLRPM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Rainfall Generator Bartlett-Lewis Rectangular PulseModel

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-R6 

%description
Due to a limited availability of observed high-resolution precipitation
records with adequate length, simulations with stochastic precipitation
models are used to generate series for subsequent studies [e.g. Khaliq and
Cunmae, 1996, <doi:10.1016/0022-1694(95)02894-3>, Vandenberghe et al.,
2011, <doi:10.1029/2009WR008388>]. This package contains an R
implementation of the original Bartlett-Lewis rectangular pulse model
(BLRPM), developed by Rodriguez-Iturbe et al. (1987)
<doi:10.1098/rspa.1987.0039>. It contains a function for simulating a
precipitation time series based on storms and cells generated by the model
with given or estimated model parameters. Additionally BLRPM parameters
can be estimated from a given or simulated precipitation time series. The
model simulations can be plotted in a three-layer plot including an
overview of generated storms and cells by the model (which can also be
plotted individually), a continuous step-function and a discrete
precipitation time series at a chosen aggregation level.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
