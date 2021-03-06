%global packname  decomposedPSF
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Time Series Prediction with PSF and Decomposition Methods (EMDand EEMD)

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-PSF 
BuildRequires:    R-CRAN-Rlibeemd 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-PSF 
Requires:         R-CRAN-Rlibeemd 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tseries 

%description
Predict future values with hybrid combinations of Pattern Sequence based
Forecasting (PSF), Autoregressive Integrated Moving Average (ARIMA),
Empirical Mode Decomposition (EMD) and Ensemble Empirical Mode
Decomposition (EEMD) methods based hybrid methods.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
