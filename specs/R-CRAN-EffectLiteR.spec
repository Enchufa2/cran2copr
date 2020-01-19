%global packname  EffectLiteR
%global packver   0.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Average and Conditional Effects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.5.20
BuildRequires:    R-CRAN-shiny >= 0.11
BuildRequires:    R-methods 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-lavaan.survey 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-lavaan >= 0.5.20
Requires:         R-CRAN-shiny >= 0.11
Requires:         R-methods 
Requires:         R-foreign 
Requires:         R-CRAN-ggplot2 
Requires:         R-nnet 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-lavaan.survey 
Requires:         R-CRAN-car 

%description
Use structural equation modeling to estimate average and conditional
effects of a treatment variable on an outcome variable, taking into
account multiple continuous and categorical covariates.

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
%doc %{rlibdir}/%{packname}/elrshiny
%{rlibdir}/%{packname}/INDEX