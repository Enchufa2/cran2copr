%global packname  DiPs
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Directional Penalties for Optimal Matching in ObservationalStudies

License:          MIT+file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rcbalance 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-liqueueR 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-methods 
Requires:         R-CRAN-rcbalance 
Requires:         R-stats 
Requires:         R-CRAN-liqueueR 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvnfast 
Requires:         R-methods 

%description
Improves the balance of optimal matching with near-fine balance by giving
penalties on the unbalanced covariates with the unbalanced directions.
Many directional penalties can also be viewed as Lagrange multipliers,
pushing a matched sample in the direction of satisfying a linear
constraint that would not be satisfied without penalization. Rosenbaum,
P.R. (1989). <DOI:10.1080/01621459.1989.10478868>. Yang, D., Small, D. S.,
Silber, J. H., and Rosenbaum, P. R. (2012).
<DOI:10.1111/j.1541-0420.2011.01691.x>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX