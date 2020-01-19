%global packname  TKF
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}
Summary:          Pairwise Distance Estimation with TKF91 and TKF92 Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-ape >= 3.2
BuildRequires:    R-CRAN-phangorn >= 1.99.12
BuildRequires:    R-CRAN-phytools >= 0.4.45
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-ape >= 3.2
Requires:         R-CRAN-phangorn >= 1.99.12
Requires:         R-CRAN-phytools >= 0.4.45
Requires:         R-methods 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-numDeriv 

%description
Pairwise evolutionary distance estimation between protein sequences with
the TKF91 and TKF92 model, which consider all the possible paths of
transforming from one sequence to another.

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
%doc %{rlibdir}/%{packname}/buildMatrix
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/makePackage
%doc %{rlibdir}/%{packname}/oldScripts
%doc %{rlibdir}/%{packname}/TestData
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs