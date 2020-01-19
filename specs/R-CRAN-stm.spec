%global packname  stm
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          1%{?dist}
Summary:          Estimation of the Structural Topic Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lda 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glmnet 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-lda 
Requires:         R-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-parallel 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-slam 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
The Structural Topic Model (STM) allows researchers to estimate topic
models with document-level covariates. The package also includes tools for
model selection, visualization, and estimation of topic-covariate
regressions. Methods developed in Roberts et al (2014)
<doi:10.1111/ajps.12103> and Roberts et al (2016)
<doi:10.1080/01621459.2016.1141684>. Vignette is Roberts et al (2019)
<doi:10.18637/jss.v091.i02>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs