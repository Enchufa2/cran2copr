%global packname  HDLSSkST
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Distribution-Free Exact High Dimensional Low Sample Size k-Sample Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-stats 
Requires:         R-utils 

%description
Testing homogeneity of k multivariate distributions is a classical and
challenging problem in statistics, and this becomes even more challenging
when the dimension of the data exceeds the sample size. We construct some
tests for this purpose which are exact level (size) alpha tests based on
clustering. These tests are easy to implement and distribution-free in
finite sample situations. Under appropriate regularity conditions, these
tests have the consistency property in HDLSS asymptotic regime, where the
dimension of data grows to infinity while the sample size remains fixed.
We also consider a multiscale approach, where the results for different
number of partitions are aggregated judiciously. Details are in Biplab
Paul, Shyamal K De and Anil K Ghosh (2020); Soham Sarkar and Anil K Ghosh
(2019) <doi:10.1109/TPAMI.2019.2912599>; William M Rand (1971)
<doi:10.1080/01621459.1971.10482356>; Cyrus R Mehta and Nitin R Patel
(1983) <doi:10.2307/2288652>; Joseph C Dunn (1973)
<doi:10.1080/01969727308546046>; Sture Holm (1979) <doi:10.2307/4615733>;
Yoav Benjamini and Yosef Hochberg (1995) <doi: 10.2307/2346101>.

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
