%global packname  mvdalab
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          2%{?dist}%{?buildtag}
Summary:          Multivariate Data Analysis Laboratory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dummies 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-sn 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dummies 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-moments 
Requires:         R-parallel 
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-sn 

%description
An open-source implementation of latent variable methods and multivariate
modeling tools. The focus is on exploratory analyses using dimensionality
reduction methods including low dimensional embedding, classical
multivariate statistical tools, and tools for enhanced interpretation of
machine learning methods (i.e. intelligible models to provide important
information for end-users).  Target domains include extension to dedicated
applications e.g. for manufacturing process modeling, spectroscopic
analyses, and data mining.

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
