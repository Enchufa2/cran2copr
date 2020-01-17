%global packname  mvSLOUCH
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Multivariate Stochastic Linear Ornstein-Uhlenbeck Models forPhylogenetic Comparative Hypotheses

License:          GPL (>= 2) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.3
BuildRequires:    R-CRAN-PCMBase >= 1.2.10
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-ouch 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-TreeSim 
Requires:         R-CRAN-ape >= 5.3
Requires:         R-CRAN-PCMBase >= 1.2.10
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-ouch 
Requires:         R-stats 
Requires:         R-CRAN-TreeSim 

%description
Fits multivariate Ornstein-Uhlenbeck types of models to continues trait
data from species related by a common evolutionary history. See K.
Bartoszek, J, Pienaar, P. Mostad, S. Andersson, T. F.Hansen (2012)
<doi:10.1016/j.jtbi.2012.08.005>. The suggested PCMBaseCpp package (which
significantly speeds up the likelihood calculations) can be obtained from
<https://github.com/venelin/PCMBaseCpp/>.

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/GPL-2
%doc %{rlibdir}/%{packname}/GPL-3
%{rlibdir}/%{packname}/INDEX
