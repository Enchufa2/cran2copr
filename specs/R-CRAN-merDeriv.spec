%global packname  merDeriv
%global packver   0.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Case-Wise and Cluster-Wise Derivatives for Mixed Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.1.10
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nonnest2 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-lme4 >= 1.1.10
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-nonnest2 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lavaan 
Requires:         R-utils 
Requires:         R-Matrix 

%description
Compute case-wise and cluster-wise derivative for mixed effects models
with respect to fixed effects parameter, random effect (co)variances, and
residual variance.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX