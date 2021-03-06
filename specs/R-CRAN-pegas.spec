%global packname  pegas
%global packver   0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14
Release:          1%{?dist}%{?buildtag}
Summary:          Population and Evolutionary Genetics Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-ape >= 5.3.11
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape >= 5.3.11
Requires:         R-CRAN-adegenet 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 

%description
Functions for reading, writing, plotting, analysing, and manipulating
allelic and haplotypic data, including from VCF files, and for the
analysis of population nucleotide sequences and micro-satellites including
coalescent analyses, linkage disequilibrium, population structure (Fst,
Amova) and equilibrium (HWE), haplotype networks, minimum spanning tree
and network, and median-joining networks.

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
