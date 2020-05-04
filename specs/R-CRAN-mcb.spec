%global packname  mcb
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Model Confidence Bounds

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-parcor 
BuildRequires:    R-CRAN-smoothmest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-lars 
Requires:         R-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-parcor 
Requires:         R-CRAN-smoothmest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
When choosing proper variable selection methods, it is important to
consider the uncertainty of a certain method. The Model Confidence Bound
for variable selection identifies two nested models (upper and lower
confidence bound models) containing the true model at a given confidence
level. A good variable selection method is the one of which the Model
Confidence Bound under a certain confidence level has the shortest width.
When visualizing the variability of model selection and comparing
different model selection procedures, Model Uncertainty Curve is a good
graphical tool. A good variable selection method is the one of whose Model
Uncertainty Curve will tend to arch towards the upper left corner. This
function aims to obtain the Model Confidence Bound and draw the Model
Uncertainty Curve of certain single model selection method under a
coverage rate equal or little higher than user-given confidential level.
About what Model Confidence Bound is and how it work please see Li,Y.,
Luo,Y., Ferrari,D., Hu,X. and Qin,Y. (2019) Model Confidence Bounds for
Variable Selection. Biometrics, 75:392-403. <DOI:10.1111/biom.13024>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX