%global packname  fdm2id
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Data Mining and R Programming for Beginners

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-class 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ibr 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-kohonen 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-meanShiftR 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-NMF 
BuildRequires:    R-CRAN-questionr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-text2vec 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-mclust 
Requires:         R-nnet 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-car 
Requires:         R-CRAN-caret 
Requires:         R-class 
Requires:         R-cluster 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-fpc 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ibr 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-kohonen 
Requires:         R-CRAN-leaps 
Requires:         R-MASS 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-meanShiftR 
Requires:         R-methods 
Requires:         R-CRAN-NMF 
Requires:         R-CRAN-questionr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ROCR 
Requires:         R-rpart 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-SnowballC 
Requires:         R-stats 
Requires:         R-CRAN-text2vec 
Requires:         R-CRAN-stopwords 
Requires:         R-utils 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-xgboost 

%description
Contains functions to simplify the use of data mining methods
(classification, regression, clustering, etc.), for students and beginners
in R programming. Various R packages are used and wrappers are built
around the main functions, to standardize the use of data mining methods
(input/output): it brings a certain loss of flexibility, but also a gain
of simplicity. The package name came from the French "Fouille de Données
en Master 2 Informatique Décisionnelle".

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
