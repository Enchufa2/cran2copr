%global packname  binomialRF
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Binomial Random Forest Feature Selection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-correlbinom 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-methods 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-correlbinom 
Requires:         R-parallel 
Requires:         R-CRAN-Rmpfr 
Requires:         R-methods 

%description
The 'binomialRF' is a new feature selection technique for decision trees
that aims at providing an alternative approach to identify significant
feature subsets using binomial distributional assumptions (Rachid Zaim,
S., et al. (2019)) <doi:10.1101/681973>. Treating each splitting variable
selection as a set of exchangeable correlated Bernoulli trials,
'binomialRF' then tests whether a feature is selected more often than by
random chance.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX