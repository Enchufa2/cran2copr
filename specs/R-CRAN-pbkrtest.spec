%global packname  pbkrtest
%global packver   0.4-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.7
Release:          1%{?dist}
Summary:          Parametric Bootstrap and Kenward Roger Based Methods for MixedModel Comparison

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-Matrix >= 1.2.3
BuildRequires:    R-CRAN-lme4 >= 1.1.10
BuildRequires:    R-parallel 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
Requires:         R-Matrix >= 1.2.3
Requires:         R-CRAN-lme4 >= 1.1.10
Requires:         R-parallel 
Requires:         R-MASS 
Requires:         R-methods 

%description
Test in mixed effects models. Attention is on mixed effects models as
implemented in the 'lme4' package. This package implements a parametric
bootstrap test and a Kenward Roger modification of F-tests for linear
mixed effects models and a parametric bootstrap test for generalized
linear mixed models.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX