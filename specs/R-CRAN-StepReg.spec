%global packname  StepReg
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}
Summary:          Stepwise Regression Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.13

%description
Stepwise regression analysis for variable selection can be used to get the
best candidate final regression model with the forward selection, backward
elimination and bidirectional elimination approaches. Best subset
selection fit a separate least squares regression for each possible
combination of all predictors. Both the above two procedures in this
package can use weighted data to get best regression model in univariate
regression and multivariate regression analysis(Alsubaihi, A. A., (2002)
<doi:10.18637/jss.v007.i12>). Besides, continuous variables nested within
class effect is also considered in both two procedures. A widely used
selection criteria are available which includes Akaike information
criterion(Darlington, R. B. (1968) <doi:10.1037/h0025471>, Judge, G. G.
(1985) <doi:10.2307/1391738>), corrected Akaike information
criterion(Hurvich, C. M., and Tsai, C. (1989)
<doi:10.1093/biomet/76.2.297>), Bayesian information criterion(Sawa, T.
(1978) <doi:10.2307/1913828>, Judge, G. G. (1985) <doi:10.2307/1391738>),
Mallows Cp statistic(Mallows, C. L. (1973)
<doi:10.1080/00401706.1995.10484370>, Hocking, R. R. (1976)
<doi:10.2307/2529336>), Hannan and Quinn information criterion(Hannan, E.
J. and Quinn, B. G. (1979) <doi:10.1111/j.2517-6161.1979.tb01072.x>,
Mcquarrie, A. D. R. and Tsai, C. L. (1998) <doi:10.1142/3573>), corrected
Hannan and Quinn information criterion(Mcquarrie, A. D. R. and Tsai, C. L.
(1998) <doi:10.1142/3573>), Schwarz criterion(Schwarz, G. (1978)
<doi:10.1214/aos/1176344136>, Judge, G. G. (1985) <doi:10.2307/1391738>),
adjusted R-square statistic(Darlington, R. B. (1968)
<doi:10.1037/h0025471>, Judge, G. G. (1985) <doi:10.2307/1391738>) and
significance levels(Mckeon, J. J. (1974) <doi:10.1093/biomet/61.2.381>,
Harold Hotelling. (1992) <doi:10.1007/978-1-4612-0919-5_4>, Pillai, K. C.
S. (2006) <doi:10.1002/0471667196.ess1965.pub2>), where multicollinearity
can be detected with checking tolerance value.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
