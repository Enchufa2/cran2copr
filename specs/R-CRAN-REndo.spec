%global packname  REndo
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Fitting Linear Models with Endogenous Regressors using LatentInstrumental Variables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-methods >= 3.4
BuildRequires:    R-stats >= 3.4
BuildRequires:    R-utils >= 3.4
BuildRequires:    R-CRAN-optimx >= 2013.8.7
BuildRequires:    R-CRAN-corpcor >= 1.6.9
BuildRequires:    R-CRAN-AER >= 1.2.5
BuildRequires:    R-Matrix >= 1.2.14
BuildRequires:    R-CRAN-Formula >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.11.8
BuildRequires:    R-CRAN-lme4 >= 1.1.18.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.8
Requires:         R-methods >= 3.4
Requires:         R-stats >= 3.4
Requires:         R-utils >= 3.4
Requires:         R-CRAN-optimx >= 2013.8.7
Requires:         R-CRAN-corpcor >= 1.6.9
Requires:         R-CRAN-AER >= 1.2.5
Requires:         R-Matrix >= 1.2.14
Requires:         R-CRAN-Formula >= 1.2
Requires:         R-CRAN-data.table >= 1.11.8
Requires:         R-CRAN-lme4 >= 1.1.18.1
Requires:         R-CRAN-mvtnorm >= 1.0.8

%description
Fits linear models with endogenous regressor using latent instrumental
variable approaches. The methods included in the package are Lewbel's
(1997) <doi:10.2307/2171884> higher moments approach as well as Lewbel's
(2012) <doi:10.1080/07350015.2012.643126> heteroscedasticity approach,
Park and Gupta's (2012) <doi:10.1287/mksc.1120.0718> joint estimation
method that uses Gaussian copula and Kim and Frees's (2007)
<doi:10.1007/s11336-007-9008-1> multilevel generalized method of moment
approach that deals with endogeneity in a multilevel setting. These are
statistical techniques to address the endogeneity problem where no
external instrumental variables are needed. Note that with version 2.0.0
sweeping changes were introduced which greatly improve functionality and
usability but break backwards compatibility.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX