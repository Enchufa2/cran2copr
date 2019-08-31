%global packname  assignPOP
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Population Assignment using Genetic, Non-Genetic or IntegratedData in a Machine Learning Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.2
Requires:         R-core >= 2.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tree 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tree 

%description
Use Monte-Carlo and K-fold cross-validation coupled with machine- learning
classification algorithms to perform population assignment, with
functionalities of evaluating discriminatory power of independent training
samples, identifying informative loci, reducing data dimensionality for
genomic data, integrating genetic and non-genetic data, and visualizing
results.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX