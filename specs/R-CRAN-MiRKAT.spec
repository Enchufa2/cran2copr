%global packname  MiRKAT
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Microbiome Regression-Based Analysis Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-GUniFrac 
BuildRequires:    R-CRAN-PearsonDS 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ecodist 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-GUniFrac 
Requires:         R-CRAN-PearsonDS 
Requires:         R-CRAN-lme4 
Requires:         R-Matrix 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-mixtools 
Requires:         R-survival 
Requires:         R-CRAN-ecodist 
Requires:         R-stats 

%description
Test for overall association between microbiome composition data and
phenotypes via phylogenetic kernels. The phenotype can be univariate
continuous or binary (Zhao et al. (2015)
<doi:10.1016/j.ajhg.2015.04.003>), survival outcomes (Plantinga et al.
(2017) <doi:10.1186/s40168-017-0239-9>), multivariate (Zhan et al. (2017)
<doi:10.1002/gepi.22030>) and structured phenotypes (Zhan et al. (2017)
<doi:10.1111/biom.12684>). The package can also use robust and quantile
regression (Fu et al. (2020+), in preparation). In each case, the
microbiome community effect is modeled nonparametrically through a kernel
function, which can incorporate phylogenetic tree information.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
