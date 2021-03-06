%global packname  CLVTools
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Customer Lifetime Value Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-optimx >= 2019.12.02
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-Matrix >= 1.2.17
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.500.2.0
BuildRequires:    R-CRAN-RcppGSL >= 0.3.7
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-optimx >= 2019.12.02
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-Matrix >= 1.2.17
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-utils 

%description
Probabilistic latent customer attrition models (also known as
"buy-'til-you-die models") are used to predict future purchase behavior of
customers. This package includes fast and accurate implementations of
various probabilistic latent customer attrition models for non-contractual
settings (e.g., retail business) with and without time-invariant and
time-varying covariates. Currently, the package includes the Pareto/NBD
model (Pareto/Negative-Binomial-Distribution), the BG/NBD mode
(Beta-Gamma/Negative-Binomial-Distribution) and the GGom/NBD
(Gamma-Gompertz/Negative-Binomial-Distribution) for the purchase and the
attrition processes as well as the Gamma/Gamma model for the spending
process. For reference to the Pareto/NBD model, see Schmittlein DC,
Morrison DG, Colombo R (1987) <doi:10.1287/mnsc.33.1.1>, for the BG/NBD
model, see Fader PS, Hardie BG, Lee K (2005) <doi:10.1287/mksc.1040.0098>
and for the GGom/NBD model see Bemmaor AC, Glady N (2012)
<doi:10.1287/mnsc.1110.1461>. For reference to the Gamma/Gamma model, see
Fader PS, Hardie BG, Lee K (2005) <doi:10.1509/jmkr.2005.42.4.415>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
