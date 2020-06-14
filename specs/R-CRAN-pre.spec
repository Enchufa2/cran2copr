%global packname  pre
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Prediction Rule Ensembles

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit >= 1.2.0
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-survival 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-MatrixModels 
Requires:         R-CRAN-partykit >= 1.2.0
Requires:         R-CRAN-earth 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-rpart 
Requires:         R-CRAN-stringr 
Requires:         R-survival 
Requires:         R-Matrix 
Requires:         R-CRAN-MatrixModels 

%description
Derives prediction rule ensembles (PREs). Largely follows the procedure
for deriving PREs as described in Friedman & Popescu (2008;
<DOI:10.1214/07-AOAS148>), with adjustments and improvements. The main
function pre() derives prediction rule ensembles consisting of rules
and/or linear terms for continuous, binary, count, multinomial, and
multivariate continuous responses. Function gpe() derives generalized
prediction ensembles, consisting of rules, hinge and linear functions of
the predictor variables.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bib_style.csl
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/README-figures
%{rlibdir}/%{packname}/INDEX
