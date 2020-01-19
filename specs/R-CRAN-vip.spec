%global packname  vip
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Variable Importance Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 0.9.0
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ModelMetrics 
BuildRequires:    R-CRAN-pdp 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 0.9.0
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ModelMetrics 
Requires:         R-CRAN-pdp 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
A general framework for constructing variable importance plots from
various types of machine learning models in R. Aside from some standard
model- specific variable importance measures, this package also provides
model- agnostic approaches that can be applied to any supervised learning
algorithm. These include an efficient permutation-based variable
importance measure as well as novel approaches based on partial dependence
plots (PDPs) and individual conditional expectation (ICE) curves which are
described in Greenwell et al. (2018) <arXiv:1805.04755>. An experimental
method for quantifying the relative strength of interaction effects is
also included (see the previous reference for details).

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX