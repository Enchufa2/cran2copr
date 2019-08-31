%global packname  chngpt
%global packver   2019.3-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.3.12
Release:          1%{?dist}
Summary:          Estimation and Hypothesis Testing for Threshold Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-survival 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-kyotil 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-survival 
Requires:         R-splines 
Requires:         R-CRAN-kyotil 
Requires:         R-boot 
Requires:         R-MASS 

%description
Threshold regression models are also called two-phase regression,
broken-stick regression, split-point regression, structural change models,
and regression kink models. Methods for both continuous and discontinuous
threshold models are included, but the support for the former is much
greater. This package is described in Fong, Huang, Gilbert and Permar
(2017) chngpt: threshold regression model estimation and inference, BMC
Bioinformatics, in press, <DOI:10.1186/s12859-017-1863-x>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs