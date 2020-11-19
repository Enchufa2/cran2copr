%global packname  mixComp
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the Order of Mixture Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-kdensity 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-kdensity 

%description
Methods for estimating the order of a mixture model. The approaches
considered are based on the following papers (the extended list of
references is available in the vignette): 1. Dacunha-Castelle, Didier, and
Elisabeth Gassiat. The estimation of the order of a mixture model.
Bernoulli 3, no. 3 (1997): 279-299.
<https://projecteuclid.org/download/pdf_1/euclid.bj/1177334456>. 2. Woo,
Mi-Ja, and T. N. Sriram. Robust estimation of mixture complexity. Journal
of the American Statistical Association 101, no. 476 (2006): 1475-1486.
<doi:10.1198/016214506000000555>. 3. Woo, Mi-Ja, and T. N. Sriram. Robust
estimation of mixture complexity for count data. Computational statistics
& data analysis 51, no. 9 (2007): 4379-4392.
<doi:10.1016/j.csda.2006.06.006>. 4. Umashanger, T., and T. N. Sriram. L2E
estimation of mixture complexity for count data. Computational statistics
& data analysis 53, no. 12 (2009): 4243-4254.
<doi:10.1016/j.csda.2009.05.013>. 5. Karlis, Dimitris, and Evdokia
Xekalaki. On testing for the number of components in a mixed Poisson
model. Annals of the Institute of Statistical Mathematics 51, no. 1
(1999): 149-162. <doi:10.1023/A:1003839420071>. 6. Cutler, Adele, and Olga
I. Cordero-Brana. Minimum Hellinger Distance Estimation for Finite Mixture
Models. Journal of the American Statistical Association 91, no. 436
(1996): 1716-1723. <doi:10.2307/2291601>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
