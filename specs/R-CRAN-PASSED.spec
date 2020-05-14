%global packname  PASSED
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Calculate Power and Sample Size for Two Sample Mean Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-MESS 
Requires:         R-CRAN-betareg 
Requires:         R-stats 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-MESS 

%description
Power calculations are a critical component of any research study to
determine the minimum sample size necessary to detect differences between
multiple groups. Here we present an 'R' package, 'PASSED', that performs
power and sample size calculations for the test of two-sample means or
ratios with data following beta, gamma (Chang et al. (2011),
<doi:10.1007/s00180-010-0209-1>), normal, Poisson (Gu et al. (2008),
<doi:10.1002/bimj.200710403>), binomial, geometric, and negative binomial
(Zhu and Lakkis (2014), <doi:10.1002/sim.5947>) distributions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
