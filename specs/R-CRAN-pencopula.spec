%global packname  pencopula
%global packver   0.3.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5.1
Release:          1%{?dist}
Summary:          Flexible Copula Density Estimation with Penalized HierarchicalB-Splines

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-lattice 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-latticeExtra 

%description
Flexible copula density estimation with penalized hierarchical B-Splines.

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
%{rlibdir}/%{packname}/INDEX