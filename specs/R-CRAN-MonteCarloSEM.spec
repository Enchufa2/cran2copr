%global packname  MonteCarloSEM
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Monte Carlo Data Simulation Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lavaan 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-lavaan 

%description
Monte Carlo simulation allows to test different conditions given to the
correct structural equation models. This package runs Monte Carlo
simulations under different conditions (such as sample size or normality
of data). Within the package data sets can be simulated and run based on
the given model. First, continuous and normal data sets are generated
based on the given model. Later Fleishman's power method (1978)
<DOI:10.1007/BF02293811> is used to add non-normality if exists. When data
generation is completed (or when generated data sets are given) model test
can also be run.

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
