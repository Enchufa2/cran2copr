%global packname  SimComp
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}
Summary:          Simultaneous Comparisons for Multiple Endpoints

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-mratios 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-mratios 
Requires:         R-graphics 
Requires:         R-stats 

%description
Simultaneous tests and confidence intervals are provided for one-way
experimental designs with one or many normally distributed, primary
response variables (endpoints). Differences (Hasler and Hothorn, 2011) or
ratios (Hasler and Hothorn, 2012) of means can be considered. Various
contrasts can be chosen, unbalanced sample sizes are allowed as well as
heterogeneous variances (Hasler and Hothorn, 2008) or covariance matrices
(Hasler, 2014).

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