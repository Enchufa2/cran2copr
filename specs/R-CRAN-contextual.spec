%global packname  contextual
%global packver   0.9.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8.3
Release:          2%{?dist}
Summary:          Simulation and Analysis of Contextual Multi-Armed BanditPolicies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.3.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R.devices 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-rjson 
Requires:         R-CRAN-R6 >= 2.3.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R.devices 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-itertools 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-rjson 

%description
Facilitates the simulation and evaluation of context-free and contextual
multi-Armed Bandit policies or algorithms to ease the implementation,
evaluation, and dissemination of both existing and new bandit algorithms
and policies.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
