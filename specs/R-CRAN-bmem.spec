%global packname  bmem
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Mediation Analysis with Missing Data Using Bootstrap

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.7
Requires:         R-core >= 1.7
BuildArch:        noarch
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-sem 
Requires:         R-CRAN-Amelia 
Requires:         R-MASS 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-sem 

%description
Four methods for mediation analysis with missing data: Listwise deletion,
Pairwise deletion, Multiple imputation, and Two Stage Maximum Likelihood
algorithm. For MI and TS-ML, auxiliary variables can be included.
Bootstrap confidence intervals for mediation effects are obtained. The
robust method is also implemented for TS-ML. Since version 1.4, bmem adds
the capability to conduct power analysis for mediation models.

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

%files
%{rlibdir}/%{packname}
